# Vortex 🤖 — Tu propio asistente de grupo de Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · **Español** · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · [Português](README.pt.md) · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Si te gusta Vortex, dale una estrella a este proyecto en GitHub y sigue a [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — ayuda a que más gente lo encuentre. ¡Gracias!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## ¿Qué es Vortex?

Vortex es un bot de Telegram que vive en tus grupos y chats privados y responde a la gente con un modelo de chat de IA. Dices su nombre (el nombre por defecto es **Vortex**) y te responde — puede chatear, buscar en la web, crear imágenes, consultar precios, contar chistes, leer archivos, transcribir mensajes de voz y más.

Se ejecuta en tu propio servidor, en tu propio país e idioma. Tú eres el jefe: un panel `/admin` oculto te permite gestionar claves de IA, usuarios y ajustes.

## Características

- 💬 **Chat con IA** en grupos (palabra de activación) y chats privados (no se necesita palabra de activación)
- 🔑 **Conjunto de tokens** — usa varios proveedores y claves de LLM, rota y cambia automáticamente si falla uno
- 🖼️ **Generación de imágenes** — con tu propio servicio de imagen (URL base + clave API + modelo), añadido en `/admin`
- 🔍 **Búsqueda web** — SearXNG autoalojado, con respaldo de Wikipedia
- 💰 **Precios en vivo** — divisas, oro, petróleo y cripto en tu moneda local
- 🕌 **Horarios de oración**, 🃏 **frases de la fortuna**, 😄 **chistes**, 🎲 **dados y cara o cruz**
- 📎 **Análisis de archivos** y **transcripción de voz**
- 📥 **Descargas** — envía un enlace, recibe el archivo multimedia de vuelta (hasta 45 MB)
- 🌍 **195 países** y **40 idiomas** — el país y el idioma son ajustes separados
- 🔄 **Autoactualización** — busca nuevas versiones cada día y te pregunta antes de actualizar
- 🛡️ **Panel /admin oculto** — tokens, usuarios, estadísticas, chats, modelo de imagen, gestores, encendido/apagado

## Antes de instalar

Necesitas un servidor (o un ordenador que se quede encendido) con **Linux** y estos programas instalados:

| Qué | Cómo comprobarlo | Qué deberías ver |
| --- | --- | --- |
| **Python 3.11 o superior** | `python3 --version` | `Python 3.11.x` o superior (3.12 y 3.13 también valen) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` o `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` o similar |
| **Docker** *(opcional)* | `docker --version` | `Docker version 2x.x.x` — solo necesario si quieres la búsqueda web opcional SearXNG |

Si falta algo, instálalo todo con un solo comando (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Para el Docker opcional (solo necesario si quieres la búsqueda web de SearXNG):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Después de la última línea, cierra sesión y vuelve a entrar (o ejecuta comandos `docker` con `sudo`). El instalador también te ofrece instalar las herramientas que falten con `apt` en Debian/Ubuntu. En otros sistemas, instálalas primero con tu gestor de paquetes. `systemd` viene con el sistema: no se puede instalar por separado.

También necesitas dos cosas de Telegram (las dos son gratis):

1. **Un token de bot** — habla con [@BotFather](https://t.me/BotFather) en Telegram, envía `/newbot` y copia el token que te dé.
2. **Tu ID numérico de usuario de Telegram** — habla con [@userinfobot](https://t.me/userinfobot) y copia el número que te muestre. Este es tu ID de "jefe": solo esta cuenta puede usar `/admin`.

## Instalación

Un solo comando. Cópialo, pégalo en tu terminal y pulsa Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

El instalador te hace seis preguntas, en orden:

1. **País** — pega el nombre en inglés de tu país **exactamente como aparece en la [tabla de países](#countries) de abajo** (por ejemplo `Turkey`). El país define la zona horaria, la moneda local para precios, horarios de oración y contenido local.
2. **Idioma** — el idioma que habla el bot (por ejemplo `en`, `fa`, `tr`). Pulsa Enter para aceptar el predeterminado de tu país. El idioma es independiente del país: solo cambia lo que dice el bot, y puedes cambiarlo luego desde `/admin`.
3. **Token del bot** — pega el token de [@BotFather](https://t.me/BotFather). El instalador lo comprueba en directo con Telegram.
4. **ID numérico del jefe** — tu ID de usuario de Telegram de [@userinfobot](https://t.me/userinfobot).
5. **Nombre del bot / palabra de activación** — el nombre que dice la gente en grupos para hablar con el bot. Cualquier idioma vale (por ejemplo `Vortex` o `ورتکس`). Pulsa Enter para el predeterminado `Vortex`.
6. **Primer proveedor LLM** — elige uno: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere, o **Personalizado** (pega una URL base). Luego pega tu clave API de ese proveedor — el instalador obtiene la lista de modelos en vivo del proveedor y eliges uno.

Luego el instalador instala las dependencias, escribe el archivo `.env`, crea el servicio systemd `vortex-bot`, ofrece instalar SearXNG para búsqueda web (necesita Docker) y arranca el bot.

> ⚠️ **Anthropic no funciona directamente.** La API nativa de Anthropic no es compatible con OpenAI, y este bot solo habla APIs compatibles con OpenAI. Si eliges Anthropic, el instalador te avisa: la clave solo funciona a través de una pasarela compatible con OpenAI. Usa OpenRouter, u otro proveedor de la lista, en su lugar.

## Después de instalar

Comprueba que el bot está corriendo:

```bash
systemctl status vortex-bot
```

Deberías ver `active (running)`. Para ver el registro en vivo:

```bash
journalctl -u vortex-bot -f
```

Ahora abre Telegram y habla con tu bot:

- Envía `/start` — el bot te saluda.
- En un **chat privado**, solo escríbele — no hace falta palabra de activación.
- En un **grupo**, añade el bot al grupo, luego desactiva la Privacidad de grupo: en [@BotFather](https://t.me/BotFather) envía `/setprivacy`, elige tu bot y selecciona **Disable** — de lo contrario el bot no verá los mensajes del grupo ni escuchará su palabra de activación. Luego di su nombre, por ejemplo: `Vortex what's the time?`
- Como jefe, envía `/admin` en un chat privado para abrir el panel de administración oculto.

