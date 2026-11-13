# Vortex 🤖 — ผู้ช่วยกลุ่ม Telegram ของคุณเอง

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · **ไทย** · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **ถ้าคุณชอบ Vortex โปรดให้ดาวโปรเจกต์นี้บน GitHub และติดตาม [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — จะช่วยให้คนอื่นพบเจอมากขึ้น ขอบคุณครับ!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Vortex คืออะไร?

Vortex เป็นบอท Telegram ที่อยู่ในกลุ่มและแชทส่วนตัวของคุณ ตอบสนองด้วยโมเดล AI คุณเรียกชื่อมัน (ชื่อเริ่มต้นคือ **Vortex**) มันจะตอบกลับ — สามารถพูดคุย ค้นหาเว็บ สร้างภาพ เช็คราคา เล่าตลก อ่านไฟล์ ถอดเสียง และอื่นๆ อีกมากมาย

มันรันบนเซิร์ฟเวอร์ของคุณเอง ในประเทศและภาษาของคุณเอง คุณคือผู้บังคับบัญชา: แผง `/admin` แบบซ่อนอยู่ ให้คุณจัดการคีย์ AI ผู้ใช้ และการตั้งค่า

## คุณสมบัติ

- 💬 **แชท AI** ในกลุ่ม (คำปลุก) และแชทส่วนตัว (ไม่ต้องใช้คำปลุก)
- 🔑 **Token pool** — ใช้ผู้ให้บริการ LLM และคีย์หลายตัว สลับและสำรองอัตโนมัติ
- 🖼️ **สร้างและแก้ไขภาพ** — ฟรี (DuckAI) หรือผู้ให้บริการแบบจ่ายเงิน
- 🔍 **ค้นหาเว็บ** — SearXNG โฮสต์เอง พร้อมสำรอง Wikipedia
- 💰 **ราคาเรียลไทม์** — สกุลเงิน ทอง น้ำมัน และคริปโต ในสกุลเงินท้องถิ่นของคุณ
- 🕌 **เวลาปฏิบัติธรรม**, 🃏 **ดูดวง**, 😄 **ตลก**, 🎲 **ทอยลูกเต๋าและทอยเหรียญ**
- 📎 **วิเคราะห์ไฟล์** และ **ถอดเสียง**
- 📥 **ดาวน์โหลด** — ส่งลิงก์ รับไฟล์สื่อกลับมา (สูงสุด 45 MB)
- 🌍 **195 ประเทศ** และ **40 ภาษา** — ประเทศและภาษาเป็นการตั้งค่าแยกกัน
- 🔄 **อัปเดตเอง** — ตรวจสอบรุ่นใหม่ทุกวัน และถามก่อนอัปเดต
- 🛡️ **แผง /admin แบบซ่อน** — โทเคน ผู้ใช้ สถิติ แชท โมเดลภาพ ผู้จัดการ อำนาจ

## ก่อนการติดตั้ง

คุณต้องการเซิร์ฟเวอร์ (หรือคอมพิวเตอร์ที่เปิดตลอดเวลา) ที่รัน **Linux** และติดตั้งสิ่งต่อไปนี้:

| สิ่งที่ต้องการ | วิธีตรวจสอบ | สิ่งที่ควรเห็น |
| --- | --- | --- |
| **Python 3.11 หรือใหม่กว่า** | `python3 --version` | `Python 3.11.x` หรือสูงกว่า (3.12 และ 3.13 ใช้ได้) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` หรือ `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` หรือคล้ายกัน |
| **Docker** *(ตัวเลือก)* | `docker --version` | `Docker version 2x.x.x` — จำเป็นต่อเมื่อคุณต้องการค้นหาเว็บด้วย SearXNG ที่เป็นตัวเลือก |

ถ้าขาดอะไร โปรแกรมติดตั้งจะเสนอติดตั้งให้ด้วย `apt` (บน Debian/Ubuntu) ระบบอื่นติดตั้งด้วยตัวจัดการแพ็กเกจของคุณก่อน

คุณยังต้องการสองสิ่งจาก Telegram (ทั้งคู่ฟรี):

1. **โทเคนบอท** — คุยกับ [@BotFather](https://t.me/BotFather) บน Telegram ส่ง `/newbot` และคัดลอกโทเคนที่มันให้
2. **รหัสผู้ใช้ Telegram แบบตัวเลขของคุณ** — คุยกับ [@userinfobot](https://t.me/userinfobot) และคัดลอกตัวเลขที่มันแสดง นี่คือรหัส "ผู้บังคับบัญชา" ของคุณ: บัญชีนี้เท่านั้นที่ใช้ `/admin` ได้

## การติดตั้ง

คำสั่งเดียว คัดลอกไป วางในเทอร์มินัล แล้วกด Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

โปรแกรมติดตั้งจะถามคุณหกคำถาม ตามลำดับ:

1. **ประเทศ** — วางชื่อประเทศภาษาอังกฤษ **ตรงตามที่แสดงใน [ตารางประเทศ](#countries) ด้านล่าง** (เช่น `Turkey`) ประเทศจะกำหนดเขตเวลา สกุลเงินท้องถิ่นสำหรับราคา เวลาปฏิบัติธรรม และเนื้อหาท้องถิ่น
2. **ภาษา** — ภาษาที่บอทใช้พูด (เช่น `en`, `fa`, `tr`) กด Enter เพื่อยอมรับค่าเริ่มต้นของประเทศของคุณ ภาษาแยกจากประเทศ: มันเปลี่ยนแค่สิ่งที่บอทพูด และคุณสามารถเปลี่ยนได้ภายหลังจาก `/admin`
3. **โทเคนบอท** — วางโทเคนจาก [@BotFather](https://t.me/BotFather) ตัวติดตั้งจะตรวจสอบแบบเรียลไทม์กับ Telegram
4. **รหัสตัวเลขบอส** — Telegram user ID ของคุณจาก [@userinfobot](https://t.me/userinfobot)
5. **ชื่อบอท / คำปลุก** — ชื่อที่คนเรียกในกลุ่มเพื่อคุยกับบอท ภาษาไหนก็ได้ (เช่น `Vortex` หรือ `ورتکس`) กด Enter สำหรับค่าเริ่มต้น `Vortex`
6. **ผู้ให้บริการ LLM แรก** — เลือกหนึ่ง: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, หรือ **Custom** (วาง base URL) จากนั้นวาง API key สำหรับผู้ให้บริการนั้น — ตัวติดตั้งจะดึงรายการโมเดลแบบเรียลไทม์จากผู้ให้บริการและคุณเลือกโมเดล

จากนั้นตัวติดตั้งจะติดตั้ง dependencies เขียนไฟล์ `.env` สร้างบริการ systemd `vortex-bot` เสนอให้ติดตั้ง SearXNG สำหรับค้นหาเว็บ (ต้องการ Docker) และเริ่มบอท

> ⚠️ **Anthropic ใช้งานโดยตรงไม่ได้** API ต้นทางของ Anthropic ไม่รองรับ OpenAI-compatible และบอทนี้รองรับเฉพาะ OpenAI-compatible APIs เท่านั้น หากคุณเลือก Anthropic ตัวติดตั้งจะเตือน: key จะทำงานได้เฉพาะผ่าน OpenAI-compatible gateway ให้ใช้ OpenRouter หรือผู้ให้บริการอื่นในรายการแทน

## หลังติดตั้ง

ตรวจสอบว่าบอทกำลังทำงาน:

```bash
systemctl status vortex-bot
```

ควรเห็น `active (running)` หากต้องการดู log แบบเรียลไทม์:

```bash
journalctl -u vortex-bot -f
```

ตอนนี้เปิด Telegram และคุยกับบอทของคุณ:

- ส่ง `/start` — บอทจะทักทาย
- ใน **แชทส่วนตัว** แค่พิมพ์เข้าไป — ไม่ต้องใช้คำปลุก
- ใน **กลุ่ม** เพิ่มบอทเข้าไปในกลุ่ม แล้วพูดชื่อมัน เช่น: `Vortex what's the time?`
- ในฐานะบอส ส่ง `/admin` ในแชทส่วนตัวเพื่อเปิดแผงแอดมินซ่อน

**อัปเดตอัตโนมัติ** ทุกวันบอทจะเช็ค GitHub หา release ใหม่ หากมี จะส่งข้อความส่วนตัวมาพร้อมปุ่ม ✅ / ❌ กด ✅ และมันจะอัปเดตเองและรีสตาร์ท — คุณไม่ต้องแตะเซิร์ฟเวอร์เลย

## การตั้งค่า

การตั้งค่าทั้งหมดอยู่ในไฟล์ `.env` ในโฟลเดอร์ติดตั้ง ดู [`.env.example`](.env.example) สำหรับทุกตัวเลือก ตัวสำคัญที่สุด:

| Setting | What it does |
| --- | --- |
| `BOT_TOKEN` | โทเค็นบอท Telegram ของคุณ (จาก @BotFather) |
| `BOSS_ID` | รหัสผู้ใช้ Telegram แบบตัวเลขของคุณ (เจ้าของบอท) |
| `BOT_NAME` | ชื่อบอทและคำปลุกในกลุ่ม (ค่าเริ่มต้น `Vortex`) |
| `BOT_COUNTRY` | ชื่อประเทศภาษาอังกฤษ เช่น `United States` (ตั้งค่าเขตเวลา สกุลเงิน เวลาปฏิบัติธรรม) |
| `BOT_LANGUAGE` | รหัสภาษาบอท เช่น `en`, `fa`, `tr` (เปลี่ยนเฉพาะข้อความที่บอทพูด) |
| `LLM_PROVIDERS` | ผู้ให้บริการ LLM และคีย์: `base_url\|api_key\|model` คั่นด้วยเครื่องหมายจุลภาค |
| `UPDATE_CHECK_ENABLED` | `1` = ตรวจสอบอัปเดตรายวัน, `0` = ไม่ตรวจสอบเลย |
| `UPDATE_REPO` | รีโพที่ดูรุ่นปล่อย (ค่าเริ่มต้น `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | ค้นหาบนเว็บ: `searxng` (ค่าเริ่มต้น), `tavily`, หรือ `serper` |
| `DAILY_LIMIT_MESSAGES` | จำนวนตอบกลับสูงสุดต่อผู้ใช้ต่อวัน (ค่าเริ่มต้น `30`, เจ้าของบอทไม่ถูกจำกัด) |

ประเทศและภาษาสามารถเปลี่ยนได้ภายหลังจากแผง `/admin` ที่ซ่อนอยู่ (Language & Country) โดยไม่ต้องแก้ไขไฟล์ใดๆ

## ทางเลือก Docker

หากคุณชอบ Docker มากกว่าตัวติดตั้ง:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

คำสั่งนี้จะเริ่มบอทพร้อมกับเครื่องมือค้นหา SearXNG ที่โฮสต์เอง ดูล็อกได้ด้วย `docker compose logs -f bot`

หมายเหตุ: ตัวอัปเดตอัตโนมัติต้องการบริการ systemd ดังนั้นใน Docker การอัปเดตต้องทำด้วยตนเอง: `git pull` แล้ว `docker compose up -d --build` อีกครั้ง

## รายละเอียดฟีเจอร์

### แผง /admin

ส่ง `/admin` ในแชทส่วนตัว (เฉพาะเจ้าของบอท — ไม่มีใครเปิดได้ และไม่ปรากฏใน `/help` หรือเมนู) มีฟีเจอร์ดังนี้:

- 🔑 **Tokens & model** — เพิ่มหรือลบคีย์ LLM, ดูว่าคีย์ไหนใช้งานได้, เลือกโมเดลที่ใช้งานอยู่, เรียกดูรายการโมเดลแบบเรียลไทม์ของผู้ให้บริการ
- 👥 **Users** — จำนวนผู้ใช้, บล็อก/ปลดบล็อก, รายชื่อที่อนุญาต
- 📊 **Stats** — ตัวเลขการใช้งาน
- 💬 **Recent chats** — ผู้คนพูดกับบอทอะไรบ้าง (เฉพาะเจ้าของบอท, แชทส่วนตัว)
- 🖼️ **Image model** — DuckAI (ฟรี, ค่าเริ่มต้น), HiLinkUp, บริการภาพแบบกำหนดเอง, หรือปิด
- 🛡️ **Managers** — ให้คนที่ไว้วางใจเข้าถึงบางส่วนของแผง
- 🟢/🔴 **Power** — เปิด/ปิดบอทให้ทุกคน (เจ้าของบอทยังคงควบคุมได้)
- 🌍 **Language & Country** — เปลี่ยนภาษาหรือประเทศของบอทได้ตลอดเวลา

### สระคีย์ (Token Pool)

บอทสามารถเก็บคีย์จากผู้ให้บริการ LLM หลายแห่งพร้อมกันได้ มันจะสลับใช้คีย์ที่ยังทำงานอยู่และフェイルออเวอร์อัตโนมัติเมื่อคีย์ไหนหยุดทำงาน จาก `/admin` คุณสามารถปักหมุดโมเดลหนึ่งตัว, เลือกโมเดลด้วยตนเอง, หรือปล่อยให้บอทสลับใช้งานอิสระ ผู้ให้บริการที่มี API เข้ากันได้กับ OpenAI ทำงานได้หมด — รวมถึงตัวรวมเล็กๆ ไม่ใช่แค่ชื่อดังอย่างเดียว

### ภาพ

การสร้างภาพมี 3 โหมด: **DuckAI** (ฟรี, ไม่ต้องคีย์, ค่าเริ่มต้น), **HiLinkUp** (เสียเงิน, คุณภาพดีกว่า), หรือบริการภาพ **แบบกำหนดเอง** ที่เข้ากันได้กับ OpenAI ของคุณเอง คุณยังส่งรูปให้บอทและบอกวิธีแก้ไขได้ ("ทำให้เป็นสไตล์การ์ตูน") และมันจะสร้างภาพใหม่มาให้ การสร้างภาพสามารถปิดได้จาก `/admin`

### ประเทศและภาษา

Vortex รองรับ **195 ประเทศ** และ **40 ภาษา** ประเทศจะกำหนดเขตเวลา สกุลเงินที่แสดงราคา เมืองที่ใช้สำหรับเวลาปฏิบัติธรรม และเนื้อหาท้องถิ่น ภาษาจะกำหนดเฉพาะข้อความที่บอทพูด — เช่น กลุ่มในเบลเยียมสามารถใช้ประเทศเบลเยียมและภาษาอังกฤษได้ สองอย่างนี้สามารถเปลี่ยนได้ภายหลังจาก `/admin`

### การอัปเดต

บอทจะตรวจสอบ GitHub releases ของ `VortexLabsHQ/vortex-telegram-bot` วันละครั้ง เมื่อมีเวอร์ชันใหม่ จะส่งข้อความแจ้งเจ้าของบอทแบบส่วนตัวพร้อมปุ่ม ✅ / ❌ การกดยอมรับจะอัปเดตโค้ดและรีสตาร์ทบอท ขณะที่ repo เป็น private การตรวจสอบจะไม่ทำอะไรเลย (GitHub API ต้องการ public repo) — ตั้งค่า `UPDATE_CHECK_ENABLED=0` หากไม่ต้องการตรวจสอบเลย

## การแก้ไขปัญหา / คำถามที่พบบ่อย

**โปรแกรมติดตั้งบอกว่าโทเค็นของฉันไม่ถูกต้อง**
โทเค็นมาจาก [@BotFather](https://t.me/BotFather) ตรวจสอบว่าได้คัดลอกโทเค็นทั้งหมด (ตัวเลข จุลภาค แล้วตามด้วย 35+ ตัวอักษร) โดยไม่มีช่องว่างเพิ่มเติม หากลบบอทหรือสร้างโทเค็นใหม่ โทเก็นเก่าจะหยุดทำงาน — ให้วางโทเค็นใหม่แทน

**บอทไม่ตอบในกลุ่มของฉัน**
มี 3 สิ่งที่ต้องตรวจสอบ: (1) บอทต้องถูกเพิ่มเข้าไปในกลุ่ม (2) คุณต้องพูดคำปลุกของมัน — ชื่อของมัน เช่น `Vortex what's the time?` — บอทจะฟังเฉพาะเมื่อมีการเรียกชื่อในกลุ่ม (3) ในแชทส่วนตัว ไม่ต้องใช้คำปลุกเลย

**บอทตอบเป็นภาษาอังกฤษ ไม่ใช่ภาษาของฉัน**
ส่ง `/admin` (เฉพาะเจ้าของ) → Language & Country แล้วเลือกภาษาของคุณ โปรแกรมติดตั้งก็จะถามภาษาเช่นกัน — กด Enter ที่นั่นเพื่อยอมรับค่าเริ่มต้นของประเทศคุณ

**ฉันเลือก Anthropic แต่บอทไม่แชท**
API ต้นฉบับของ Anthropic ไม่เข้ากันได้กับ OpenAI จึงทำให้บอทแชทด้วยมันโดยตรงไม่ได้ ให้ใช้ OpenRouter (ซึ่งสามารถให้บริการโมเดล Claude ผ่าน API ที่เข้ากันได้กับ OpenAI) หรือเลือกผู้ให้บริการอื่นจากรายการ

**การค้นหาบนเว็บไม่ทำงาน**
การค้นหาบนเว็บต้องการ SearXNG ซึ่งโปรแกรมติดตั้งเสนอให้ตั้งค่าด้วย Docker หากไม่มี บอทจะใช้ Wikipedia แทน ซึ่งอ่อนกว่า คุณยังสามารถตั้งค่า `SEARCH_PROVIDER=tavily` หรือ `serper` พร้อม `SEARCH_API_KEY` ใน `.env` ได้

**ล็อกอยู่ที่ไหน?**
`journalctl -u vortex-bot -f` แสดงล็อกแบบเรียลไทม์ `systemctl status vortex-bot` แสดงว่าบริการกำลังทำงานอยู่หรือไม่ หากบอทหยุดทำงาน `sudo systemctl restart vortex-bot` จะเริ่มต้นใหม่

**บอทบอกว่าฉันถึงขีดจำกัดรายวันแล้ว**
แต่ละผู้ใช้ได้รับการตอบกลับจากบอท 30 ครั้งต่อวัน (เจ้าของบอทไม่ถูกจำกัด) ขีดจำกัดจะรีเซ็ตตอนเที่ยงคืนตามเขตเวลาประเทศของบอท เพิ่มได้ด้วย `DAILY_LIMIT_MESSAGES` ใน `.env` หรือขอเจ้าของบอท

**ฉันพบบั๊ก / มีไอเดีย**
กรุณาเปิด issue บน GitHub — ดู [CONTRIBUTING.md](CONTRIBUTING.md) สำหรับวิธีรายงานและวิธีส่งการแก้ไข

## การพัฒนา

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

รันการทดสอบ (สคริปต์ Python ธรรมดา ไม่ต้องใช้ pytest):

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

ชุดทดสอบทั้งเก้าต้องผ่านก่อนที่คุณจะเปิด pull request ดู [CONTRIBUTING.md](CONTRIBUTING.md) สำหรับสไตล์โค้ด (ruff) และกระบวนการ PR

## ใบอนุญาต

Vortex เผยแพร่ภายใต้ [MIT License](LICENSE) — ใช้ คัดลอก แก้ไข และแชร์ได้อย่างอิสระ สำหรับทุกวัตถุประสงค์

<a id="countries"></a>

## ประเทศ

วางชื่อประเทศ **เป็นภาษาอังกฤษ ตรงตามที่เขียนไว้ที่นี่** เมื่อโปรแกรมติดตั้งถามถึงประเทศของคุณ ตารางนี้สร้างจาก `bot/countries.py` — หากชื่อที่นี่และชื่อที่นั่นไม่ตรงกัน ให้ใช้ `bot/countries.py` เป็นหลัก

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

## ขอบคุณ

> ⭐ **โปรดกดดาวโปรเจกต์นี้บน GitHub และติดตาม [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — นี่คือวิธีที่ง่ายที่สุดในการสนับสนุน Vortex และช่วยให้ผู้อื่นพบเจอได้ ขอบคุณ!
