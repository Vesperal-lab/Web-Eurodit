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
* Target IP resolution
* HTTP response information
* HTTP headers inspection
* Interactive options menu
* Directory enumeration
* Fast directory enumeration
* Deep directory enumeration
* Fast and Deep wordlists
* Show All option
* Fast + Show All option
* Deep + Show All option
* Path testing counter
* Found results counter
* Scan interruption with Ctrl+C
* Relative wordlist path handling
* Dynamic URL testing display
* Randomized messages for interesting findings

---

## How It Works

Web Eurodit starts by asking the user for a target URL.

```text
> python Eurodit.py


                             ___                                                      ___         ___      
                            (   )                                                    (   )  .-.  (   )     
     ___  ___  ___   .--.    | |.-.       .--.    ___  ___   ___ .-.      .--.     .-.| |  ( __)  | |_     
    (   )(   )(   ) /    \   | /   \     /    \  (   )(   ) (   )   \    /    \   /   \ |  (''") (   __)   
     | |  | |  | | |  .-. ;  |  .-. |   |  .-. ;  | |  | |   | ' .-. ;  |  .-. ; |  .-. |   | |   | |      
     | |  | |  | | |  | | |  | |  | |   |  | | |  | |  | |   |  / (___) | |  | | | |  | |   | |   | | ___  
     | |  | |  | | |  |/  |  | |  | |   |  |/  |  | |  | |   | |        | |  | | | |  | |   | |   | |(   ) 
     | |  | |  | | |  ' _.'  | |  | |   |  ' _.'  | |  | |   | |        | |  | | | |  | |   | |   | | | |  
     | |  ; '  | | |  .'.-.  | '  | |   |  .'.-.  | |  ; '   | |        | '  | | | '  | |   | |   | ' | |  
     ' `-'   `-' ' '  `-' /  ' `-' ;    '  `-' /  ' `-'  /   | |        '  `-' / ' `-'  /   | |   ' `-' ;  
      '.__.'.__.'   `.__.'    `.__.      `.__.'    '.__.'   (___)        `.__.'   `.__,'   (___)   `.__. 
        
                                            version 1.2
    
[*] Let's see what today's newspaper says...
[+] Usage: Enter the target url

```

The URL is then validated to make sure it uses either `http://` or `https://`.

After validation, Eurodit sends the request using a generic User-Agent to improve compatibility with servers that may reject requests from unknown or uncommon clients.

```text
https://example.com/
[*] Interesting...
[*] The server is working...
[+] Status code: 200

    ▖▖     ▌▜ ▘       
    ▙▌█▌▀▌▛▌▐ ▌▛▌█▌  ▖
    ▌▌▙▖█▌▙▌▐▖▌▌▌▙▖  ▖  
                                        
    TARGET: https://example.com/                    
    USER AGENT: Mozilla/5.0 (Windows NT 10.0; Win64; x64)    
    STATUS: 200:OK             
    SERVER: cloudflare                    
    CONTENT TYPE: text/html        
    IP: 104.20.23.154 
    X-POWERED BY: None
    COOKIES: None
    CACHE CONTROL: None
    LOCATION: None
    CONTENT LENGTH: None
```

## Removed

* User Agent Choose (just use a generic one)
____________________________________________

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

```
            ┌─────────────────┐
            │    Target URL   │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  URL Validation │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   HTTP Request  │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │  Target Info    │
            │                 │
            │ IP              │
            │ Status          │
            │ Server          │
            │ Content-Type    │
            └────────┬────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   Options Menu  │
            └────────┬────────┘
                     │
      ┌──────────────┼──────────────┐
      │              │              │
      ▼              ▼              ▼
 ┌─────────┐   ┌────────────┐  ┌────────────┐
 │ Headers │   │ Directory  │  │ WAF Detect │
 │         │   │ Enumeration│  │(planned)   │
 └────┬────┘   └─────┬──────┘  └─────┬──────┘
      │              │               │
      └──────────────┼───────────────┘
                     │
                     ▼
            ┌─────────────────┐
            │   Final Report  │
            └─────────────────┘
```

