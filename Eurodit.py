import random
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import socket
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
        "[*] that one had to be useful.",
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
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
headers = {
    "User-Agent": useragent
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
                                                                                                                                                                                                     
                            version 1.0                                                             
    """)
say("start")
def starting():
    target = input("[+] Usage: Enter the target url\n").strip()
    url_valid = False
    while not url_valid:
        if target.startswith(("https://", "http://")):
            say("interesting")
            url_valid = True
            verifyUrl(target)
        else:
            say("error")
            print("[X] Invalid URL")
    return target

def verifyUrl(target):
    openurl = Request(target, method="HEAD", headers=headers)
    try:
        with urlopen(openurl, timeout=5) as response:
            print("[*] the server are working...")
            print(f"[+] Status code: {response.status}")
    except HTTPError as error:
        say("error")
        print(f"[X] HTTP error occurred: {error.code} - {error.reason}")
        starting()

    except (URLError, socket.timeout) as error:
        say("error")
        print(f"[X] the server {target} is down..., Reason {error.reason if hasattr(error, 'reason') else 'timeout'}")
        starting()

target = starting()
req = Request(target, headers=headers)
def decision():
    choice = input("[?] do you wanna use a User Agent? [y or N]").strip()
    return choice
choice = decision()
UserDecision = False
while UserDecision == False:
    if choice == "y":
        say("choice")
        useragent = input("[+] Insert the User Agent (or just type 'pass' to continue using a generic one): ")
        UserDecision = True
    elif choice == "N":
        print("[*] alright...")
        UserDecision = True
    else:
        UserDecision = False
        say("error")
        print("[X] Wrong Type Error")
        choice = decision()

match choice:
    case "y":
        if useragent == "pass":
            useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        req = Request(target, headers={"User-Agent": useragent})
        op = urlopen(req)
        say("interesting")
        SERVER = op.headers.get("Server")
        Content = op.headers.get("Content-Type")
        Xpower = op.headers.get("X-Powered-By")
    case "N":
        req = Request(target, method="HEAD")
        useragent = "none"
        try:
            with urlopen(req, timeout=5) as response:
                print("[*] the server are working...")
                print(f"[+] Status code: {response.status}")
                status = response.status
        except HTTPError as error:
            say("error")
            print(f"[X] HTTP error occurred: {error.code} - {error.reason}")
            if error.code == 403:
                print("[!] the server need to be accessed with a user agent")
                decision()
        op = urlopen(req)
        say("interesting")
        SERVER = op.headers.get("Server")
        Content = op.headers.get("Content-Type")
        Xpower = op.headers.get("X-Powered-By")

print(fr"""

    ▄       ▌ ▘      ▖ ▖       
    ▙▘▛▘█▌▀▌▙▘▌▛▌▛▌  ▛▖▌█▌▌▌▌▛▘
    ▙▘▌ ▙▖█▌▛▖▌▌▌▙▌  ▌▝▌▙▖▚▚▘▄▌  
             ▄▌            
    
    TARGET: {target}            USER AGENT: {useragent}
    SERVER: {SERVER}
    CONTENT TYPE: {Content} 
    X-POWERED BY: {Xpower}
    
""")