**Las actualizaciones son automáticas.** Una vez al día el bot busca en GitHub una nueva versión. Si hay una, te envía un mensaje privado con botones ✅ / ❌. Pulsa ✅ y se actualiza solo y se reinicia — nunca tienes que tocar el servidor.

## Configuración

Todos los ajustes están en el archivo `.env` en el directorio de instalación. Mira [`.env.example`](.env.example) para ver todas las opciones. Las más importantes:

| Ajuste | Qué hace |
| --- | --- |
| `BOT_TOKEN` | Tu token de bot de Telegram (de @BotFather) |
| `BOSS_ID` | Tu ID numérico de usuario de Telegram (el dueño del bot) |
| `BOT_NAME` | El nombre y palabra de activación del bot en grupos (predeterminado `Vortex`) |
| `BOT_COUNTRY` | País en inglés, ej. `United States` (define zona horaria, moneda, horarios de oración) |
| `BOT_LANGUAGE` | Código de idioma del bot, ej. `en`, `fa`, `tr` (solo cambia lo que dice el bot) |
| `LLM_PROVIDERS` | Proveedores y claves LLM: `base_url\|api_key\|model`, separados por comas |
| `UPDATE_CHECK_ENABLED` | `1` = buscar actualizaciones cada día, `0` = nunca buscar |
| `UPDATE_REPO` | El repo cuyas releases se vigilan (predeterminado `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Búsqueda web: `searxng` (predeterminado), `tavily`, o `serper` |
| `DAILY_LIMIT_MESSAGES` | Máx. respuestas del bot por usuario al día (predeterminado `30`, el jefe está exento) |

El país y el idioma también se pueden cambiar luego desde el panel `/admin` oculto (Idioma y País), sin editar ningún archivo.

## Alternativa con Docker

Si prefieres Docker en vez del instalador:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Esto arranca el bot junto con un motor de búsqueda SearXNG autoalojado. Mira los logs con `docker compose logs -f bot`.

Nota: el autoactualizador automático necesita el servicio systemd, así que en Docker las actualizaciones son manuales: `git pull` y luego `docker compose up -d --build` de nuevo.

## Características en detalle

### El panel /admin

Envía `/admin` en un chat privado (solo el jefe — nadie más puede abrirlo, y nunca aparece en `/help` ni en los menús). Tiene:

- 🔑 **Tokens y modelo** — añade o quita claves LLM, ve qué claves están sanas, elige el modelo activo, explora la lista de modelos en vivo de un proveedor
- 👥 **Usuarios** — conteo de usuarios, banear / desbanear, lista de permitidos
- 📊 **Estadísticas** — números de uso
- 💬 **Chats recientes** — lo que la gente le dijo al bot (solo el jefe, privado)
- 🖼️ **Modelo de imagen** — tu propio servicio de imagen (URL base + clave API + modelo), o apagado
- 🛡️ **Gestores** — da a gente de confianza acceso a partes del panel
- 🟢/🔴 **Encendido** — enciende o apaga el bot para todos (el jefe sigue teniendo el control)
- 🌍 **Idioma y País** — cambia el idioma o el país del bot cuando quieras

### El conjunto de tokens

El bot puede guardar claves de varios proveedores LLM a la vez. Rota entre las claves sanas y cambia automáticamente cuando una deja de funcionar. Desde `/admin` puedes fijar un modelo, elegir uno a mano, o dejar que el bot rote libremente. Funciona cualquier proveedor con API compatible con OpenAI — incluyendo agregadores pequeños, no solo los grandes nombres.

### Imágenes

La generación de imágenes usa tu propio servicio de imagen compatible con OpenAI: añade su URL base, clave API y modelo en `/admin` (🖼️ Modelo de imagen). No hay proveedor de imágenes integrado, y la edición de fotos no es compatible. La generación de imágenes se puede desactivar desde `/admin`.

### Países e idiomas

Vortex soporta **195 países** y **40 idiomas**. El país define la zona horaria, la moneda en que se muestran los precios, la ciudad usada para horarios de oración y el contenido local. El idioma solo define lo que dice el bot — por ejemplo, un grupo en Bélgica puede usar el país Bélgica y el idioma inglés. Los dos se pueden cambiar luego desde `/admin`.

### Actualizaciones

El bot revisa las releases de GitHub de `VortexLabsHQ/vortex-telegram-bot` una vez al día. Cuando sale una versión nueva, le manda un mensaje privado al jefe con botones ✅ / ❌. Aceptar actualiza el código y reinicia el bot. Mientras el repo sea privado, la comprobación no hace nada en silencio (la API de GitHub necesita un repo público) — pon `UPDATE_CHECK_ENABLED=0` si nunca quieres la comprobación.

## Solución de problemas / Preguntas frecuentes

**El instalador dice que mi token no es válido.**

El token viene de [@BotFather](https://t.me/BotFather). Asegúrate de copiar el token entero (dígitos, dos puntos, luego 35+ caracteres), sin espacios extra. Si borraste el bot o creaste un token nuevo, el viejo deja de funcionar — pega el nuevo.

**El bot no responde en mi grupo.**

Cuatro cosas a verificar: (1) La Privacidad de grupo debe estar desactivada — en [@BotFather](https://t.me/BotFather) envía `/setprivacy`, elige tu bot y selecciona **Disable**; con la privacidad activada, el bot no verá ningún mensaje de grupo, (2) el bot debe haber sido añadido al grupo, (3) debes decir su palabra de activación — su nombre, por ejemplo `Vortex what's the time?` — el bot solo escucha cuando se menciona su nombre en grupos, (4) en un chat privado no se necesita ninguna palabra de activación.

**El bot responde en inglés, no en mi idioma.**

Envía `/admin` (solo el jefe) → Idioma y País, y elige tu idioma. El instalador también pregunta el idioma — pulsa Enter ahí para aceptar el predeterminado de tu país.

**Elegí Anthropic y el bot no chatea.**

La API nativa de Anthropic no es compatible con OpenAI, así que el bot no puede chatear con ella directamente. Usa OpenRouter (que puede servir modelos Claude a través de una API compatible con OpenAI), o elige otro proveedor de la lista.

**La búsqueda web no funciona.**

La búsqueda web necesita SearXNG, que el instalador ofrece configurar con Docker. Sin él, el bot recurre a Wikipedia, que es más floja. También puedes poner `SEARCH_PROVIDER=tavily` o `serper` con una `SEARCH_API_KEY` en `.env`.

**¿Dónde están los logs?**

`journalctl -u vortex-bot -f` muestra el log en vivo. `systemctl status vortex-bot` muestra si el servicio está corriendo. Si el bot se para, `sudo systemctl restart vortex-bot` lo vuelve a arrancar.

**El bot dice que alcancé el límite diario.**

Cada usuario tiene 30 respuestas del bot al día (el jefe está exento). El límite se reinicia a medianoche en la zona horaria del país del bot. Súbelo con `DAILY_LIMIT_MESSAGES` en `.env`, o pídeselo al jefe.

**Encontré un bug / Tengo una idea.**

Por favor abre un issue en GitHub — mira [CONTRIBUTING.md](CONTRIBUTING.md) para cómo reportarlo y cómo enviar una corrección.

## Desarrollo

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

Ejecuta las pruebas (scripts de Python simples, no hace falta pytest):

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

Las nueve suites deben pasar antes de abrir un pull request. Mira [CONTRIBUTING.md](CONTRIBUTING.md) para el estilo de código (ruff) y el proceso de PR.

## Licencia

Vortex se publica bajo la [Licencia MIT](LICENSE) — libre de usar, copiar, modificar y compartir, para cualquier propósito.

<a id="countries"></a>

## Países

Pega el nombre del país **en inglés, exactamente como está escrito aquí** cuando el instalador te pida tu país. La tabla se genera desde `bot/countries.py` — si un nombre aquí y otro allá no coinciden, gana `bot/countries.py`.

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

## Gracias

> ⭐ **Por favor dale una estrella a este proyecto en GitHub y sigue a [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — es la forma más sencilla de apoyar a Vortex y ayudar a que otros lo encuentren. ¡Gracias!
