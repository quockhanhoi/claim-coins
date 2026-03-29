import sys
from pystyle import Colors, Colorate, Center

def showBanner():
    if sys.stdout.encoding != 'utf-8':
        sys.stdout.reconfigure(encoding='utf-8')
    with open("module/banner.env", "r", encoding="utf-8") as f:
        bannerText = f.read()
    print(Colorate.Vertical(Colors.blue_to_purple, Center.XCenter(bannerText)), flush=True)
    
    with open("module/in4.env", "r", encoding="utf-8") as f:
        for line in f:
            if ":" in line:
                key, val = line.split(":", 1)
                print(f"{Colors.purple}[{key.strip()}] {Colors.white}{val.strip()}", flush=True)
    print("-" * 50, flush=True)


