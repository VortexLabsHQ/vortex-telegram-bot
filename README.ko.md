# Vortex 🤖 — 나만의 텔레그램 그룹 어시스턴트

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · **한국어** · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Vortex가 마음에 드신다면, GitHub에서 이 프로젝트에 스타를 눌러주시고 [@VortexLabsHQ](https://github.com/VortexLabsHQ)를 팔로우해 주세요** — 더 많은 분들이 찾을 수 있게 도와줍니다. 감사합니다!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex란 무엇인가요?

Vortex는 내 그룹과 개인 채팅에 상주하며 AI 채팅 모델로 사람들에게 답장하는 텔레그램 봇입니다. 봇의 이름(기본 이름은 **Vortex**)을 부르면 응답합니다 — 대화, 웹 검색, 이미지 생성, 가격 확인, 농담, 파일 읽기, 음성 메시지 변환 등 다양한 기능을 제공합니다.

내 서버에서, 내 국가와 언어로 실행됩니다. 당신이 주인입니다: 숨겨진 `/admin` 패널로 AI 키, 사용자, 설정을 관리할 수 있습니다.

## 기능

- 💬 **AI 채팅** — 그룹에서는 호출어로, 개인 채팅에서는 호출어 없이
- 🔑 **토큰 풀** — 여러 LLM 제공자와 키를 사용, 자동 순환 및 장애 조치
- 🖼️ **이미지 생성 및 편집** — 무료(DuckAI) 또는 유료 제공자
- 🔍 **웹 검색** — 자체 호스팅 SearXNG, 위키백과 폴백 지원
- 💰 **실시간 가격** — 통화, 금, 원유, 암호화폐를 내 통화로 표시
- 🕌 **기도 시간**, 🃏 **운세**, 😄 **농담**, 🎲 **주사위와 동전 던지기**
- 📎 **파일 분석** 및 **음성 변환**
- 📥 **다운로드** — 링크를 보내면 미디어 파일을 받아옵니다 (최대 45 MB)
- 🌍 **195개 국가**와 **40개 언어** — 국가와 언어는 별도 설정
- 🔄 **자동 업데이트** — 매일 새 릴리스 확인, 업데이트 전 확인
- 🛡️ **숨겨진 /admin 패널** — 토큰, 사용자, 통계, 채팅, 이미지 모델, 관리자, 권한

## 설치 전 준비사항

**Linux**가 실행되는 서버(또는 항상 켜진 컴퓨터)가 필요하며, 다음이 설치되어 있어야 합니다:

| 항목 | 확인 방법 | 예상 결과 |
| --- | --- | --- |
| **Python 3.11 이상** | `python3 --version` | `Python 3.11.x` 이상 (3.12, 3.13도 가능) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` 또는 `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` 또는 유사 |
| **Docker** *(선택 사항)* | `docker --version` | `Docker version 2x.x.x` — 선택 사항인 SearXNG 웹 검색을 원할 때만 필요 |

누락된 것이 있으면, 한 명령어로 모두 설치하세요 (`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

선택 사항인 `Docker`용 (웹 검색 `SearXNG`를 원할 때만 필요):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

마지막 줄 이후, 로그아웃했다가 다시 로그인하세요 (또는 `docker` 명령을 `sudo`로 실행하세요). 설치 프로그램은 `Debian/Ubuntu`에서 `apt`로 누락된 도구를 자동으로 설치해 주기도 합니다. 다른 시스템에서는 패키지 관리자로 먼저 설치하세요. `systemd`는 시스템에 기본 포함되어 있어 별도로 설치할 수 없습니다.

텔레그램에서 두 가지가 더 필요합니다(둘 다 무료):

1. **봇 토큰** — 텔레그램에서 [@BotFather](https://t.me/BotFather)에게 말 걸어 `/newbot`을 보내고, 받은 토큰을 복사하세요.
2. **숫자 텔레그램 사용자 ID** — [@userinfobot](https://t.me/userinfobot)에게 말 걸어 표시된 숫자를 복사하세요. 이 ID가 '주인' ID가 되어, 이 계정만 `/admin`을 사용할 수 있습니다.

## 설치

한 줄 명령어입니다. 복사해서 터미널에 붙여넣고 Enter를 누르세요:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

설치 프로그램이 순서대로 여섯 가지를 묻습니다:

1. **국가** — 아래 [국가 표](#countries)에 나온 영문 국가명을 **그대로** 붙여넣으세요 (예: `Turkey`). 국가가 시간대, 가격 표시 통화, 기도 시간, 로컬 콘텐츠를 결정합니다.
2. **언어** — 봇이 사용할 언어 (예: `en`, `fa`, `tr`). 엔터를 눌러 국가 기본값을 그대로 쓰세요. 언어는 국가와 별개라 봇 말투만 바뀌며, 나중에 `/admin`에서 변경 가능합니다.
3. **봇 토큰** — [@BotFather](https://t.me/BotFather)에서 받은 토큰을 붙여넣으세요. 설치 프로그램이 텔레그램과 실시간으로 확인합니다.
4. **관리자 숫자 ID** — [@userinfobot](https://t.me/userinfobot)에서 확인한 본인의 텔레그램 사용자 ID.
5. **봇 이름 / 깨우기 단어** — 그룹에서 봇을 부를 때 말할 이름. 아무 언어나 괜찮습니다 (예: `Vortex` 또는 `ورتکس`). 엔터면 기본값 `Vortex`로 설정됩니다.
6. **첫 번째 LLM 제공자** — 하나 선택: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, 또는 **Custom** (베이스 URL 직접 입력). 선택한 제공자의 API 키를 붙여넣으면 설치 프로그램이 실시간 모델 목록을 가져와 모델을 고르게 합니다.

그러면 설치 프로그램이 의존성을 설치하고, `.env` 파일을 작성하고, `vortex-bot` systemd 서비스를 만들고, 웹 검색용 SearXNG 설치(Docker 필요) 여부를 묻고, 봇을 시작합니다.

> ⚠️ **Anthropic은 직접 사용 불가.** Anthropic 네이티브 API는 OpenAI 호환이 아니며, 이 봇은 OpenAI 호환 API만 지원합니다. Anthropic을 고르면 설치 프로그램이 경고합니다: 해당 키는 OpenAI 호환 게이트웨이를 거쳐야만 작동합니다. 대신 OpenRouter나 목록의 다른 제공자를 쓰세요.

## 설치 후

봇이 실행 중인지 확인하세요:

```bash
systemctl status vortex-bot
```

`active (running)`으로 나와야 합니다. 실시간 로그를 보려면:

```bash
journalctl -u vortex-bot -f
```

이제 텔레그램에서 봇과 대화해 보세요:

- `/start` 보내기 — 봇이 인사합니다.
- **개인 채팅**에서는 그냥 말을 걸면 됩니다 — 깨우기 단어 필요 없음.
- **그룹**에 봇을 추가한 뒤 그룹 프라이버시를 끄세요: [@BotFather](https://t.me/BotFather)에서 `/setprivacy`를 보내고, 본인의 봇을 선택한 뒤 **Disable**을 선택하세요 — 그렇지 않으면 봇이 그룹 메시지를 볼 수 없고 웨이크 워드를 듣지 못합니다. 그런 다음 봇 이름을 부르세요, 예: `Vortex what's the time?`
- 관리자(보스)라면 개인 채팅에서 `/admin`을 보내 숨겨진 관리자 패널을 여세요.

**업데이트는 자동입니다.** 하루에 한 번 GitHub에서 새 릴리스를 확인합니다. 업데이트가 있으면 ✅ / ❌ 버튼이 달린 비공개 메시지를 보냅니다. ✅를 누르면 스스로 업데이트하고 재시작합니다 — 서버에 손댈 필요 전혀 없습니다.

## 설정

모든 설정은 설치 디렉터리의 `.env` 파일에 있습니다. 모든 옵션은 [`.env.example`](.env.example)을 참고하세요. 가장 중요한 것들:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | 텔레그램 봇 토큰 (@BotFather에서 발급) |
| `BOSS_ID` | 본인의 숫자 텔레그램 사용자 ID (봇 소유자) |
| `BOT_NAME` | 그룹에서 사용할 봇 이름과 호출어 (기본값 `Vortex`) |
| `BOT_COUNTRY` | 영문 국가명, 예: `United States` (시간대, 통화, 기도 시간 설정) |
| `BOT_LANGUAGE` | 봇 언어 코드, 예: `en`, `fa`, `tr` (봇이 말하는 언어만 변경) |
| `LLM_PROVIDERS` | LLM 공급자 및 키: `base_url\|api_key\|model`, 쉼표로 구분 |
| `UPDATE_CHECK_ENABLED` | `1` = 매일 업데이트 확인, `0` = 확인 안 함 |
| `UPDATE_REPO` | 릴리스를 감시할 저장소 (기본값 `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | 웹 검색: `searxng` (기본값), `tavily`, 또는 `serper` |
| `DAILY_LIMIT_MESSAGES` | 사용자당 하루 최대 봇 응답 수 (기본값 `30`, 보스는 예외) |

국가와 언어는 나중에 숨겨진 `/admin` 패널(Language & Country)에서 파일 수정 없이 변경할 수 있습니다.

## Docker 대안

설치 프로그램 대신 Docker를 선호한다면:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

이 명령으로 봇과 자체 호스팅 SearXNG 검색 엔진이 함께 실행됩니다. `docker compose logs -f bot`으로 로그를 확인하세요.

참고: 자동 셀프 업데이터는 systemd 서비스가 필요하므로, Docker에서는 업데이트가 수동입니다: `git pull` 후 `docker compose up -d --build`를 다시 실행하세요.

## 기능 상세

### `/admin` 패널

비공개 채팅에서 `/admin`을 보내세요 (보스만 가능 — 아무도 열 수 없고, `/help`나 메뉴에도 절대 나타나지 않습니다). 포함된 기능:

- 🔑 **토큰 & 모델** — LLM 키 추가/제거, 키 상태 확인, 활성 모델 선택, 공급자의 실시간 모델 목록 탐색
- 👥 **사용자** — 사용자 수, 차단/차단 해제, 허용 목록
- 📊 **통계** — 사용량 수치
- 💬 **최근 대화** — 사람들이 봇에게 한 말 (보스만, 비공개)
- 🖼️ **이미지 모델** — DuckAI (무료, 기본값), HiLinkUp, 커스텀 이미지 서비스, 또는 끄기
- 🛡️ **매니저** — 신뢰할 수 있는 사람에게 패널 일부 권한 부여
- 🟢/🔴 **전원** — 모두에 대한 봇 켜기/끄기 (보스는 계속 제어 가능)
- 🌍 **언어 & 국가** — 언제든 봇의 언어 또는 국가 변경

### 토큰 풀

봇은 여러 LLM 공급자의 키를 동시에 보유할 수 있습니다. 정상 키 사이를 순환하며, 하나가 작동하지 않으면 자동으로 페일오버합니다. `/admin`에서 한 모델을 고정하거나, 직접 모델을 선택하거나, 봇이 자유롭게 순환하게 둘 수 있습니다. OpenAI 호환 API를 가진 모든 공급자가 작동합니다 — 대형 업체뿐만 아니라 소규모 애그리게이터도 포함됩니다.

### 이미지

이미지 생성은 세 가지 모드가 있습니다: **DuckAI** (무료, 키 불필요, 기본값), **HiLinkUp** (유료, 더 나은 품질), 또는 직접 구축한 **커스텀** OpenAI 호환 이미지 서비스. 봇에게 사진을 보내고 어떻게 편집할지 말하면("이걸 만화 스타일로 만들어"), 새 이미지를 생성해 줍니다. 이미지 생성은 `/admin`에서 끌 수 있습니다.

### 국가와 언어

Vortex는 **195개 국가**와 **40개 언어**를 지원합니다. 국가는 시간대, 가격 표시 통화, 기도 시간용 도시, 현지 콘텐츠를 결정합니다. 언어는 봇이 말하는 내용만 설정합니다. 예를 들어 벨기에 그룹에서 국가를 벨기에로, 언어를 영어로 설정할 수 있습니다. 둘 다 나중에 `/admin`에서 변경할 수 있습니다.

### Updates

봇은 하루에 한 번 `VortexLabsHQ/vortex-telegram-bot`의 GitHub 릴리스를 확인합니다. 새 버전이 나오면 ✅ / ❌ 버튼과 함께 관리자에게 비공개 메시지를 보냅니다. 수락하면 코드가 업데이트되고 봇이 재시작됩니다. 저장소가 비공개인 동안에는 확인 기능이 조용히 아무 작업도 하지 않습니다(GitHub API는 공개 저장소가 필요함) — 절대 확인을 원하지 않으면 `UPDATE_CHECK_ENABLED=0`으로 설정하세요.

## Troubleshooting / FAQ

**설치 프로그램이 토큰이 유효하지 않다고 합니다.**
토큰은 [@BotFather](https://t.me/BotFather)에서 발급받습니다. 토큰 전체(숫자, 콜론, 이후 35자 이상)를 공백 없이 복사했는지 확인하세요. 봇을 삭제했거나 새 토큰을 발급받았다면 기존 토큰은 작동하지 않습니다. 새 토큰을 붙여넣으세요.

**봇이 그룹에서 응답하지 않습니다.**
확인해야 할 네 가지: (1) 그룹 프라이버시가 꺼져 있어야 합니다 — [@BotFather](https://t.me/BotFather)에서 `/setprivacy`를 보내고, 봇을 선택한 뒤 **Disable**을 선택하세요; 프라이버시가 켜져 있으면 봇이 그룹 메시지를 전혀 볼 수 없습니다, (2) 봇이 그룹에 추가되어 있어야 합니다, (3) 웨이크 워드(봇 이름)를 말해야 합니다 — 예: `Vortex what's the time?` — 봇은 그룹에서 이름이 호출될 때만 듣습니다, (4) 개인 채팅에서는 웨이크 워드가 전혀 필요하지 않습니다.

**봇이 내 언어가 아닌 영어로 응답합니다.**
`/admin`(관리자만) → 언어 및 국가로 이동해 언어를 선택하세요. 설치 프로그램에서도 언어를 묻습니다. 거기서 Enter를 누르면 국가 기본값이 적용됩니다.

**Anthropic을 선택했는데 봇이 대화하지 않습니다.**
Anthropic 네이티브 API는 OpenAI 호환이 아니어서 봇이 직접 대화할 수 없습니다. OpenRouter를 사용하세요(OpenAI 호환 API로 Claude 모델 제공). 또는 목록에서 다른 공급자를 선택하세요.

**웹 검색이 작동하지 않습니다.**
웹 검색에는 SearXNG가 필요하며, 설치 프로그램이 Docker로 설정해 줍니다. 없으면 봇은 Wikipedia로 대체되는데, 이는 기능이 약합니다. `.env`에서 `SEARCH_API_KEY`와 함께 `SEARCH_PROVIDER=tavily` 또는 `serper`로 설정할 수도 있습니다.

**로그는 어디에 있나요?**
`journalctl -u vortex-bot -f`로 실시간 로그를 볼 수 있습니다. `systemctl status vortex-bot`으로 서비스 실행 여부를 확인하세요. 봇이 멈췄다면 `sudo systemctl restart vortex-bot`으로 다시 시작하세요.

**봇이 일일 한도에 도달했다고 합니다.**
사용자당 하루 30회 봇 응답이 가능합니다(관리자는 예외). 한도는 봇 국가 시간대 기준 자정에 초기화됩니다. `.env`에서 `DAILY_LIMIT_MESSAGES`로 늘리거나 관리자에게 문의하세요.

**버그를 발견했어요 / 아이디어가 있어요.**
GitHub에 이슈를 열어 주세요. 신고 방법과 수정 제출 방법은 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

## Development

```bash
git clone https://github.com/VortexLabsHQ/vortex-telegram-bot.git
cd vortex-telegram-bot

python3.11 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
pip install ruff

cp .env.example .env   # then fill in your own BOT_TOKEN and LLM key(s)
python -m bot.main
```

테스트 실행(일반 Python 스크립트, pytest 불필요):

```bash
python tests/test_admin.py
python tests/test_admin_keys.py
python tests/test_admin_select.py
python tests/test_admin_power.py
python tests/test_admin_image.py
python tests/test_fixes.py
python tests/test_installer.py
python tests/test_locale.py
python tests/test_updater.py
```

풀 리퀘스트를 열기 전에 아홉 개 테스트 스위트가 모두 통과해야 합니다. 코드 스타일(ruff)과 PR 절차는 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.

## License

Vortex는 [MIT 라이선스](LICENSE)로 배포됩니다. 어떤 목적으로든 자유롭게 사용, 복사, 수정, 공유할 수 있습니다.

<a id="countries"></a>

## Countries

설치 프로그램이 국가를 묻을 때, 국가 이름을 **영어로, 여기에 적힌 그대로** 붙여넣으세요. 이 표는 `bot/countries.py`에서 생성됩니다 — 여기에 있는 이름과 저기에 있는 이름이 다르다면, `bot/countries.py`가 우선합니다.

<!-- COUNTRY_TABLE_START -->

| Country | Time zone | Currency | Capital |
| --- | --- | --- | --- |
| Iran | Asia/Tehran | IRR | Tehran |
| Turkey | Europe/Istanbul | TRY | Ankara |
| United States | America/New_York | USD | Washington |
| United Kingdom | Europe/London | GBP | London |
| Germany | Europe/Berlin | EUR | Berlin |
| France | Europe/Paris | EUR | Paris |
| Spain | Europe/Madrid | EUR | Madrid |
| Italy | Europe/Rome | EUR | Rome |
| Netherlands | Europe/Amsterdam | EUR | Amsterdam |
| Belgium | Europe/Brussels | EUR | Brussels |
| Russia | Europe/Moscow | RUB | Moscow |
| Ukraine | Europe/Kyiv | UAH | Kyiv |
| Poland | Europe/Warsaw | PLN | Warsaw |
| Sweden | Europe/Stockholm | SEK | Stockholm |
| Brazil | America/Sao_Paulo | BRL | Brasília |
| Mexico | America/Mexico_City | MXN | Mexico City |
| Argentina | America/Argentina/Buenos_Aires | ARS | Buenos Aires |
| Saudi Arabia | Asia/Riyadh | SAR | Riyadh |
| United Arab Emirates | Asia/Dubai | AED | Abu Dhabi |
| Egypt | Africa/Cairo | EGP | Cairo |
| Morocco | Africa/Casablanca | MAD | Rabat |
| India | Asia/Kolkata | INR | New Delhi |
| Pakistan | Asia/Karachi | PKR | Islamabad |
| China | Asia/Shanghai | CNY | Beijing |
| Japan | Asia/Tokyo | JPY | Tokyo |
| South Korea | Asia/Seoul | KRW | Seoul |
| Indonesia | Asia/Jakarta | IDR | Jakarta |
| Thailand | Asia/Bangkok | THB | Bangkok |
| Vietnam | Asia/Ho_Chi_Minh | VND | Hanoi |
| Australia | Australia/Sydney | AUD | Canberra |
| Nigeria | Africa/Lagos | NGN | Abuja |
| Kenya | Africa/Nairobi | KES | Nairobi |
| Afghanistan | Asia/Kabul | AFN | Kabul |
| Albania | Europe/Tirane | ALL | Tirana |
| Algeria | Africa/Algiers | DZD | Algiers |
| Andorra | Europe/Andorra | EUR | Andorra la Vella |
| Angola | Africa/Luanda | AOA | Luanda |
| Antigua & Barbuda | America/Antigua | XCD | St. John's |
| Armenia | Asia/Yerevan | AMD | Yerevan |
| Austria | Europe/Vienna | EUR | Vienna |
| Azerbaijan | Asia/Baku | AZN | Baku |
| Bahamas | America/Nassau | BSD | Nassau |
| Bahrain | Asia/Bahrain | BHD | Manama |
| Bangladesh | Asia/Dhaka | BDT | Dhaka |
| Barbados | America/Barbados | BBD | Bridgetown |
| Belarus | Europe/Minsk | BYN | Minsk |
| Belize | America/Belize | BZD | Belmopan |
| Benin | Africa/Porto-Novo | XOF | Porto-Novo |
| Bhutan | Asia/Thimphu | BTN | Thimphu |
| Bolivia | America/La_Paz | BOB | Sucre |
| Bosnia & Herzegovina | Europe/Sarajevo | BAM | Sarajevo |
| Botswana | Africa/Gaborone | BWP | Gaborone |
| Brunei | Asia/Brunei | BND | Bandar Seri Begawan |
| Bulgaria | Europe/Sofia | EUR | Sofia |
| Burkina Faso | Africa/Ouagadougou | XOF | Ouagadougou |
| Burundi | Africa/Bujumbura | BIF | Gitega |
| Cambodia | Asia/Phnom_Penh | KHR | Phnom Penh |
| Cameroon | Africa/Douala | XAF | Yaounde |
| Canada | America/Toronto | CAD | Ottawa |
| Cape Verde | Atlantic/Cape_Verde | CVE | Praia |
| Central African Republic | Africa/Bangui | XAF | Bangui |
| Chad | Africa/Ndjamena | XAF | N'Djamena |
| Chile | America/Santiago | CLP | Santiago |
| Colombia | America/Bogota | COP | Bogota |
| Comoros | Indian/Comoro | KMF | Moroni |
| Congo - Brazzaville | Africa/Brazzaville | XAF | Brazzaville |
| Congo - Kinshasa | Africa/Kinshasa | CDF | Kinshasa |
| Costa Rica | America/Costa_Rica | CRC | San Jose |
| Croatia | Europe/Zagreb | EUR | Zagreb |
| Cuba | America/Havana | CUP | Havana |
| Cyprus | Asia/Nicosia | EUR | Nicosia |
| Czechia | Europe/Prague | CZK | Prague |
| Côte d’Ivoire | Africa/Abidjan | XOF | Yamoussoukro |
| Denmark | Europe/Copenhagen | DKK | Copenhagen |
| Djibouti | Africa/Djibouti | DJF | Djibouti |
| Dominica | America/Dominica | XCD | Roseau |
| Dominican Republic | America/Santo_Domingo | DOP | Santo Domingo |
| Ecuador | America/Guayaquil | USD | Quito |
| El Salvador | America/El_Salvador | USD | San Salvador |
| Equatorial Guinea | Africa/Malabo | XAF | Ciudad de la Paz |
| Eritrea | Africa/Asmara | ERN | Asmara |
| Estonia | Europe/Tallinn | EUR | Tallinn |
| Eswatini | Africa/Mbabane | SZL | Mbabane |
| Ethiopia | Africa/Addis_Ababa | ETB | Addis Ababa |
| Fiji | Pacific/Fiji | FJD | Suva |
| Finland | Europe/Helsinki | EUR | Helsinki |
| Gabon | Africa/Libreville | XAF | Libreville |
| Gambia | Africa/Banjul | GMD | Banjul |
| Georgia | Asia/Tbilisi | GEL | Tbilisi |
| Ghana | Africa/Accra | GHS | Accra |
| Greece | Europe/Athens | EUR | Athens |
| Grenada | America/Grenada | XCD | St. George's |
| Guatemala | America/Guatemala | GTQ | Guatemala City |
| Guinea | Africa/Conakry | GNF | Conakry |
| Guinea-Bissau | Africa/Bissau | XOF | Bissau |
| Guyana | America/Guyana | GYD | Georgetown |
| Haiti | America/Port-au-Prince | HTG | Port-au-Prince |
| Honduras | America/Tegucigalpa | HNL | Tegucigalpa |
| Hungary | Europe/Budapest | HUF | Budapest |
| Iceland | Atlantic/Reykjavik | ISK | Reykjavik |
| Iraq | Asia/Baghdad | IQD | Baghdad |
| Ireland | Europe/Dublin | EUR | Dublin |
| Israel | Asia/Jerusalem | ILS | Jerusalem |
| Jamaica | America/Jamaica | JMD | Kingston |
| Jordan | Asia/Amman | JOD | Amman |
| Kazakhstan | Asia/Almaty | KZT | Astana |
| Kiribati | Pacific/Tarawa | AUD | Tarawa |
| Kuwait | Asia/Kuwait | KWD | Kuwait City |
| Kyrgyzstan | Asia/Bishkek | KGS | Bishkek |
| Laos | Asia/Vientiane | LAK | Vientiane |
| Latvia | Europe/Riga | EUR | Riga |
| Lebanon | Asia/Beirut | LBP | Beirut |
| Lesotho | Africa/Maseru | LSL | Maseru |
| Liberia | Africa/Monrovia | LRD | Monrovia |
| Libya | Africa/Tripoli | LYD | Tripoli |
| Liechtenstein | Europe/Vaduz | CHF | Vaduz |
| Lithuania | Europe/Vilnius | EUR | Vilnius |
| Luxembourg | Europe/Luxembourg | EUR | Luxembourg |
| Madagascar | Indian/Antananarivo | MGA | Antananarivo |
| Malawi | Africa/Blantyre | MWK | Lilongwe |
| Malaysia | Asia/Kuala_Lumpur | MYR | Kuala Lumpur |
| Maldives | Indian/Maldives | MVR | Male |
| Mali | Africa/Bamako | XOF | Bamako |
| Malta | Europe/Malta | EUR | Valletta |
| Marshall Islands | Pacific/Majuro | USD | Majuro |
| Mauritania | Africa/Nouakchott | MRU | Nouakchott |
| Mauritius | Indian/Mauritius | MUR | Port Louis |
| Micronesia | Pacific/Pohnpei | USD | Palikir |
| Moldova | Europe/Chisinau | MDL | Chisinau |
| Monaco | Europe/Monaco | EUR | Monaco |
| Mongolia | Asia/Ulaanbaatar | MNT | Ulaanbaatar |
| Montenegro | Europe/Podgorica | EUR | Podgorica |
| Mozambique | Africa/Maputo | MZN | Maputo |
| Myanmar | Asia/Yangon | MMK | Nay Pyi Taw |
| Namibia | Africa/Windhoek | NAD | Windhoek |
| Nauru | Pacific/Nauru | AUD | Yaren |
| Nepal | Asia/Kathmandu | NPR | Kathmandu |
| New Zealand | Pacific/Auckland | NZD | Wellington |
| Nicaragua | America/Managua | NIO | Managua |
| Niger | Africa/Niamey | XOF | Niamey |
| North Korea | Asia/Pyongyang | KPW | Pyongyang |
| North Macedonia | Europe/Skopje | MKD | Skopje |
| Norway | Europe/Oslo | NOK | Oslo |
| Oman | Asia/Muscat | OMR | Muscat |
| Palau | Pacific/Palau | USD | Melekeok |
| Palestine | Asia/Hebron | ILS | Ramallah |
| Panama | America/Panama | USD | Panama City |
| Papua New Guinea | Pacific/Port_Moresby | PGK | Port Moresby |
| Paraguay | America/Asuncion | PYG | Asuncion |
| Peru | America/Lima | PEN | Lima |
| Philippines | Asia/Manila | PHP | Manila |
| Portugal | Europe/Lisbon | EUR | Lisbon |
| Qatar | Asia/Qatar | QAR | Doha |
| Romania | Europe/Bucharest | RON | Bucharest |
| Rwanda | Africa/Kigali | RWF | Kigali |
| Samoa | Pacific/Apia | WST | Apia |
| San Marino | Europe/San_Marino | EUR | San Marino |
| Senegal | Africa/Dakar | XOF | Dakar |
| Serbia | Europe/Belgrade | RSD | Belgrade |
| Seychelles | Indian/Mahe | SCR | Victoria |
| Sierra Leone | Africa/Freetown | SLE | Freetown |
| Singapore | Asia/Singapore | SGD | Singapore |
| Slovakia | Europe/Bratislava | EUR | Bratislava |
| Slovenia | Europe/Ljubljana | EUR | Ljubljana |
| Solomon Islands | Pacific/Guadalcanal | SBD | Honiara |
| Somalia | Africa/Mogadishu | SOS | Mogadishu |
| South Africa | Africa/Johannesburg | ZAR | Pretoria |
| South Sudan | Africa/Juba | SSP | Juba |
| Sri Lanka | Asia/Colombo | LKR | Colombo |
| St. Kitts & Nevis | America/St_Kitts | XCD | Basseterre |
| St. Lucia | America/St_Lucia | XCD | Castries |
| St. Vincent & Grenadines | America/St_Vincent | XCD | Kingstown |
| Sudan | Africa/Khartoum | SDG | Khartoum |
| Suriname | America/Paramaribo | SRD | Paramaribo |
| Switzerland | Europe/Zurich | CHF | Bern |
| Syria | Asia/Damascus | SYP | Damascus |
| São Tomé & Príncipe | Africa/Sao_Tome | STN | Sao Tome |
| Tajikistan | Asia/Dushanbe | TJS | Dushanbe |
| Tanzania | Africa/Dar_es_Salaam | TZS | Dodoma |
| Timor-Leste | Asia/Dili | USD | Dili |
| Togo | Africa/Lome | XOF | Lome |
| Tonga | Pacific/Tongatapu | TOP | Nuku'alofa |
| Trinidad & Tobago | America/Port_of_Spain | TTD | Port of Spain |
| Tunisia | Africa/Tunis | TND | Tunis |
| Turkmenistan | Asia/Ashgabat | TMT | Ashgabat |
| Tuvalu | Pacific/Funafuti | AUD | Funafuti |
| Uganda | Africa/Kampala | UGX | Kampala |
| Uruguay | America/Montevideo | UYU | Montevideo |
| Uzbekistan | Asia/Tashkent | UZS | Tashkent |
| Vanuatu | Pacific/Efate | VUV | Port Vila |
| Vatican City | Europe/Vatican | EUR | Vatican City |
| Venezuela | America/Caracas | VES | Caracas |
| Yemen | Asia/Aden | YER | Sanaa |
| Zambia | Africa/Lusaka | ZMW | Lusaka |
| Zimbabwe | Africa/Harare | ZWG | Harare |

<!-- COUNTRY_TABLE_END -->

## 감사합니다

> ⭐ **GitHub에서 이 프로젝트에 별표를 누르고 [@VortexLabsHQ](https://github.com/VortexLabsHQ)를 팔로우해 주세요** — Vortex를 지원하고 다른 사람들이 찾기 쉽게 돕는 가장 간단한 방법입니다. 감사합니다!
