# https://www.postfinance.ch/en/private/support/tools-calculator/currency-converter.html

# pip install requests
import requests
import json

class PostFinanceProxy():
    def __init__(self):
        self._url = "https://www.postfinance.ch/pfch-rest/unsecure/calculator/currency/calculate"
    
    def _ensureSuccessfullResponse(self, response):
        if response.status_code < 200 or response.status_code >= 300:
            raise ValueError(f"error: { response.text }")

    def convert(self, amount, fromCurrency: str, toCurrency: str):
        payload = {
            "amount":amount,
            "baseCurrency":fromCurrency,
            "targetCurrency":toCurrency,
            "triggerField":"amount",
            "lastChanged":"amount"
        }
        
        with requests.Session() as s:
            response = s.post(
                url = self._url,
                data = json.dumps(payload), 
                headers={'content-type': 'application/json'})

            self._ensureSuccessfullResponse(response)

            responseJson = json.loads(response.text)
            print(type(responseJson))

            if "error" in responseJson:
                print(f"Received error: {responseJson.error.reason}")
            if "result" in responseJson:
                result_value = responseJson['result']['result']
                return float(result_value)


try:
    qty = 1
    currencyFrom = "EUR"
    currencyTo = "CHF"
    proxy = PostFinanceProxy()
    convertedAmount = proxy.convert(qty, currencyFrom, currencyTo)
    print(f"{qty} {currencyFrom} = {convertedAmount:.2f}{currencyTo}")
except Exception as ex:
    print(f"Error: {ex.args[0]}")