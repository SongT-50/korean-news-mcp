<p align="center">
  <img src="./assets/logo.svg" alt="Korean AI News Hub MCP" width="420">
</p>

<p align="center">
  <strong>한국 뉴스와 글로벌 AI/테크 뉴스를 AI에게 연결합니다</strong><br>
  API 키 없이 바로 사용 가능
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/MCP-Protocol-blue" alt="MCP Protocol">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Claude-supported-d4a574" alt="Claude">
  <img src="https://img.shields.io/badge/Claude_Code-supported-5B21B6" alt="Claude Code">
  <img src="https://img.shields.io/badge/API_Key-불필요-10b981" alt="No API Key">
  <img src="https://img.shields.io/badge/Price-Free-10b981" alt="Free">
  <br>
  <a href="https://render.com/deploy?repo=https://github.com/SongT-50/korean-news-mcp"><img src="https://render.com/images/deploy-to-render-button.svg" alt="Deploy to Render"></a>
</p>

---

## 뭘 할 수 있나요?

AI에게 뉴스를 물어보세요. API 키 없이 바로 작동합니다.

```
"오늘 한국 뉴스 알려줘"
"AI 최신 뉴스 검색해줘"
"Claude 관련 뉴스 찾아줘"
"오늘 뉴스 브리핑 해줘"
"이 기사 읽어줘: https://..."
"지금 트렌딩 뉴스 뭐야"
```

## 제공 도구 (6개)

| 도구 | 설명 |
|------|------|
| `korean_news` | 한국 뉴스 카테고리별 조회 (속보/정치/경제/사회/IT/세계/연예/스포츠) |
| `tech_news` | 글로벌 AI/테크 뉴스 (AI/Claude/OpenAI/MCP/스타트업/개발/클라우드) |
| `news_search` | 키워드 뉴스 검색 (한국어/영어) |
| `trending` | 실시간 트렌딩 뉴스 (한국/글로벌테크) |
| `read_article` | 기사 URL 본문 읽기 |
| `daily_briefing` | 종합 뉴스 브리핑 (한국 + AI + Claude) |

## 데이터 소스

### 한국 뉴스
- 네이버 뉴스 RSS (8개 카테고리)
- Google News 한국판

### 글로벌 AI/테크 뉴스
- Hacker News
- TechCrunch
- The Verge
- Ars Technica
- GeekNews (긱뉴스)
- AI 전문 매체

## 빠른 시작

### 1. Claude Code (권장)

```bash
git clone https://github.com/SongT-50/korean-news-mcp.git
cd korean-news-mcp
pip install -r requirements.txt

# API 키 불필요 — 바로 등록
claude mcp add korean-news -- python server.py
```

### 2. Claude Desktop

```json
{
  "mcpServers": {
    "korean-news": {
      "command": "python",
      "args": ["/path/to/korean-news-mcp/server.py"]
    }
  }
}
```

### 3. MCPize

[MCPize에서 바로 사용하기](https://mcpize.com/mcp/korean-news-hub)

## 사용 예시

### 뉴스 조회
```
"오늘 IT 뉴스 5개만"
"경제 뉴스 알려줘"
"연예 뉴스 최신 3개"
```

### AI/테크 뉴스
```
"Claude 최신 뉴스"
"OpenAI 관련 소식"
"MCP 서버 관련 뉴스"
```

### 검색
```
"바이브코딩 뉴스 검색"
"삼성전자 관련 기사"
```

### 브리핑
```
"오늘 뉴스 브리핑 해줘"
"트렌딩 뉴스 뭐야"
```

### 기사 읽기
```
"이 기사 요약해줘: https://news.example.com/article"
```

## 기술 스택

| 항목 | 기술 |
|------|------|
| 언어 | Python 3.10+ |
| MCP SDK | `mcp[cli]` (FastMCP) |
| RSS | `feedparser` |
| 스크래핑 | `beautifulsoup4` + `httpx` |
| 전송 | stdio / SSE |

## 프로젝트 구조

```
korean-news-mcp/
├── server.py          # MCP 서버 (6개 도구)
├── src/               # 소스 모듈
├── docs/              # 문서
├── requirements.txt   # Python 의존성
├── mcpize.yaml        # MCPize 배포 설정
├── Dockerfile         # 컨테이너 배포
└── README.md          # 이 문서
```

## 라이선스

MIT License

## 만든 사람

**삽질코딩** — AI 코딩으로 실제 제품을 만드는 기록

- YouTube: [삽질코딩](https://www.youtube.com/channel/UCSHxaZHNDOrp0h0Ux8_6CVQ)
- GitHub: [SongT-50](https://github.com/SongT-50)
