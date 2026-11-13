# Vortex 🤖 — Seu próprio assistente de grupo do Telegram

[English](README.md) · [فارسی](README.fa.md) · [Türkçe](README.tr.md) · [Deutsch](README.de.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Nederlands](README.nl.md) · [Русский](README.ru.md) · [Українська](README.uk.md) · [Polski](README.pl.md) · [Svenska](README.sv.md) · **Português** · [العربية](README.ar.md) · [हिन्दी](README.hi.md) · [اردو](README.ur.md) · [中文](README.zh.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Bahasa Indonesia](README.id.md) · [ไทย](README.th.md) · [Tiếng Việt](README.vi.md) · [Bahasa Melayu](README.ms.md) · [বাংলা](README.bn.md) · [ਪੰਜਾਬੀ](README.pa.md) · [मराठी](README.mr.md) · [తెలుగు](README.te.md) · [தமிழ்](README.ta.md) · [ગુજરાતી](README.gu.md) · [አማርኛ](README.am.md) · [Kiswahili](README.sw.md) · [Hausa](README.ha.md) · [Filipino](README.fil.md) · [Română](README.ro.md) · [Magyar](README.hu.md) · [Čeština](README.cs.md) · [Ελληνικά](README.el.md) · [עברית](README.he.md) · [Dansk](README.da.md) · [Norsk](README.no.md)