---

## Directory Enumeration

Eurodit includes two wordlists:

* `Euromini.txt` — Fast enumeration
* `Eurolib.txt` — Deep enumeration

The wordlists are included in the repository and are automatically loaded by Eurodit.

---

## Example Output

Example of the Options menu:

```text
PRESS ENTER FOR OPTIONS...

    ┏┓   •        
    ┃┃┏┓╋┓┏┓┏┓┏  •
    ┗┛┣┛┗┗┗┛┛┗┛  •
      ┛           

    [1] HTTP Headers
    [2] Directory Enumeration
    [3] WAF Detection (coming soon...)
    [4] Security Checks (coming soon...)
    [5] Exit

    [+] Select an option: 
```

Example of directory enumeration:

```text


┳┓•              ┏┓              •    
┃┃┓┏┓┏┓┏╋┏┓┏┓┓┏  ┣ ┏┓┓┏┏┳┓┏┓┏┓┏┓╋┓┏┓┏┓
┻┛┗┛ ┗ ┗┗┗┛┛ ┗┫  ┗┛┛┗┗┻┛┗┗┗ ┛ ┗┻┗┗┗┛┛┗
              ┛                       
OPTIONS: 
F = "Fast" For a fast search (using a smaller wordlist (recommended))
D = "Deep" For a deep search (using a bigger wordlist)
S = "Show All" For show all response url's (including 404)              
              
target: https://example.com/


```

---

## Screenshots

Screenshots of Web Eurodit will be added as the interface continues to evolve.

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
* [x] Options Menu
* [x] Improved response analysis

### v1.1 — Reconnaissance Improvements

* [x] Target IP resolution
* [x] HTTP response information
* [x] HTTP headers inspection
* [x] Interactive options menu
* [x] Improved error handling
* [x] Placeholders for directory enumeration
* [x] Placeholders for WAF detection
* [x] Placeholders for security checks

### v1.2 — Directory Enumeration

* [x] Directory enumeration
* [x] Fast enumeration
* [x] Deep enumeration
* [x] `Euromini.txt` wordlist
* [x] `Eurolib.txt` wordlist
* [x] Show All option
* [x] Fast + Show All option
* [x] Deep + Show All option
* [x] Path testing counter
* [x] Found results counter
* [x] Scan interruption with `Ctrl+C`
* [x] Relative wordlist path handling
* [x] Dynamic URL testing display
* [x] Randomized messages for interesting findings
* [x] `robots.txt` detection

## Future

* [ ] Full HTTP header enumeration
* [ ] Customize User Agent
* [ ] Security header detection
* [ ] Redirect detection
* [ ] Improved HTTP request handling
* [ ] Technology detection
* [ ] `sitemap.xml` detection
* [ ] Basic endpoint discovery
* [ ] More detailed server information
* [ ] Better timeout handling
* [ ] Configurable request options
* [ ] Improved CLI output
* [ ] Verbose mode
* [ ] Web crawler
* [ ] WAF detection
* [ ] Vulnerability checks
* [ ] JSON output
* [ ] Report generation

## Version

**Current version: 1.2**

---

## Disclaimer

Web Eurodit was created for **educational purposes and authorized security testing**.

Do not use this tool against systems without permission.

I'm not responsible for misuse of this software.

---

## Changelog

### v1.2

* Added directory enumeration
* Added `Euromini.txt` wordlist for Fast enumeration
* Added `Eurolib.txt` wordlist for Deep enumeration
* Added Fast enumeration option
* Added Deep enumeration option
* Added Show All option
* Added Fast + Show All option
* Added Deep + Show All option
* Added path testing counter
* Added found results counter
* Added scan interruption with `Ctrl+C`
* Added relative wordlist path handling
* Added dynamic URL testing display
* Added randomized messages for interesting findings
* Added `robots.txt` detection

### v1.1

* Added target IP resolution
* Added HTTP response information
* Added HTTP headers inspection
* Added interactive options menu
* Added placeholders for future directory enumeration
* Added placeholders for future WAF detection
* Added placeholders for future security checks
* Improved error handling

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

