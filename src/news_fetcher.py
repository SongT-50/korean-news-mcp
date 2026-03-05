"""Korean & Global News Fetcher - RSS 기반 뉴스 수집 엔진"""

import feedparser
import httpx
from bs4 import BeautifulSoup
from dataclasses import dataclass
from datetime import datetime
from urllib.parse import quote_plus


@dataclass
class NewsArticle:
    title: str
    link: str
    summary: str
    source: str
    published: str
    category: str


# Google News RSS 기반 카테고리 매핑
KOREAN_CATEGORIES = {
    "속보": "한국 속보",
    "정치": "한국 정치",
    "경제": "한국 경제 금융",
    "사회": "한국 사회",
    "IT": "한국 IT 기술 AI",
    "세계": "세계 국제 뉴스",
    "연예": "한국 연예 엔터테인먼트",
    "스포츠": "한국 스포츠",
}

TECH_CATEGORIES = {
    "AI": "AI artificial intelligence LLM",
    "Claude": "Claude Anthropic AI",
    "OpenAI": "OpenAI GPT ChatGPT",
    "MCP": "MCP model context protocol AI agent",
    "OpenClaw": "OpenClaw AI agent framework",
    "스타트업": "tech startup funding",
    "개발": "software development programming coding",
    "클라우드": "AWS cloud computing kubernetes",
}


def _build_google_news_url(query: str, lang: str = "ko", country: str = "KR") -> str:
    encoded = quote_plus(query)
    return (
        f"https://news.google.com/rss/search?"
        f"q={encoded}&hl={lang}&gl={country}&ceid={country}:{lang}"
    )


def _build_google_news_top_url(topic: str, lang: str = "ko", country: str = "KR") -> str:
    topic_map = {
        "headlines": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFZxYUdjU0FtdHZHZ0pMVWlnQVAB",
        "tech": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGRqTVhZU0FtdHZHZ0pMVWlnQVAB",
        "business": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtdHZHZ0pMVWlnQVAB",
        "science": "CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp0Y1RjU0FtdHZHZ0pMVWlnQVAB",
    }
    topic_id = topic_map.get(topic, topic_map["headlines"])
    return (
        f"https://news.google.com/rss/topics/{topic_id}?"
        f"hl={lang}&gl={country}&ceid={country}:{lang}"
    )


def _parse_feed(url: str, category: str, max_items: int = 10) -> list[NewsArticle]:
    articles = []
    try:
        feed = feedparser.parse(url)
        for entry in feed.entries[:max_items]:
            source = ""
            if hasattr(entry, "source") and hasattr(entry.source, "title"):
                source = entry.source.title
            elif " - " in entry.title:
                parts = entry.title.rsplit(" - ", 1)
                source = parts[-1] if len(parts) > 1 else ""

            published = ""
            if hasattr(entry, "published"):
                published = entry.published
            elif hasattr(entry, "updated"):
                published = entry.updated

            summary = ""
            if hasattr(entry, "summary"):
                soup = BeautifulSoup(entry.summary, "html.parser")
                summary = soup.get_text(strip=True)[:300]

            articles.append(NewsArticle(
                title=entry.title,
                link=entry.link,
                summary=summary,
                source=source,
                published=published,
                category=category,
            ))
    except Exception as e:
        articles.append(NewsArticle(
            title=f"[피드 오류] {str(e)}",
            link="",
            summary="",
            source="error",
            published="",
            category=category,
        ))
    return articles


def get_korean_news(category: str = "속보", count: int = 10) -> list[NewsArticle]:
    """한국 뉴스를 카테고리별로 가져옵니다."""
    query = KOREAN_CATEGORIES.get(category, category)
    url = _build_google_news_url(query, lang="ko", country="KR")
    return _parse_feed(url, category, max_items=count)


def get_tech_news(topic: str = "AI", count: int = 10) -> list[NewsArticle]:
    """글로벌 테크/AI 뉴스를 가져옵니다."""
    query = TECH_CATEGORIES.get(topic, topic)
    url = _build_google_news_url(query, lang="en", country="US")
    return _parse_feed(url, topic, max_items=count)


def search_news(query: str, lang: str = "ko", count: int = 10) -> list[NewsArticle]:
    """키워드로 뉴스를 검색합니다."""
    country = "KR" if lang == "ko" else "US"
    url = _build_google_news_url(query, lang=lang, country=country)
    return _parse_feed(url, f"검색: {query}", max_items=count)


def get_trending_news(count: int = 15) -> list[NewsArticle]:
    """현재 한국 헤드라인 뉴스를 가져옵니다."""
    url = _build_google_news_top_url("headlines", lang="ko", country="KR")
    return _parse_feed(url, "헤드라인", max_items=count)


def get_trending_tech(count: int = 15) -> list[NewsArticle]:
    """글로벌 테크 트렌드 뉴스를 가져옵니다."""
    url = _build_google_news_top_url("tech", lang="en", country="US")
    return _parse_feed(url, "글로벌 테크", max_items=count)


async def read_article_content(url: str) -> str:
    """기사 URL에서 본문 텍스트를 추출합니다."""
    try:
        async with httpx.AsyncClient(
            follow_redirects=True,
            timeout=15.0,
            headers={"User-Agent": "Mozilla/5.0 (compatible; NewsBot/1.0)"},
        ) as client:
            resp = await client.get(url)
            resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # 불필요한 태그 제거
        for tag in soup(["script", "style", "nav", "header", "footer", "aside", "ad"]):
            tag.decompose()

        # 기사 본문 추출 시도 (일반적 패턴)
        article = (
            soup.find("article")
            or soup.find("div", class_=lambda c: c and "article" in c.lower() if c else False)
            or soup.find("div", class_=lambda c: c and "content" in c.lower() if c else False)
            or soup.find("div", id=lambda i: i and "content" in i.lower() if i else False)
        )

        if article:
            text = article.get_text(separator="\n", strip=True)
        else:
            # fallback: body의 p 태그들
            paragraphs = soup.find_all("p")
            text = "\n".join(p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 30)

        # 너무 길면 자르기
        if len(text) > 3000:
            text = text[:3000] + "\n\n... (본문이 길어 3000자로 잘림)"

        return text if text.strip() else "본문을 추출할 수 없습니다. 직접 링크를 방문해주세요."

    except Exception as e:
        return f"기사 읽기 실패: {str(e)}\n직접 방문: {url}"


def format_articles(articles: list[NewsArticle]) -> str:
    """기사 목록을 읽기 좋은 텍스트로 포맷합니다."""
    if not articles:
        return "뉴스를 찾을 수 없습니다."

    lines = []
    for i, a in enumerate(articles, 1):
        lines.append(f"### {i}. {a.title}")
        if a.source:
            lines.append(f"   출처: {a.source}")
        if a.published:
            lines.append(f"   시간: {a.published}")
        if a.summary:
            lines.append(f"   요약: {a.summary}")
        lines.append(f"   링크: {a.link}")
        lines.append("")

    return "\n".join(lines)