> ⭐ **Se você gosta do Vortex, por favor dê uma estrela neste projeto no GitHub e siga [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — isso ajuda mais pessoas a encontrá-lo. Obrigado!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## O que é o Vortex?

O Vortex é um bot do Telegram que vive nos seus grupos e chats privados e responde às pessoas com um modelo de chat de IA. Você diz o nome dele (o nome padrão é **Vortex**) e ele responde — pode conversar, pesquisar na web, criar imagens, verificar preços, contar piadas, ler arquivos, transcrever mensagens de voz e muito mais.

Ele roda no seu próprio servidor, no seu próprio país e idioma. Você é o chefe: um painel `/admin` oculto permite gerenciar chaves de IA, usuários e configurações.

## Recursos

- 💬 **Chat com IA** em grupos (palavra de ativação) e chats privados (sem precisar de palavra de ativação)
- 🔑 **Pool de tokens** — use vários provedores e chaves de LLM, alterne e faça failover automaticamente
- 🖼️ **Geração e edição de imagens** — grátis (DuckAI) ou provedores pagos
- 🔍 **Busca na web** — SearXNG auto-hospedado, com fallback para Wikipedia
- 💰 **Preços em tempo real** — moedas, ouro, petróleo e cripto na sua moeda local
- 🕌 **Horários de oração**, 🃏 **previsões**, 😄 **piadas**, 🎲 **dados e cara ou coroa**
- 📎 **Análise de arquivos** e **transcrição de voz**
- 📥 **Downloads** — envie um link, receba o arquivo de mídia de volta (até 45 MB)
- 🌍 **195 países** e **40 idiomas** — país e idioma são configurações separadas
- 🔄 **Autoatualização** — verifica novas versões diariamente e pergunta antes de atualizar
- 🛡️ **Painel /admin oculto** — tokens, usuários, estatísticas, chats, modelo de imagem, gerentes, energia

## Antes de instalar

Você precisa de um servidor (ou um computador que fique ligado) rodando **Linux** com estes instalados:

| O que | Como verificar | O que você deve ver |
| --- | --- | --- |
| **Python 3.11 ou mais novo** | `python3 --version` | `Python 3.11.x` ou superior (3.12 e 3.13 também funcionam) |
| **git** | `git --version` | `git version 2.x.x` |
| **curl** | `curl --version` | `curl 7.x.x` ou `8.x.x` |
| **systemd** | `systemctl --version` | `systemd 24x` ou similar |
| **Docker** *(opcional)* | `docker --version` | `Docker version 2x.x.x` — só necessário se quiser a busca web opcional do SearXNG |

Se algo estiver faltando, instale tudo com um único comando (Debian/Ubuntu):

```bash
sudo apt update && sudo apt install -y python3 python3-venv python3-pip git curl
```

Para o Docker opcional (necessário apenas se você quiser a busca na web do SearXNG):

```bash
sudo apt install -y docker.io
sudo systemctl enable --now docker
sudo usermod -aG docker $USER
```

Após a última linha, saia e entre novamente (ou execute comandos `docker` com `sudo`). O instalador também oferece instalar as ferramentas ausentes para você com `apt` no Debian/Ubuntu. Em outros sistemas, instale-as primeiro com seu gerenciador de pacotes. O `systemd` vem com o sistema — não pode ser instalado separadamente.

Você também precisa de duas coisas do Telegram (ambas são grátis):

1. **Um token de bot** — converse com [@BotFather](https://t.me/BotFather) no Telegram, envie `/newbot` e copie o token que ele der.
2. **Seu ID numérico de usuário do Telegram** — converse com [@userinfobot](https://t.me/userinfobot) e copie o número que ele mostrar. Este é seu ID de "chefe": apenas esta conta pode usar `/admin`.

## Instalação

Um comando. Copie, cole no seu terminal e pressione Enter:

```bash
curl -sSL https://raw.githubusercontent.com/VortexLabsHQ/vortex-telegram-bot/main/install.sh | bash
```

O instalador faz seis perguntas, nesta ordem:

1. **País** — cole o nome do seu país em inglês **exatamente como listado na [tabela de países](#countries) abaixo** (por exemplo `Turkey`). O país define o fuso horário, a moeda local para preços, horários de oração e conteúdo local.
2. **Idioma** — o idioma que o bot fala (por exemplo `en`, `fa`, `tr`). Pressione Enter para aceitar o padrão do seu país. O idioma é separado do país: só muda o que o bot diz, e você pode alterar depois em `/admin`.
3. **Token do bot** — cole o token do [@BotFather](https://t.me/BotFather). O instalador verifica na hora com o Telegram.
4. **ID numérico do chefe** — seu ID de usuário do Telegram do [@userinfobot](https://t.me/userinfobot).
5. **Nome do bot / palavra de ativação** — o nome que as pessoas dizem em grupos para falar com o bot. Qualquer idioma serve (por exemplo `Vortex` ou `ورتکس`). Pressione Enter para o padrão `Vortex`.
6. **Primeiro provedor de LLM** — escolha um: OpenAI, Anthropic, OpenRouter, Google AI (Gemini), DeepSeek, Groq, Together AI, Mistral AI, xAI (Grok), Cohere ou **Personalizado** (cole uma URL base). Depois cole sua chave de API desse provedor — o instalador busca a lista de modelos ativa do provedor e você escolhe um.

Depois o instalador instala as dependências, cria o arquivo `.env`, cria o serviço systemd `vortex-bot`, oferece instalar o SearXNG para busca na web (precisa do Docker) e inicia o bot.

> ⚠️ **O Anthropic não funciona diretamente.** A API nativa do Anthropic não é compatível com OpenAI, e este bot só fala APIs compatíveis com OpenAI. Se você escolher Anthropic, o instalador avisa: a chave só funciona através de um gateway compatível com OpenAI. Use o OpenRouter ou outro provedor da lista.

## Após a instalação

Verifique se o bot está rodando:

```bash
systemctl status vortex-bot
```

Você deve ver `active (running)`. Para acompanhar o log em tempo real:

```bash
journalctl -u vortex-bot -f
```

Agora abra o Telegram e converse com seu bot:

- Envie `/start` — o bot diz olá.
- Em um **chat privado**, apenas escreva para ele — nenhuma palavra de ativação necessária.
- Em um **grupo**, adicione o bot ao grupo, depois desative a Privacidade do grupo: no [@BotFather](https://t.me/BotFather) envie `/setprivacy`, escolha seu bot e selecione **Disable** — caso contrário, o bot não verá as mensagens do grupo e não ouvirá sua palavra de ativação. Em seguida, diga o nome dele, por exemplo: `Vortex what's the time?`
- Como chefe, envie `/admin` em um chat privado para abrir o painel de admin oculto.

**Atualizações são automáticas.** Uma vez por dia o bot verifica no GitHub se há uma nova versão. Se houver, ele envia uma mensagem privada com botões ✅ / ❌. Toque em ✅ e ele se atualiza e reinicia sozinho — você nunca precisa mexer no servidor.

## Configuração

Todas as configurações ficam no arquivo `.env` no diretório de instalação. Veja [`.env.example`](.env.example) para todas as opções. As mais importantes:

| Configuração | O que faz |
| --- | --- |
| `BOT_TOKEN` | Seu token do bot do Telegram (do @BotFather) |
| `BOSS_ID` | Seu ID numérico de usuário do Telegram (o dono do bot) |
| `BOT_NAME` | O nome do bot e palavra de ativação em grupos (padrão `Vortex`) |
| `BOT_COUNTRY` | País em inglês, ex.: `United States` (define fuso horário, moeda, horários de oração) |
| `BOT_LANGUAGE` | Código de idioma do bot, ex.: `en`, `fa`, `tr` (só muda o que o bot fala) |
| `LLM_PROVIDERS` | Provedores e chaves de LLM: `base_url\|api_key\|model`, separados por vírgula |
| `UPDATE_CHECK_ENABLED` | `1` = verificar atualizações diariamente, `0` = nunca verificar |
| `UPDATE_REPO` | O repositório cujos lançamentos são monitorados (padrão `VortexLabsHQ/vortex-telegram-bot`) |
| `SEARCH_PROVIDER` | Busca na web: `searxng` (padrão), `tavily` ou `serper` |
| `DAILY_LIMIT_MESSAGES` | Máx. de respostas do bot por usuário por dia (padrão `30`, o dono é isento) |

O país e o idioma também podem ser alterados depois no painel oculto `/admin` (Idioma e País), sem editar nenhum arquivo.

## Alternativa com Docker

Se você prefere Docker em vez do instalador:

```bash
cp .env.example .env   # fill in BOT_TOKEN, BOSS_ID, and your LLM key(s)
docker compose up -d --build
```

Isso inicia o bot junto com um mecanismo de busca SearXNG auto-hospedado. Verifique os logs com `docker compose logs -f bot`.

Nota: o atualizador automático precisa do serviço systemd, então no Docker as atualizações são manuais: `git pull` e depois `docker compose up -d --build` novamente.

## Recursos em detalhes

### O painel /admin

Envie `/admin` em um chat privado (apenas o chefe — ninguém mais pode abri-lo, e ele nunca aparece em `/help` ou nos menus). Ele tem:

- 🔑 **Tokens & modelo** — adicione ou remova chaves de LLM, veja quais chaves estão saudáveis, escolha o modelo ativo, navegue pela lista de modelos ao vivo de um provedor
- 👥 **Usuários** — contagem de usuários, banir / desbanir, lista de permitidos
- 📊 **Estatísticas** — números de uso
- 💬 **Chats recentes** — o que as pessoas disseram ao bot (apenas o chefe, privado)
- 🖼️ **Modelo de imagem** — DuckAI (grátis, padrão), HiLinkUp, um serviço de imagem personalizado, ou desligado
- 🛡️ **Gerentes** — dê a pessoas de confiança acesso a partes do painel
- 🟢/🔴 **Energia** — ligue ou desligue o bot para todos (o chefe continua no controle)
- 🌍 **Idioma & País** — mude o idioma ou o país do bot a qualquer momento

### O pool de tokens

O bot pode guardar chaves de vários provedores de LLM ao mesmo tempo. Ele alterna entre chaves saudáveis e faz failover automático quando uma para de funcionar. Pelo `/admin` você pode fixar um modelo, escolher um modelo manualmente ou deixar o bot alternar livremente. Qualquer provedor com API compatível com OpenAI funciona — incluindo pequenos agregadores, não apenas os grandes nomes.

### Imagens

A geração de imagens tem três modos: **DuckAI** (grátis, sem chave, padrão), **HiLinkUp** (pago, melhor qualidade) ou um serviço de imagem **personalizado** compatível com OpenAI. Você também pode enviar uma foto ao bot e dizer como editá-la ("faça isso estilo cartoon"), e ele gerará uma nova imagem. A geração de imagens pode ser desligada pelo `/admin`.

### Países e idiomas

O Vortex suporta **195 países** e **40 idiomas**. O país define o fuso horário, a moeda em que os preços são mostrados, a cidade usada para horários de oração e o conteúdo local. O idioma só define o que o bot diz — um grupo na Bélgica pode usar o país Bélgica e o idioma Inglês, por exemplo. Ambos podem ser alterados depois pelo `/admin`.

### Atualizações

O bot verifica os releases do GitHub de `VortexLabsHQ/vortex-telegram-bot` uma vez por dia. Quando há uma nova versão, ele manda uma mensagem privada ao chefe com botões ✅ / ❌. Aceitar atualiza o código e reinicia o bot. Enquanto o repositório for privado, a verificação não faz nada silenciosamente (a API do GitHub precisa de um repositório público) — defina `UPDATE_CHECK_ENABLED=0` se nunca quiser a verificação.

## Solução de Problemas / FAQ

**O instalador diz que meu token é inválido.**
O token vem do [@BotFather](https://t.me/BotFather). Certifique-se de copiar o token completo (dígitos, dois pontos, depois 35+ caracteres), sem espaços extras. Se você apagou o bot ou criou um novo token, o antigo para de funcionar — cole o novo.

**O bot não responde no meu grupo.**
Quatro pontos a verificar: (1) A Privacidade do grupo deve estar desativada — no [@BotFather](https://t.me/BotFather) envie `/setprivacy`, escolha seu bot e selecione **Disable**; com a privacidade ativada, o bot não vê nenhuma mensagem do grupo, (2) o bot deve ser adicionado ao grupo, (3) você deve dizer a palavra de ativação dele — seu nome, por exemplo `Vortex what's the time?` — o bot só escuta quando seu nome é dito em grupos, (4) em um chat privado nenhuma palavra de ativação é necessária.

**O bot responde em inglês, não no meu idioma.**
Envie `/admin` (só o chefe) → Idioma e País, e escolha seu idioma. O instalador também pergunta o idioma — aperte Enter lá para aceitar o padrão do seu país.

**Escolhi Anthropic e o bot não conversa.**
A API nativa da Anthropic não é compatível com OpenAI, então o bot não consegue conversar com ela diretamente. Use o OpenRouter (que serve modelos Claude via API compatível com OpenAI), ou escolha outro provedor da lista.

**A busca na web não funciona.**
A busca na web precisa do SearXNG, que o instalador oferece configurar com Docker. Sem ele, o bot usa a Wikipédia como alternativa, que é mais limitada. Você também pode definir `SEARCH_PROVIDER=tavily` ou `serper` com uma `SEARCH_API_KEY` no `.env`.

**Onde estão os logs?**
`journalctl -u vortex-bot -f` mostra o log em tempo real. `systemctl status vortex-bot` mostra se o serviço está rodando. Se o bot parar, `sudo systemctl restart vortex-bot` reinicia ele.

**O bot diz que atingi o limite diário.**
Cada usuário tem 30 respostas do bot por dia (o chefe é isento). O limite reseta à meia-noite no fuso horário do país do bot. Aumente com `DAILY_LIMIT_MESSAGES` no `.env`, ou peça ao chefe.

**Encontrei um bug / Tenho uma ideia.**
Abra uma issue no GitHub — veja [CONTRIBUTING.md](CONTRIBUTING.md) para como reportar e como enviar uma correção.

## Desenvolvimento

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

Execute os testes (scripts Python simples, sem pytest necessário):

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

Todos os nove conjuntos devem passar antes de você abrir um pull request. Consulte [CONTRIBUTING.md](CONTRIBUTING.md) para o estilo de código (ruff) e o processo de PR.

## Licença

O Vortex é lançado sob a [Licença MIT](LICENSE) — livre para usar, copiar, modificar e compartilhar, para qualquer finalidade.

<a id="countries"></a>

## Países

Cole o nome do país **em inglês, exatamente como escrito aqui** quando o instalador pedir o seu país. A tabela é gerada a partir de `bot/countries.py` — se um nome aqui e um nome lá discordarem, `bot/countries.py` prevalece.

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

## Obrigado

> ⭐ **Por favor, dê uma estrela a este projeto no GitHub e siga [@VortexLabsHQ](https://github.com/VortexLabsHQ)** — é a forma mais simples de apoiar o Vortex e ajudar outros a encontrá-lo. Obrigado!
