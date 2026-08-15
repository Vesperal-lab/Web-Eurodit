import random
import socket
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from pathlib import Path


MESSAGES = {
    "start": [
        "[*] Good evening, young man.",
        "[*] Let's see what today's newspaper says...",
        "[*] Another day, another headline..."
    ],

    "interesting": [
        "[*] Interesting...",
        "[*] Well, well, well...",
        "[*] Now that's a curious headline."
    ],

    "error": [
        "[*] Ouch, I cut my finger on paper.",
        "[*] The newspaper seems unreadable today.",
        "[*] My glasses aren't helping with this one."
    ],

    "vuln": [
        "[*] rise and shiny mr root.",
        "[*] that one can be useful.",
        "[*] maybe you can use this..."
    ],

    "choice": [
        "[*] You know what you are doing son.",
        "[*] Good choice."
    ],

    "finish": [
        "[*] That's all for today's edition.",
        "[*] Nothing more to report.",
        "[*] I'll see you in tomorrow's edition."
    ]
}
DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
headers = {
    "User-Agent": DEFAULT_USER_AGENT
}
def say(category):
    print(random.choice(MESSAGES[category]))
print(r"""

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
    """)

say("start")
BASE_DIR = Path(__file__).resolve().parent
def starting():
    while True:
        target = input("[+] Usage: Enter the target url\n").strip()
        if target.startswith(("https://", "http://")):
            say("interesting")
            return target
        say("error")
        print("[X] Invalid URL")

def verifyUrl(target):
    request = Request(
        target,
        method="HEAD",
        headers=headers
    )

    try:
        with urlopen(request, timeout=5) as response:
            print("[*] The server is working...")
            print(f"[+] Status code: {response.status}")
            return response
    except HTTPError as error:
        say("error")
        print(
            f"[X] HTTP error occurred: "
            f"{error.code} - {error.reason}"
        )
        return None
    except (URLError, socket.timeout) as error:
        say("error")
        reason = (
            error.reason
            if hasattr(error, "reason")
            else "timeout"
        )
        print(
            f"[X] The server {target} is unreachable. "
            f"Reason: {reason}"
        )
        return None
target = starting()
response = verifyUrl(target)
host = urlparse(target).hostname

def resolveIp(host):
    try:
        return socket.gethostbyname(host)
    except socket.gaierror:
        return "Unable to resolve"

if response is None:
    print("[X] Eurodit could not continue.")
    exit()
STATUS = response.status
REASON_STATUS = f"{response.status}:{response.reason}"
SERVER = response.headers.get("Server")
CONTENT_TYPE = response.headers.get("Content-Type")
X_POWERED_BY = response.headers.get("X-Powered-By")
IP = resolveIp(host)
CONTENT_LENGTH = response.headers.get("Content-Length")
LOCATION = response.headers.get("Location")
CACHE_CONTROL = response.headers.get("Cache-Control")
COOKIES = response.headers.get("Set-Cookie")
print(fr"""
    ▖▖     ▌▜ ▘       
    ▙▌█▌▀▌▛▌▐ ▌▛▌█▌  ▖
    ▌▌▙▖█▌▙▌▐▖▌▌▌▙▖  ▖  
                                        
    TARGET: {target}                    
    USER AGENT: {DEFAULT_USER_AGENT}    
    STATUS: {REASON_STATUS}             
    SERVER: {SERVER}                    
    CONTENT TYPE: {CONTENT_TYPE}        
    IP: {IP} 
    X-POWERED BY: {X_POWERED_BY}
    COOKIES: {COOKIES}
    CACHE CONTROL: {CACHE_CONTROL}
    LOCATION: {LOCATION}
    CONTENT LENGTH: {CONTENT_LENGTH}
""")
input("PRESS ENTER FOR OPTIONS...")

def directoryChoice():
    while True:
        directory = input("[+] Select an option: ").strip().upper().replace(" ", "")

        match directory:
            case "F" | "D" | "FS" | "DS":
                return directory

            case _:
                say("error")
                print("[X] Invalid option (you can't use the Deep search and Fast search)")

