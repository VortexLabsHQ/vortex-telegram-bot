# Vortex 🤖 — Trợ lý nhóm Telegram của riêng bạn

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · **Tiếng Việt** · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Nếu bạn thích Vortex, hãy star dự án này trên GitHub và theo dõi [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — điều đó giúp nhiều người tìm thấy nó hơn. Cảm ơn bạn!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex là gì?

Vortex là một bot Telegram sống trong các nhóm và trò chuyện riêng tư của bạn và trả lời mọi người bằng một mô hình chat AI. Bạn nói tên của nó (tên mặc định là **Vortex**) và nó sẽ phản hồi — nó có thể trò chuyện, tìm kiếm web, tạo hình ảnh, kiểm tra giá, kể chuyện cười, đọc file, chuyển văn bản tin nhắn thoại, và nhiều hơn nữa.

Nó chạy trên máy chủ của riêng bạn, ở quốc gia và ngôn ngữ của riêng bạn. Bạn là người chủ: một bảng điều khiển `/admin` ẩn cho phép bạn quản lý khóa AI, người dùng và cài đặt.

## Tính năng

- 💬 **Trò chuyện AI** trong nhóm (từ khóa đánh thức) và trò chuyện riêng (không cần từ khóa đánh thức)
- 🔑 **Nhóm token** — sử dụng nhiều nhà cung cấp và khóa LLM, xoay vòng và chuyển đổi tự động
- 🖼️ **Tạo và chỉnh sửa hình ảnh** — miễn phí (DuckAI) hoặc các nhà cung cấp trả phí
- 🔍 **Tìm kiếm web** — SearXNG tự lưu trữ, có dự phòng Wikipedia
- 💰 **Giá trực tiếp** — tiền tệ, vàng, dầu và crypto bằng tiền tệ địa phương của bạn
- 🕌 **Giờ cầu nguyện**, 🃏 **xem bói**, 😄 **truyện cười**, 🎲 **tung xúc xắc và lật đồng xu**
- 📎 **Phân tích file** và **chuyển văn bản giọng nói**
- 📥 **Tải xuống** — gửi liên kết, nhận lại file phương tiện (tối đa 45 MB)
- 🌍 **195 quốc gia** và **40 ngôn ngữ** — quốc gia và ngôn ngữ là cài đặt riêng biệt
- 🔄 **Tự cập nhật** — kiểm tra bản phát hành mới hàng ngày và hỏi bạn trước khi cập nhật
- 🛡️ **Bảng điều khiển /admin ẩn** — token, người dùng, thống kê, trò chuyện, mô hình hình ảnh, quản lý, quyền lực

## Trước khi cài đặt

Bạn cần một máy chủ (hoặc một máy tính luôn bật) chạy **Linux** với các phần mềm sau đã cài đặt:

| Nội dung | Cách kiểm tra | Kết quả mong đợi |
| --- | --- | --- |
| **Python 3.11 hoặc mới hơn** | `python3 --version` | `Python 3.11.x` hoặc cao hơn (3.12 và 3.13 cũng hoạt động) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` hoặc `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` hoặc tương tự |
| **Docker** *(tùy chọn)* | `docker --version` | `Docker version 2x.x.x` — chỉ cần nếu bạn muốn tìm kiếm web SearXNG tùy chọn |

Nếu thiếu thứ gì, trình cài đặt sẽ đề nghị cài đặt nó cho bạn bằng `apt` (trên Debian/Ubuntu). Trên các hệ thống khác, hãy cài đặt nó bằng trình quản lý gói của bạn trước.

Bạn cũng cần hai thứ từ Telegram (cả hai đều miễn phí):

1. **Token bot** — trò chuyện với [@BotFather](https://t.me/BotFather) trên Telegram, gửi `/newbot`, và sao chép token mà nó cung cấp.
2. **ID người dùng Telegram dạng số của bạn** — trò chuyện với [@userinfobot](https://t.me/userinfobot) và sao chép số mà nó hiển thị. Đây là ID "chủ" của bạn: chỉ tài khoản này mới có thể dùng `/admin`.

## Cài đặt

Một lệnh duy nhất. Sao chép nó, dán vào terminal của bạn, và nhấn Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

Trình cài đặt sẽ hỏi bạn sáu câu hỏi, theo thứ tự:

1. **Quốc gia** — dán tên tiếng Anh của quốc gia bạn **chính xác như trong [bảng quốc gia](#countries) bên dưới** (ví dụ `Turkey`). Quốc gia xác định múi giờ, đơn vị tiền tệ địa phương cho giá cả, giờ cầu nguyện và nội dung địa phương.
2. **Ngôn ngữ** — ngôn ngữ bot sử dụng để nói chuyện (ví dụ `en`, `fa`, `tr`). Nhấn Enter để chấp nhận mặc định cho quốc gia của bạn. Ngôn ngữ tách biệt với quốc gia: nó chỉ thay đổi những gì bot nói, và bạn có thể đổi sau từ `/admin`.
3. **Token bot** — dán token từ [@BotFather](https://t.me/BotFather). Trình cài đặt kiểm tra trực tiếp với Telegram.
4. **ID số Boss** — ID người dùng Telegram của bạn từ [@userinfobot](https://t.me/userinfobot).
5. **Tên bot / từ khóa đánh thức** — tên mọi người nói trong nhóm để nói chuyện với bot. Bất kỳ ngôn ngữ nào cũng được (ví dụ `Vortex` hoặc `ورتکس`). Nhấn Enter cho mặc định `Vortex`.
6. **Nhà cung cấp LLM đầu tiên** — chọn một: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, hoặc **Tùy chỉnh** (dán URL cơ sở). Sau đó dán khóa API cho nhà cung cấp đó — trình cài đặt lấy danh sách mô hình trực tiếp từ nhà cung cấp và bạn chọn một mô hình.

Sau đó trình cài đặt cài các phụ thuộc, ghi file `.env`, tạo dịch vụ systemd `vortex-bot`, đề nghị cài SearXNG cho tìm kiếm web (cần Docker), và khởi động bot.

> ⚠️ **Anthropic không hoạt động trực tiếp.** API gốc của Anthropic không tương thích OpenAI, và bot này chỉ nói API tương thích OpenAI. Nếu bạn chọn Anthropic, trình cài đặt cảnh báo: khóa chỉ hoạt động qua cổng tương thích OpenAI. Hãy dùng OpenRouter, hoặc nhà cung cấp khác từ danh sách.

## Sau khi cài đặt

Kiểm tra bot đang chạy:

```bash
systemctl status vortex-bot
```

Bạn nên thấy `active (running)`. Để xem log trực tiếp:

```bash
journalctl -u vortex-bot -f
```

Bây giờ mở Telegram và nói chuyện với bot của bạn:

- Gửi `/start` — bot chào hỏi.
- Trong **chat riêng**, chỉ cần viết cho nó — không cần từ khóa đánh thức.
- Trong **nhóm**, thêm bot vào nhóm, rồi nói tên nó, ví dụ: `Vortex mấy giờ rồi?`
- Là Boss, gửi `/admin` trong chat riêng để mở bảng điều khiển ẩn.

**Cập nhật tự động.** Mỗi ngày bot kiểm tra GitHub xem có bản phát hành mới không. Nếu có, nó gửi tin nhắn riêng cho bạn với nút ✅ / ❌. Bấm ✅ và nó tự cập nhật và khởi động lại — bạn không bao giờ cần chạm vào server.

## Cấu hình

Tất cả cài đặt nằm trong file `.env` trong thư mục cài đặt. Xem [`.env.example`](.env.example) cho mọi tùy chọn. Những cái quan trọng nhất:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | Token bot Telegram của bạn (từ @BotFather) |
| `BOSS_ID` | ID người dùng Telegram dạng số của bạn (chủ bot) |
| `BOT_NAME` | Tên bot và từ khóa đánh thức trong nhóm (mặc định `Vortex`) |
| `BOT_COUNTRY` | Quốc gia bằng tiếng Anh, ví dụ `United States` (thiết lập múi giờ, tiền tệ, giờ cầu nguyện) |
| `BOT_LANGUAGE` | Mã ngôn ngữ bot, ví dụ `en`, `fa`, `tr` (chỉ thay đổi nội dung bot nói) |
| `LLM_PROVIDERS` | Nhà cung cấp LLM và khóa: `base_url\|api_key\|model`, cách nhau bằng dấu phẩy |
| `UPDATE_CHECK_ENABLED` | `1` = kiểm tra cập nhật hàng ngày, `0` = không bao giờ kiểm tra |
| `UPDATE_REPO` | Repo được theo dõi bản phát hành (mặc định `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Tìm kiếm web: `searxng` (mặc định), `tavily`, hoặc `serper` |
| `DAILY_LIMIT_MESSAGES` | Số lần bot trả lời tối đa mỗi người mỗi ngày (mặc định `30`, boss được miễn trừ) |

Quốc gia và ngôn ngữ cũng có thể thay đổi sau từ bảng `/admin` ẩn (Ngôn ngữ & Quốc gia), không cần chỉnh sửa file nào.

## Docker alternative

Nếu bạn thích Docker hơn bộ cài đặt:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Lệnh này khởi động bot cùng với công cụ tìm kiếm SearXNG tự lưu trữ. Xem log bằng `docker compose logs -f bot`.

Lưu ý: trình cập nhật tự động cần dịch vụ systemd, nên trong Docker cập nhật là thủ công: `git pull` rồi `docker compose up -d --build` lại.

## Features in detail

### The /admin panel

Gửi `/admin` trong chat riêng (chỉ boss — không ai khác mở được, và nó không xuất hiện trong `/help` hay menu). Nó có:

- 🔑 **Tokens & model** — thêm hoặc xoá khóa LLM, xem khóa nào khỏe, chọn model đang hoạt động, duyệt danh sách model trực tiếp của nhà cung cấp
- 👥 **Users** — thống kê người dùng, ban / unban, danh sách cho phép
- 📊 **Stats** — con số sử dụng
- 💬 **Recent chats** — mọi người nói gì với bot (chỉ boss, riêng tư)
- 🖼️ **Image model** — DuckAI (miễn phí, mặc định), HiLinkUp, dịch vụ ảnh tùy chỉnh, hoặc tắt
- 🛡️ **Managers** — cấp quyền truy cập một phần bảng điều khiển cho người tin cậy
- 🟢/🔴 **Power** — bật hoặc tắt bot cho mọi người (boss vẫn giữ điều khiển)
- 🌍 **Language & Country** — đổi ngôn ngữ hoặc quốc gia của bot bất cứ lúc nào

### The token pool

Bot có thể giữ khóa từ nhiều nhà cung cấp LLM cùng lúc. Nó xoay vòng giữa các khóa khỏe và tự động chuyển dự phòng khi một khóa ngừng hoạt động. Từ `/admin` bạn có thể ghim một model, chọn model thủ công, hoặc để bot xoay tự do. Bất kỳ nhà cung cấp nào có API tương thích OpenAI đều hoạt động — kể cả các bộ gom nhỏ, không chỉ các tên lớn.

### Images

Tạo ảnh có ba chế độ: **DuckAI** (miễn phí, không cần khóa, mặc định), **HiLinkUp** (trả phí, chất lượng tốt hơn), hoặc dịch vụ ảnh **tùy chỉnh** tương thích OpenAI của riêng bạn. Bạn cũng có thể gửi ảnh cho bot và nói cách chỉnh sửa ("biến này thành phong cách hoạt hình"), và nó sẽ tạo ảnh mới. Tạo ảnh có thể tắt từ `/admin`.

### Countries and languages

Vortex hỗ trợ **195 quốc gia** và **40 ngôn ngữ**. Quốc gia xác định múi giờ, đơn vị tiền tệ hiển thị giá, thành phố dùng cho giờ cầu nguyện và nội dung địa phương. Ngôn ngữ chỉ quyết định bot nói gì — ví dụ nhóm ở Belgium có thể dùng quốc gia Belgium và ngôn ngữ English. Cả hai đều có thể thay đổi sau từ `/admin`.

### Cập nhật

Bot kiểm tra bản phát hành GitHub của `VortexLabsHQ/vortex-telegram-bot` một lần mỗi ngày. Khi có phiên bản mới, bot nhắn tin riêng cho boss với nút ✅ / ❌. Chấp nhận sẽ cập nhật mã và khởi động lại bot. Khi repo còn riêng tư, kiểm tra lặng lẽ không làm gì (API GitHub cần repo công khai) — đặt `UPDATE_CHECK_ENABLED=0` nếu bạn không bao giờ muốn kiểm tra.

## Khắc phục sự cố / Câu hỏi thường gặp

**Cài đặt báo token của tôi không hợp lệ.**
Token lấy từ [@BotFather](https://t.me/BotFather). Hãy chắc chắn bạn sao chép toàn bộ token (số, dấu hai chấm, rồi 35+ ký tự), không có khoảng trắng thừa. Nếu bạn xóa bot hoặc tạo token mới, token cũ ngừng hoạt động — dán token mới vào.

**Bot không trả lời trong nhóm của tôi.**
Ba điều cần kiểm tra: (1) bot phải được thêm vào nhóm, (2) bạn phải nói từ khóa đánh thức — tên của nó, ví dụ `Vortex what's the time?` — bot chỉ lắng nghe khi tên nó được nói trong nhóm, (3) trong trò chuyện riêng không cần từ khóa đánh thức.

**Bot trả lời bằng English, không phải ngôn ngữ của tôi.**
Gửi `/admin` (chỉ boss) → Language & Country, và chọn ngôn ngữ của bạn. Cài đặt cũng hỏi ngôn ngữ — nhấn Enter đó để chấp nhận mặc định của quốc gia bạn.

**Tôi chọn Anthropic mà bot không trò chuyện.**
API gốc của Anthropic không tương thích OpenAI, nên bot không thể trò chuyện trực tiếp với nó. Dùng OpenRouter (có thể phục vụ mô hình Claude qua API tương thích OpenAI), hoặc chọn nhà cung cấp khác từ danh sách.

**Tìm kiếm web không hoạt động.**
Tìm kiếm web cần SearXNG, mà cài đặt đề xuất thiết lập bằng Docker. Nếu không có, bot sẽ dùng Wikipedia dự phòng, yếu hơn. Bạn cũng có thể đặt `SEARCH_PROVIDER=tavily` hoặc `serper` kèm `SEARCH_API_KEY` trong `.env`.

**Log ở đâu?**
`journalctl -u vortex-bot -f` hiển thị log trực tiếp. `systemctl status vortex-bot` cho biết dịch vụ có đang chạy không. Nếu bot dừng, `sudo systemctl restart vortex-bot` khởi động lại nó.

**Bot báo tôi đã đạt giới hạn hàng ngày.**
Mỗi người được 30 phản hồi bot mỗi ngày (boss được miễn). Giới hạn đặt lại lúc nửa đêm theo múi giờ quốc gia của bot. Tăng nó bằng `DAILY_LIMIT_MESSAGES` trong `.env`, hoặc nhờ boss.

**Tôi tìm thấy lỗi / có ý tưởng.**
Vui lòng mở issue trên GitHub — xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết cách báo cáo và gửi sửa lỗi.

## Phát triển

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

Chạy thử nghiệm (script Python thuần túy, không cần pytest):

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

Cả chín bộ thử nghiệm phải pass trước khi bạn mở pull request. Xem [CONTRIBUTING.md](CONTRIBUTING.md) cho phong cách mã (ruff) và quy trình PR.

## Giấy phép

Vortex được phát hành dưới [MIT License](LICENSE) — tự do sử dụng, sao chép, thay đổi và chia sẻ, cho mọi mục đích.

<a id="countries"></a>

## Quốc gia

Dán tên quốc gia **bằng tiếng Anh, chính xác như viết ở đây** khi trình cài đặt yêu cầu quốc gia của bạn. Bảng được tạo từ `bot/countries.py` — nếu tên ở đây và tên ở đó có khác biệt, `bot/countries.py` sẽ được ưu tiên.

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

## Cảm ơn

> ⭐ **Vui lòng cấp sao cho dự án này trên GitHub và theo dõi [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — đây là cách đơn giản nhất để ủng hộ Vortex và giúp người khác tìm thấy nó. Cảm ơn!
