import os
from module.logs import printInfo, printSuccess, printError
from module.in4 import getUserInfo, getServers, getTransactions, getAffiliate
from module.banner import showBanner
from module.claim import autoClaim

def getEnv(key):
    try:
        if os.path.exists(".env"):
            with open(".env", "r") as f:
                for line in f:
                    if line.startswith(f"{key}="):
                        return line.split("=", 1)[1].strip()
    except: pass
    return None

def main():
    showBanner()
    tokenInput = input(" [?] Nhập Token: ").strip()
    if not tokenInput:
        printError("Token không được để trống!")
        return

    apiKey = getEnv("apiKey")
    siteKey = getEnv("siteKey")
    pageUrl = getEnv("pageUrl")

    user = getUserInfo(tokenInput)
    if user:
        printSuccess(f"Login: {user.get('username')} | Xu: {user.get('coins')}")
        
        servers = getServers(tokenInput)
        if isinstance(servers, list):
            printInfo("Server đang chạy", len(servers))
            
        transactions = getTransactions(tokenInput)
        if isinstance(transactions, list):
            printInfo("Hoạt động gần đây", transactions[0].get('text') if transactions else "Trống")
            
        affiliate = getAffiliate(tokenInput)
        if affiliate:
            printInfo("Affiliate Link", affiliate.get("link"))
            
        print("-" * 50, flush=True)
        printSuccess("Starting Auto Claimer...")
        autoClaim(tokenInput, apiKey, siteKey, pageUrl)
    else:
        printError("Invalid Token")

if __name__ == "__main__":
    main()