def options():
    while True:
        opt = input(f"""
    ┏┓   •        
    ┃┃┏┓╋┓┏┓┏┓┏  •
    ┗┛┣┛┗┗┗┛┛┗┛  •
      ┛           

    [1] HTTP Headers
    [2] Directory Enumeration
    [3] WAF Detection (coming soon...)
    [4] Security Checks (coming soon...)
    [5] Exit

    [+] Select an option: """)

        match opt:
            case "1":
                print(f"""
┓┏    ┏┏┓┓  ┓┏     ┓       
┣┫╋╋┏┓┃┗┓┃  ┣┫┏┓┏┓┏┫┏┓┏┓┏  
┛┗┗┗┣┛┗┗┛┛  ┛┗┗ ┗┻┗┻┗ ┛ ┛  

Target: {target}
Server: {SERVER}
Content-Type: {CONTENT_TYPE}
Content-Length: {CONTENT_LENGTH}
X-Powered-By: {X_POWERED_BY}
Cache-Control: {CACHE_CONTROL}
Location: {LOCATION}
Set-Cookie: {COOKIES}
                """)
                input("PRESS ENTER FOR CONTINUE...")

            case "2":
             print(f"""
┳┓•              ┏┓              •    
┃┃┓┏┓┏┓┏╋┏┓┏┓┓┏  ┣ ┏┓┓┏┏┳┓┏┓┏┓┏┓╋┓┏┓┏┓
┻┛┗┛ ┗ ┗┗┗┛┛ ┗┫  ┗┛┛┗┗┻┛┗┗┗ ┛ ┗┻┗┗┗┛┛┗
              ┛                       
OPTIONS: 
F = "Fast" For a fast search (using a smaller wordlist (recommended))
D = "Deep" For a deep search (using a bigger wordlist)
S = "Show All" For show all response url's (including 404)              
              
target: {target}
                """)

             directory = directoryChoice()


             match directory:
                 case "F":
                     print("[*] Fast scan selected")
                     haveS = False

                 case "D":
                     print("[*] Deep scan selected")
                     haveS = False

                 case "FS":
                     print("[*] Fast scan selected")
                     print("[*] Show All enabled")
                     haveS = True

                 case "DS":
                     print("[*] Deep scan selected")
                     print("[*] Show All enabled")
                     haveS = True

             def simpleVerify(target):
                 request = Request(target, method="HEAD", headers=headers)
                 try:
                     with urlopen(request, timeout=5) as response:
                         status = response.status
                         if haveS:
                             if "adm" in target:
                                 print(" ")
                                 say("interesting")
                             print(" ")
                             print("[*] FOUND")
                             print(f"[+] Status code: {status}")
                             print(f"[+] {target}")
                             print("__________________________________________________________")
                             return True

                         elif status != 404:
                             if "adm" in target:
                                 say("interesting")
                             print("[*] FOUND")
                             print(f"[+] Status code: {status}")
                             print(f"[+] {target}")
                             print("__________________________________________________________")

                             return True


                         return False
                 except HTTPError as error:
                     return False
                 except (URLError, socket.timeout) as error:
                     return False

             if "F" in directory:
                 wordlist = BASE_DIR / "Euromini.txt"
             elif "D" in directory:
                 wordlist = BASE_DIR / "Eurolib.txt"
             def directoryEnum(target, wordlist):
                tested = 0
                found = 0
                try:
                    with open(wordlist, "r") as file:
                        for dir in file:

                            path = dir.strip()
                            url = target.rstrip("/") + "/" + path
                            print(f"\r[*] Testing: {url}", end="", flush=True)
                            if simpleVerify(url):
                                found += 1
                            tested += 1
                    print("\n[*] Directory enumeration finished.")
                    print(f"[*] Paths tested: {tested}")
                    print(f"[*] Paths tested: {found}")
                except KeyboardInterrupt:
                    print("\n")
                    print("[*] Scan interrupted by user.")
                    print(f"[*] Paths tested: {tested}")
                    print(f"[*] Paths tested: {found}")
             directoryEnum(target, wordlist)

            case "3":
                print("[*] WAF Detection coming soon...")
                input("PRESS ENTER FOR CONTINUE...")
            case "4":
                print("[*] Security Checks coming soon...")
                input("PRESS ENTER FOR CONTINUE...")
            case "5":
                print("[*] Exiting Eurodit...")
                break

            case _:
                say("error")
                print("[X] Invalid number")


options()