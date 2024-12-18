import requests
from bs4 import BeautifulSoup
import json

def makeRes(method, url, out, params):
    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }

    MethodDic = {
        "GET":requests.get,
        "POST":requests.post,
        "PUT":requests.put,
        "Delete":requests.delete
    }

    nowMethod = MethodDic[method]

    response = nowMethod(url, params=params, headers=headers)

    status = response.status_code

    resHeaders = response.request.headers

    if out == "JSON":
        resOutPut = json.dumps(response.json(), indent=4)
        return {"res":resOutPut, "statusCode":status, "resHeaders":resHeaders}
    else:
        soup = BeautifulSoup(response.text, 'html.parser')
        resOutPut = soup.prettify()
        return {"res":resOutPut, "statusCode":status, "resHeaders":resHeaders}