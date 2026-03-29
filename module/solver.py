import requests
import time

def solveHcaptcha(apiKey, siteKey, pageUrl):
    createPayload = {
        "clientKey": apiKey,
        "task": {
            "type": "HCaptchaTaskProxyless",
            "websiteURL": pageUrl,
            "websiteKey": siteKey
        }
    }
    
    try:
        createResponse = requests.post("https://api.yescaptcha.com/createTask", json=createPayload).json()
        if createResponse.get("errorId") != 0:
            print(f"Error Create: {createResponse.get('errorCode')} - {createResponse.get('errorDescription')}")
            return None
            
        taskId = createResponse.get("taskId")
        while True:
            time.sleep(5)
            resultPayload = {"clientKey": apiKey, "taskId": taskId}
            resultResponse = requests.post("https://api.yescaptcha.com/getTaskResult", json=resultPayload).json()
            
            if resultResponse.get("status") == "ready":
                return resultResponse.get("solution", {}).get("gRecaptchaResponse")
            if resultResponse.get("errorId") != 0:
                print(f"Error Result: {resultResponse.get('errorCode')}")
                return None
    except Exception as e:
        print(f"Exception: {str(e)}")
        return None
