# Vortex 🤖 — 您专属的 Telegram 群组助手

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · **中文** · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **如果您喜欢 Vortex，请在 GitHub 上给这个项目点星，并关注 [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — 这能帮助更多人发现它。谢谢！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 什么是 Vortex？

Vortex 是一个 Telegram 机器人，它驻留在你的群组和私聊中，使用 AI 聊天模型回答人们的问题。你叫它的名字（默认名字是 **Vortex**），它就会回复——它能聊天、搜索网页、生成图片、查价格、讲笑话、读取文件、转录语音消息，等等。

它运行在你自己的服务器上，使用你自己的国家和语言。你是老大：一个隐藏的 `/admin` 面板让你管理 AI 密钥、用户和设置。

## 功能

- 💬 **AI 聊天** 在群组中（需唤醒词）和私聊中（无需唤醒词）
- 🔑 **令牌池** — 使用多个 LLM 提供商和密钥，自动轮换和故障转移
- 🖼️ **图像生成** — 使用您自己的图片服务（基础 URL + API 密钥 + 模型），在 `/admin` 中添加
- 🔍 **网络搜索** — 自托管 SearXNG，维基百科备选
- 💰 **实时价格** — 货币、黄金、石油和加密货币，以您的本地货币显示
- 🕌 **祷告时间**，🃏 **运势**，😄 **笑话**，🎲 **掷骰子和抛硬币**
- 📎 **文件分析** 和 **语音转文字**
- 📥 **下载** — 发送链接，获取媒体文件（最高 45 MB）
- 🌍 **195 个国家** 和 **40 种语言** — 国家和语言为独立设置
- 🔄 **自动更新** — 每日检查新版本，更新前询问您
- 🛡️ **隐藏的 /admin 面板** — 令牌、用户、统计、聊天、图像模型、管理员、权力

## 安装前准备

你需要一台运行 **Linux** 的服务器（或一台一直开机的电脑），并已安装以下软件：

| 项目 | 如何检查 | 应该看到的内容 |
| --- | --- | --- |
| **Python 3.11 或更新版本** | `python3 --version` | `Python 3.11.x` 或更高（3.12 和 3.13 也可以） |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` 或 `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` 或类似版本 |
| **Docker** *(可选)* | `docker --version` | `Docker version 2x.x.x` — 仅当你想要可选的 SearXNG 网页搜索时需要 |

如果缺少某些内容，请用一条命令安装所有内容（`Debian/Ubuntu`):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

对于可选的 `docker`（仅在你需要 `SearXNG` 网页搜索时才需要):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

在最后一行之后，请注销并重新登录（或使用 `sudo` 运行 `docker` 命令）。安装程序还会提议在 `Debian/Ubuntu` 上用 `apt` 为你安装缺失的工具。在其他系统上，请先用包管理器安装它们。`systemd` 随系统自带，无法单独安装。

你还需要从 Telegram 获取两样东西（都是免费的）：

1. **Bot Token** — 在 Telegram 找 [@BotFather](https://t.me/BotFather)，发送 `/newbot`，复制它给你的 token。
2. **你的 Telegram 数字用户 ID** — 在 Telegram 找 [@userinfobot](https://t.me/userinfobot)，复制它显示的数字。这是你的「老板」ID：只有这个账号能用 `/admin`。

## 安装

一条命令。复制它，粘贴到终端，然后按回车：

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

安装程序会按顺序问你六个问题：

1. **Country** — 粘贴你国家的英文名称，**必须与下方[国家表](#countries)中的完全一致**（例如 `Turkey`）。国家设置决定时区、价格显示的本地货币、祷告时间和本地内容。
2. **Language** — 机器人使用的语言（例如 `en`、`fa`、`tr`）。按回车接受你国家的默认语言。语言与国家是分开的：它只改变机器人说的话，稍后可以用 `/admin` 修改。
3. **Bot token** — 粘贴来自 [@BotFather](https://t.me/BotFather) 的 token。安装程序会实时与 Telegram 验证。
4. **Boss numeric ID** — 你的 Telegram 用户 ID，从 [@userinfobot](https://t.me/userinfobot) 获取。
5. **Bot name / wake word** — 群里唤醒机器人的名字。任何语言都可以（例如 `Vortex` 或 `ورتکس`）。按回车使用默认值 `Vortex`。
6. **First LLM provider** — 选一个：OpenAI、Anthropic、OpenRouter、Google AI (Gemini)、DeepSeek、Groq、Together AI、Mistral AI、xAI (Grok)、Cohere，或 **Custom**（粘贴基础 URL）。然后粘贴该提供商的 API key —— 安装程序会获取实时模型列表供你选择。

然后安装程序会安装依赖、写入 `.env` 文件、创建 `vortex-bot` systemd 服务、提议安装 SearXNG 用于网页搜索（需要 Docker），并启动机器人。

> ⚠️ **Anthropic 无法直接使用。** Anthropic 原生 API 不兼容 OpenAI，而本机器人只支持 OpenAI 兼容的 API。如果你选 Anthropic，安装程序会警告：该 key 只能通过 OpenAI 兼容的网关使用。请改用 OpenRouter 或列表中的其他提供商。

## 安装后

检查机器人是否正在运行：

```bash
systemctl status vortex-bot
```

您应该会看到 `active (running)`。查看实时日志：

```bash
journalctl -u vortex-bot -f
```

现在打开 Telegram 并与您的机器人对话：

- 发送 `/start` — 机器人会打招呼。
- 在**私聊**中，直接发消息给它 — 不需要唤醒词。
- 在**群组** 中，将机器人添加到群组，然后关闭群组隐私：在 [@BotFather](https://t.me/BotFather) 发送 `/setprivacy`，选择你的机器人，并选择 **Disable** —— 否则机器人无法看到群组消息，也听不到唤醒词。然后说出它的名字，例如：`Vortex what's the time?`
- 作为管理员，在私聊中发送 `/admin` 以打开隐藏的管理面板。

**更新是自动的。** 机器人每天检查一次 GitHub 是否有新版本。如果有新版本，它会发送一条带有 ✅ / ❌ 按钮的私信给您。点击 ✅，它会自动更新并重启 — 您永远不需要操作服务器。

## 配置

所有设置都位于安装目录下的 `.env` 文件中。请参阅 [`.env.example`](.env.example) 查看所有选项。最重要的设置如下：

| 设置 | 作用 |
| --- | --- |
| `BOT_TOKEN` | 您的 Telegram 机器人令牌（来自 @BotFather） |
| `BOSS_ID` | 您的数字 Telegram 用户 ID（机器人所有者） |
| `BOT_NAME` | 群组中的机器人名称和唤醒词（默认 `Vortex`） |
| `BOT_COUNTRY` | 英文国家名，例如 `United States`（设置时区、货币、祈祷时间） |
| `BOT_LANGUAGE` | 机器人语言代码，例如 `en`、`fa`、`tr`（仅更改机器人说的话） |
| `LLM_PROVIDERS` | LLM 提供商和密钥：`base_url\|api_key\|model`，逗号分隔 |
| `UPDATE_CHECK_ENABLED` | `1` = 每日检查更新，`0` = 从不检查 |
| `UPDATE_REPO` | 要监视发布版本的仓库（默认 `VortexLabsHQ/vortex-telegram-bot`） |
| `SEARCH_PROVIDER` | 网络搜索：`searxng`（默认）、`tavily` 或 `serper` |
| `DAILY_LIMIT_MESSAGES` | 每用户每日最大机器人回复数（默认 `30`，所有者不受限制） |

国家和语言稍后也可以通过隐藏的 `/admin` 面板（语言和国家）更改，无需编辑任何文件。

## Docker 替代方案

如果您更倾向于使用 Docker 而非安装程序：

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

这将启动机器人以及一个自托管的 SearXNG 搜索引擎。使用 `docker compose logs -f bot` 查看日志。

注意：自动自我更新器需要 systemd 服务，因此在 Docker 中更新是手动的：执行 `git pull`，然后再次运行 `docker compose up -d --build`。

## 功能详解

### /admin 面板

在私聊中发送 `/admin`（仅限老板 — 其他人无法打开，且不会出现在 `/help` 或菜单中）。它包含：

- 🔑 **Tokens 与模型** — 添加或移除 LLM 密钥，查看哪些密钥正常，选择当前模型，浏览提供商的实时模型列表
- 👥 **用户** — 用户数量、封禁 / 解封、允许名单
- 📊 **统计** — 使用数据
- 💬 **近期对话** — 用户对机器人说的内容（仅限老板，私密）
- 🖼️ **图像模型** — 您自己的图片服务（基础 URL + API 密钥 + 模型），或关闭
- 🛡️ **管理员** — 让受信任的人访问面板的部分功能
- 🟢/🔴 **开关** — 为所有人开启或关闭机器人（老板始终保持控制权）
- 🌍 **语言与国家** — 随时更改机器人的语言或国家

### 密钥池

机器人可同时保存多个 LLM 提供商的密钥。它会在正常的密钥间轮换，当某个密钥失效时自动故障转移。在 `/admin` 中，你可以固定某个模型、手动选择模型，或让机器人自由轮换。任何提供 OpenAI 兼容 API 的服务商都适用 — 包括小型聚合商，不仅限于大厂。

### 图像

图像生成使用您自己的 OpenAI 兼容图片服务：在 `/admin`（🖼️ 图像模型）中添加其基础 URL、API 密钥和模型。没有内置的图片提供商，也不支持照片编辑。可以从 `/admin` 关闭图像生成。

### 国家与语言

Vortex 支持 **195 个国家** 和 **40 种语言**。国家决定时区、价格显示的货币、祈祷时间使用的城市以及本地化内容。语言仅决定机器人说什么 — 例如，比利时的群组可以使用国家「比利时」但语言选英语。两者稍后都可在 `/admin` 中修改。

### 更新

机器人每天检查一次 `VortexLabsHQ/vortex-telegram-bot` 的 GitHub 发布版本。有新版本时，会私聊发送带有 ✅ / ❌ 按钮的消息给老板。确认后会更新代码并重启机器人。仓库为私有时，检查会静默无操作（GitHub API 需公开仓库）— 如永不想检查，请设置 `UPDATE_CHECK_ENABLED=0`。

## 故障排查 / 常见问题

**安装程序提示我的令牌无效。**
令牌来自 [@BotFather](https://t.me/BotFather)。请确保复制了完整的令牌（数字、一个冒号，然后是 35 个以上字符），没有多余空格。如果你删除了机器人或生成了新令牌，旧令牌将失效 —— 请粘贴新令牌。

**机器人在群组中不回复。**
需检查四项：(1) 群组隐私必须关闭 — 在 [@BotFather](https://t.me/BotFather) 发送 `/setprivacy`，选择你的机器人，并选择 **Disable**；若隐私开启，机器人完全无法看到群组消息，(2) 机器人必须已添加到群组，(3) 必须说出唤醒词 — 即它的名字，例如 `Vortex what's the time?` — 机器人仅在群组中听到其名字时才会响应，(4) 在私聊中完全不需要唤醒词。

**机器人用英语回复，而不是我的语言。**
发送 `/admin`（仅限管理员）→ 语言与国家，选择你的语言。安装程序也会询问语言 —— 在那里按回车键即可接受你所在国家的默认语言。

**我选择了 Anthropic，但机器人不聊天。**
Anthropic 的原生 API 与 OpenAI 不兼容，因此机器人无法直接使用它聊天。请使用 OpenRouter（它通过 OpenAI 兼容 API 提供 Claude 模型），或从列表中选择其他提供商。

**网页搜索不工作。**
网页搜索需要 SearXNG，安装程序会提议用 Docker 设置它。没有它时，机器人会退回到 Wikipedia，效果较弱。你也可以在 `.env` 中设置 `SEARCH_PROVIDER=tavily` 或 `serper` 并配合 `SEARCH_API_KEY`。

**日志在哪里？**
`journalctl -u vortex-bot -f` 显示实时日志。`systemctl status vortex-bot` 显示服务是否正在运行。如果机器人停止，`sudo systemctl restart vortex-bot` 可重新启动它。

**机器人提示我已达到每日限制。**
每位用户每天可获得 30 次机器人回复（管理员除外）。限制会在机器人所在国家时区的午夜重置。可在 `.env` 中通过 `DAILY_LIMIT_MESSAGES` 调高限制，或询问管理员。

**我发现了 bug / 我有个想法。**
请在 GitHub 上提交 issue —— 详见 [CONTRIBUTING.md](CONTRIBUTING.md) 了解如何报告和提交修复。

## 开发

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

运行测试（纯 Python 脚本，无需 pytest）：

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

所有九个测试套件必须通过后才能提交拉取请求。代码风格（ruff）和 PR 流程请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 许可证

Vortex 采用 [MIT License](LICENSE) 发布 —— 免费用于使用、复制、修改和分享，适用于任何目的。

<a id="countries"></a>

## 国家

安装程序询问您的国家时，请**按此处所示的英文原样**粘贴国家名称。该表格由 `bot/countries.py` 生成 — 如果此处的名称与该文件中的名称不一致，以 `bot/countries.py` 为准。

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

## 谢谢

> ⭐ **请在 GitHub 上给这个项目加星标并关注 [@VortexLabsHQ](https://github.com/VortexLabsHQ)** —— 这是支持 Vortex 并帮助他人发现它的最简单方式。谢谢！
