# Vortex 🤖 — あなた専用のTelegramグループアシスタント

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · **日本語** · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Vortexが気に入ったら、GitHubでこのプロジェクトにスターをつけて、[@VortexLabsHQ](https://github.com/VortexLabsHQ)をフォローしてください** — そうすると、より多くの人に見つけてもらえます。ありがとうございます！

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortexとは？

Vortexは、あなたのグループやプライベートチャットに住み、AIチャットモデルで人々に答えるTelegramボットです。その名前（デフォルト名は**Vortex**）を呼ぶと返信します — チャットしたり、ウェブ検索したり、画像を作ったり、価格をチェックしたり、冗談を言ったり、ファイルを読んだり、ボイスメッセージを文字起こししたり、その他いろいろできます。

あなたのサーバーで、あなたの国と言語で動きます。あなたがボスです：隠された `/admin` パネルでAIキー、ユーザー、設定を管理できます。

## 機能

- 💬 **AIチャット** をグループで（ウェイクワード付き）とプライベートチャットで（ウェイクワード不要）
- 🔑 **トークンプール** — 複数のLLMプロバイダーとキーを使用し、自動でローテーションとフェイルオーバー
- 🖼️ **画像生成と編集** — 無料（DuckAI）または有料プロバイダー
- 🔍 **Web検索** — セルフホスト型SearXNG、Wikipediaへのフォールバック付き
- 💰 **リアルタイム価格** — 通貨、金、原油、暗号資産をあなたの現地通貨で表示
- 🕌 **礼拝時間**、🃏 **おみくじ**、😄 **ジョーク**、🎲 **ダイスとコインフリップ**
- 📎 **ファイル解析** と **音声文字起こし**
- 📥 **ダウンロード** — リンクを送信するとメディアファイルを取得（最大45 MB）
- 🌍 **195カ国** と **40言語** — 国と言語は別々の設定
- 🔄 **自動更新** — 毎日新しいリリースをチェックし、更新前に確認
- 🛡️ **非表示の /admin パネル** — トークン、ユーザー、統計、チャット、画像モデル、管理者、電源

## インストール前に

常時稼働する **Linux** サーバー (または PC) を用意し、以下がインストール済みであることを確認してください:

| 項目 | 確認コマンド | 期待される出力 |
| --- | --- | --- |
| **Python 3.11 以上** | `python3 --version` | `Python 3.11.x` 以上 (3.12、3.13 も OK) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` または `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` など |
| **Docker** *(オプション)* | `docker --version` | `Docker version 2x.x.x` — オプションの SearXNG ウェブ検索を使う場合のみ必要 |

何かが足りない場合、インストーラーが `apt` を使って自動インストールを提案します (Debian/Ubuntu の場合)。それ以外のシステムでは、事前にパッケージマネージャーでインストールしてください。

また、Telegram から以下の 2 つ (どちらも無料) が必要です:

1. **ボットトークン** — Telegram で [@BotFather](https://t.me/BotFather) に話しかけ、`/newbot` を送信し、表示されるトークンをコピーしてください。
2. **あなたの数値 Telegram ユーザー ID** — Telegram で [@userinfobot](https://t.me/userinfobot) に話しかけ、表示される数字をコピーしてください。これがあなたの「ボス」ID です: このアカウントだけが `/admin` を使えます。

## インストール

コマンドは1つだけ。コピーしてターミナルに貼り付け、Enterキーを押してください：

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

インストーラーが順に6つの質問をします：

1. **国** — 下の[国テーブル](#countries)に記載されている通り、あなたの国の英語名を**そのまま**貼り付けてください（例：`Turkey`）。国によってタイムゾーン、価格表示用の現地通貨、礼拝時間、ローカルコンテンツが決まります。
2. **言語** — ボットが話す言語（例：`en`、`fa`、`tr`）。Enterキーを押すと、あなたの国のデフォルト言語が採用されます。言語は国とは別設定です：ボットの発言内容だけが変わり、後から `/admin` で変更できます。
3. **ボットトークン** — [@BotFather](https://t.me/BotFather) から取得したトークンを貼り付けてください。インストーラーがTelegramと通信して即座に検証します。
4. **ボスの数値ID** — [@userinfobot](https://t.me/userinfobot) で確認できるあなたのTelegramユーザーID。
5. **ボット名 / 呼び出しワード** — グループでボットに話しかけるときに使う名前。どの言語でもOKです（例：`Vortex` や `ورتکس`）。Enterキーを押すとデフォルトの `Vortex` になります。
6. **最初のLLMプロバイダー** — 以下から1つ選択：OpenAI、Anthropic、OpenRouter、Google AI (Gemini)、DeepSeek、Groq、Together AI、Mistral AI、xAI (Grok)、Cohere、または **Custom**（ベースURLを貼り付け）。続いてそのプロバイダーのAPIキーを貼り付けると、インストーラーが最新のモデル一覧を取得し、モデルを選べます。

その後、インストーラーが依存関係をインストールし、`.env` ファイルを作成し、`vortex-bot` という systemd サービスを登録し、ウェブ検索用の SearXNG のインストールを提案します（Dockerが必要）、最後にボットを起動します。

> ⚠️ **Anthropicは直接利用できません。** AnthropicのネイティブAPIはOpenAI互換ではなく、このボットはOpenAI互換APIのみに対応しています。Anthropicを選ぶとインストーラーが警告を出します：そのキーはOpenAI互換のゲートウェイ経由でしか使えません。代わりにOpenRouterやリスト内の他のプロバイダーを使ってください。

## インストール後

ボットが実行中か確認してください：

```bash
systemctl status vortex-bot
```

`active (running)` と表示されるはずです。ライブログを見るには：

```bash
journalctl -u vortex-bot -f
```

それでは Telegram を開いてボットに話しかけてみましょう：

- `/start` を送信 — ボットが挨拶します。
- **プライベートチャット**では、そのままメッセージを送るだけ — ウェイクワードは不要です。
- **グループ**では、ボットをグループに追加してから名前で呼びかけます。例: `Vortex what's the time?`
- 管理者として、プライベートチャットで `/admin` を送信すると隠し管理パネルが開きます。

**アップデートは自動です。** 1日1回、ボットが GitHub で新しいリリースをチェックします。利用可能な場合、✅ / ❌ ボタン付きのプライベートメッセージが届きます。✅ をタップすると自動で更新・再起動します — サーバーを触る必要は一切ありません。

## 設定

すべての設定は、インストールディレクトリ内の `.env` ファイルにあります。すべてのオプションについては [`.env.example`](.env.example) を参照してください。特に重要なもの:

| 設定 | 役割 |
| --- | --- |
| `BOT_TOKEN` | あなたの Telegram ボットトークン (@BotFather から取得) |
| `BOSS_ID` | あなたの数値の Telegram ユーザー ID (ボットの所有者) |
| `BOT_NAME` | グループでのボットの名前と呼び出しワード (デフォルト `Vortex`) |
| `BOT_COUNTRY` | 国名を英語で指定、例: `United States` (タイムゾーン、通貨、礼拝時間を設定) |
| `BOT_LANGUAGE` | ボットの言語コード、例: `en`, `fa`, `tr` (ボットの発言のみ変更されます) |
| `LLM_PROVIDERS` | LLM プロバイダーとキー: `base_url\|api_key\|model` をカンマ区切りで指定 |
| `UPDATE_CHECK_ENABLED` | `1` = 毎日更新を確認、`0` = 確認しない |
| `UPDATE_REPO` | リリースを監視するリポジトリ (デフォルト `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Web 検索: `searxng` (デフォルト), `tavily`, または `serper` |
| `DAILY_LIMIT_MESSAGES` | ユーザー1人あたりの1日の最大ボット返信数 (デフォルト `30`、ボスは除外) |

国と言語は、隠し `/admin` パネル (Language & Country) から後で変更することもでき、ファイルを編集する必要はありません。

## Dockerの代替案

インストーラーの代わりにDockerを使いたい場合:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

これにより、ボットがセルフホスト型のSearXNG検索エンジンと一緒に起動します。ログは `docker compose logs -f bot` で確認できます。

注: 自動セルフアップデーターにはsystemdサービスが必要なため、Dockerでは更新が手動になります: `git pull` を実行し、その後 `docker compose up -d --build` をもう一度実行してください。

## 詳細な機能

### /admin パネル

プライベートチャットで `/admin` を送信してください（ボスのみ — 他の誰も開けません。また `/help` やメニューにも表示されません）。以下の機能があります：

- 🔑 **トークンとモデル** — LLMキーの追加・削除、正常なキーの確認、アクティブなモデルの選択、プロバイダのライブモデル一覧の閲覧
- 👥 **ユーザー** — ユーザー数、ブロック / ブロック解除、許可リスト
- 📊 **統計** — 使用数
- 💬 **最近のチャット** — ユーザーがボットに送った内容（ボスのみ、プライベート）
- 🖼️ **画像モデル** — DuckAI（無料、デフォルト）、HiLinkUp、カスタム画像サービス、またはオフ
- 🛡️ **マネージャー** — 信頼できる人にパネルの一部へのアクセス権を付与
- 🟢/🔴 **電源** — 全員に対してボットをオン/オフ（ボスは常に操作可能）
- 🌍 **言語と国** — ボットの言語や国をいつでも変更

### トークンプール

ボットは複数のLLMプロバイダのキーを同時に保持できます。正常なキー間をローテーションし、キーが機能しなくなると自動的にフェイルオーバーします。`/admin` から特定のモデルを固定したり、手動でモデルを選んだり、ボットに自由にローテーションさせたりできます。OpenAI互換APIを持つプロバイダならどれでも動作します — 大手だけでなく、小規模なアグリゲータも含みます。

### 画像

画像生成には3つのモードがあります：**DuckAI**（無料、キー不要、デフォルト）、**HiLinkUp**（有料、高品質）、または独自の**カスタム** OpenAI互換画像サービス。ボットに写真を送って編集方法を指示することもできます（「これを漫画風にして」など）、すると新しい画像が生成されます。画像生成は `/admin` からオフにできます。

### 国と言語

Vortex は **195か国** と **40言語** に対応しています。国の設定により、タイムゾーン、価格表示の通貨、礼拝時間に使用する都市、ローカルコンテンツが決まります。言語はボットの発言内容のみを決めます — たとえばベルギーのグループで、国をベルギー、言語を英語にすることもできます。どちらも後から `/admin` で変更可能です。

### アップデート

ボットは `VortexLabsHQ/vortex-telegram-bot` の GitHub リリースを1日1回チェックします。新しいバージョンが出ると、ボスにプライベートで ✅ / ❌ ボタン付きのメッセージを送ります。承認するとコードが更新され、ボットが再起動します。リポジトリがプライベートの間は、チェックは静かに何もしません（GitHubのAPIは公開リポジトリを必要とします） — チェックを完全に無効にしたい場合は `UPDATE_CHECK_ENABLED=0` を設定してください。

## トラブルシューティング / よくある質問

**インストーラーがトークンが無効だと言っています。**
トークンは[@BotFather](https://t.me/BotFather)から取得します。トークン全体（数字、コロン、その後35文字以上）を余分なスペースなしでコピーしたか確認してください。ボットを削除したり新しいトークンを作成したりすると、古いトークンは動作しなくなります。新しいトークンを貼り付けてください。

**ボットがグループで応答しません。**
3つ確認してください：（1）ボットがグループに追加されていること、（2）ウェイクワード（ボットの名前）を呼ぶこと。例：`Vortex what's the time?` — グループでは名前を呼ばれたときだけ反応します、（3）プライベートチャットではウェイクワードは不要です。

**ボットが日本語ではなく英語で答えます。**
`/admin`を送信（ボスのみ）→ Language & Country で言語を選択してください。インストーラーでも言語を尋ねられます。そこでEnterを押すと、お住まいの国のデフォルト言語が採用されます。

**Anthropicを選んだのにボットが会話しません。**
AnthropicのネイティブAPIはOpenAI互換ではないため、ボットは直接会話できません。OpenRouterを使用してください（OpenAI互換API経由でClaudeモデルを利用できます）。またはリストから別のプロバイダーを選んでください。

**Web検索が動作しません。**
Web検索にはSearXNGが必要です。インストーラーでDocker経由でセットアップできます。これがないとボットはWikipediaにフォールバックしますが、機能は弱くなります。`.env`で`SEARCH_PROVIDER=tavily`または`serper`を`SEARCH_API_KEY`とともに設定することもできます。

**ログはどこにありますか？**
`journalctl -u vortex-bot -f`でライブログを表示します。`systemctl status vortex-bot`でサービスの実行状態を確認できます。ボットが停止した場合は、`sudo systemctl restart vortex-bot`で再起動できます。

**ボットが1日の上限に達したと表示します。**
各ユーザーは1日30回までボットの返信を受けられます（ボスは除外）。上限はボットの国のタイムゾーンで深夜0時にリセットされます。`.env`で`DAILY_LIMIT_MESSAGES`を増やすか、ボスに相談してください。

**バグを見つけました / アイデアがあります。**
GitHubでIssueを作成してください。報告方法と修正の送り方は[CONTRIBUTING.md](CONTRIBUTING.md)を参照してください。

## 開発

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

テストを実行します（プレーンな Python スクリプト、pytest は不要）:

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

すべての 9 つのスイートがパスしてからプルリクエストを開いてください。コードスタイル（ruff）と PR プロセスについては [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス

Vortexは[MITライセンス](LICENSE)の下で公開されています — あらゆる目的で、自由に使用、複製、変更、共有できます。

<a id="countries"></a>

## 国

インストーラーが国を尋ねたとき、**ここに書かれている通りに英語で** 国名を貼り付けてください。この表は `bot/countries.py` から生成されています — ここにある名前とあちらにある名前が食い違う場合は、 `bot/countries.py` が優先されます。

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

## ありがとうございます

> ⭐ **GitHubでこのプロジェクトにスターを付け、[@VortexLabsHQ](https://github.com/VortexLabsHQ)をフォローしてください** — これがVortexを支援し、他の人が見つけやすくする一番簡単な方法です。ありがとうございます！
