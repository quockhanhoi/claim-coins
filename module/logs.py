from pystyle import Colors, Colorate, Center

def printInfo(label, value):
    print(f"{Colors.cyan}{label}: {Colors.white}{value}", flush=True)

def printSuccess(msg):
    print(f"{Colors.green}[+] {msg}", flush=True)

def printError(msg):
    print(f"{Colors.red}[!] {msg}", flush=True)

