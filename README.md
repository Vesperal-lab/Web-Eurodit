# Web Eurodit

> **A simple HTTP reconnaissance tool written in Python.**

Web Eurodit is a lightweight web reconnaissance tool designed to collect basic information from a target web server.

The project is focused on learning how HTTP requests and responses work while building a practical reconnaissance tool from scratch.

The name **Eurodit** comes from the idea of an old man reading a newspaper — the idea of a deep read from a Eurodit monge

---

## Features

* Target URL validation
* HTTP/HTTPS connection testing
* HTTP status code detection
* Custom User-Agent support
* Server header detection
* Content-Type detection
* X-Powered-By detection
* Basic HTTP error handling
* Connection timeout handling
* Randomized newspaper-style messages
* Custom CLI interface

---

## How It Works

Web Eurodit starts by asking the user for a target URL.

```text
[+] Usage: Enter the target url
```

The URL is then validated to make sure it uses either `http://` or `https://`.

After validation, Eurodit sends an HTTP request to the target server and checks whether the server is reachable with a generic User-Agent to pass by the sites that don't accept connection with others terminals.

```text
[*] the server are working...
[+] Status code: 200
```

The user can then choose whether to use a custom **User-Agent**.

```text
[?] do you wanna use a User Agent? [y or N]
```

If a custom User-Agent is selected, the user can provide their own value or continue with the default one.

Eurodit then analyzes the HTTP response and extracts information from the returned headers.

For example:

```text
SERVER: nginx
CONTENT TYPE: text/html
X-POWERED BY: PHP
```

The collected information is then displayed in the final report.

---

## Request Flow

```text
                ┌───────────────┐
                │  Target URL   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ URL Validation│
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ HTTP Request  │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ Status Code   │
                └───────┬───────┘
                        │
                        ▼
                ┌───────────────┐
                │ HTTP Headers  │
                └───────┬───────┘
                        │
             ┌──────────┼──────────┐
             ▼          ▼          ▼
          Server    Content-Type  X-Powered-By
             │          │          │
             └──────────┼──────────┘
                        ▼
                ┌───────────────┐
                │ Final Report  │
                └───────────────┘
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Vesperal-lab/Web-Eurodit.git
```

No external Python dependencies are required.

Web Eurodit currently uses Python's standard library.

---

## Usage

Run the program with:

```bash
python3 Eurodit.py
```

Enter the target URL when prompted:

```text
[+] Usage: Enter the target url
https://example.com
```

> **Only scan systems you own or have explicit permission to test.**

---

## Requirements

* Python 3.10+
* Internet connection
* No external dependencies

---

## Roadmap

### v1.0 — Initial Release

* [x] URL validation
* [x] HTTP/HTTPS connection testing
* [x] Status code detection
* [x] User-Agent support
* [x] Server detection
* [x] Content-Type detection
* [x] X-Powered-By detection
* [x] Basic error handling
* [x] CLI interface
* [x] Randomized messages

## Future

* [ ] Full HTTP header enumeration
* [ ] Security header detection
* [ ] Redirect detection
* [ ] Improved HTTP request handling

- [ ] Technology detection
- [ ] `robots.txt` detection
- [ ] `sitemap.xml` detection
- [ ] Basic endpoint discovery
- [ ] More detailed server information

* [ ] Improved response analysis 
* [ ] Better timeout handling
* [ ] Configurable request options
* [ ] Improved CLI output
* [ ] Verbose mode

- [ ] Directory enumeration
- [ ] Web crawler
- [ ] WAF detection
- [ ] Vulnerability checks
- [ ] JSON output
- [ ] Report generation

---

## Project Structure

```text
Web-Eurodit/
│
├── eurodit.py
└── README.md
```

The project is intentionally kept simple during the early versions. As the scanner grows, the codebase will gradually be separated into modules.

---

## Version

**Current version: 1.0**

Web Eurodit is currently an early-stage project focused on HTTP reconnaissance and learning.

---

## Disclaimer

Web Eurodit was created for **educational purposes and authorized security testing**.

Do not use this tool against systems without permission.

I'm not responsible for misuse of this software.

---

## Changelog

### v1.0

* Initial release
* Added target URL validation
* Added HTTP/HTTPS connection testing
* Added status code detection
* Added User-Agent selection
* Added Server detection
* Added Content-Type detection
* Added X-Powered-By detection
* Added basic HTTP error handling
* Added timeout handling
* Added randomized CLI messages
* Added initial reconnaissance output

---

## Author

**Pedro Mendes Jangada**

> *"That's all for today's edition."* 
