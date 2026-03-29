import requests

def callApi(path, token):
    headers = {
        "authorization": token,
        "user-agent": "Mozilla/5.0"
    }
    response = requests.get(f"https://bot-hosting.net{path}", headers=headers)
    return response.json() if response.status_code == 200 else None

def getUserInfo(token):
    return callApi("/api/me", token)

def getServers(token):
    return callApi("/api/servers", token)

def getTransactions(token):
    return callApi("/api/transactions", token)

def getAffiliate(token):
    return callApi("/api/affiliate", token)

def getFreeCoinsStatus(token):
    return callApi("/api/freeCoinsStatus", token)

def claimFreeCoins(token, hCaptchaResponse):
    headers = {
        "authorization": token,
        "content-type": "application/json",
        "user-agent": "Mozilla/5.0"
    }
    data = {"hCaptchaResponse": hCaptchaResponse}
    response = requests.post("https://bot-hosting.net/api/freeCoins", headers=headers, json=data)
    return response.json() if response.status_code == 200 else None
