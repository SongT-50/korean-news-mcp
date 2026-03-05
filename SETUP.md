# Korean AI News Hub - MCP Server 설치 가이드

## 1. Claude Code에서 설정 (가장 쉬운 방법)

Claude Code 터미널에서 아래 명령어 실행:

```bash
claude mcp add korean-news -- python <YOUR_PATH>/korean-news-mcp/server.py
```

## 2. 수동 설정

`~/.claude/settings.json`의 `mcpServers`에 추가:

```json
{
  "mcpServers": {
    "korean-news": {
      "command": "python",
      "args": ["<YOUR_PATH>/korean-news-mcp/server.py"]
    }
  }
}
```

## 3. 사용법

Claude Code에서 자연어로 사용:

- "오늘 한국 뉴스 알려줘"
- "AI 최신 뉴스 검색해줘"
- "Claude 관련 뉴스 찾아줘"
- "오늘 뉴스 브리핑 해줘"
- "이 기사 읽어줘: https://..."
- "지금 트렌딩 뉴스 뭐야"
- "경제 뉴스 5개만"

## 4. 제공 도구 (Tools)

| 도구 | 설명 |
|------|------|
| `korean_news` | 한국 뉴스 카테고리별 조회 (속보/정치/경제/사회/IT/세계/연예/스포츠) |
| `tech_news` | 글로벌 AI/테크 뉴스 (AI/Claude/OpenAI/MCP/OpenClaw/스타트업/개발/클라우드) |
| `news_search` | 키워드 뉴스 검색 (한국어/영어) |
| `trending` | 실시간 트렌딩 뉴스 (한국/글로벌테크) |
| `read_article` | 기사 URL 본문 읽기 |
| `daily_briefing` | 종합 뉴스 브리핑 (한국 + AI + Claude) |
