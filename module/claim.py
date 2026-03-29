import time
from module.logs import printInfo, printSuccess, printError
from module.in4 import getUserInfo, getFreeCoinsStatus, claimFreeCoins
from module.solver import solveHcaptcha


def autoClaim(token, apiKey, siteKey, pageUrl):
    while True:
        status = getFreeCoinsStatus(token)
        if not status:
            printError("Status error. Retrying in 1 min...")
            time.sleep(60)
            continue

        if status.get("claimable"):
            captchaNeeded = status.get("captcha", True)
            result = None
            
            if not captchaNeeded:
                printSuccess("Action: Claiming(không cần giải captcha)...")
                result = claimFreeCoins(token, None)
            else:
                printSuccess("Action: Claiming(cần giải captcha)...")
                captchaToken = solveHcaptcha(apiKey, siteKey, pageUrl)
                if captchaToken:
                    result = claimFreeCoins(token, captchaToken)
                else:
                    printError("Captcha failed.")
            
            if result and result.get("success"):
                printSuccess("Success: Claimed!")
                user = getUserInfo(token)
                if user:
                    printSuccess(f"Balance: {user.get('coins')} coins")
            elif result:
                msg = result.get('message', "Error")
                printError(f"Failed: {msg}")
                if "ratelimited" in msg.lower():
                    time.sleep(1800)
        waitSec = 10
        target = time.time() + waitSec
        while time.time() < target:
            rem = target - time.time()
            print(f"\r[!] Tiep tuc sau: {rem:.2f}s ", end="", flush=True)
            time.sleep(0.05)
        print("\r" + " " * 40 + "\r", end="", flush=True)
