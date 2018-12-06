import json
import requests

#functie om Stock informatie op te halen
class Stock:

    #initialisatie aan de hand van Symbool
    def __init__(self,strSymbol):
        try:
            self.data_day = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + strSymbol + "&outputsize=full&apikey=674RK751J1T6NO31").json()
            self.data_min = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&interval=1min&symbol=" + strSymbol + "&outputsize=full&apikey=674RK751J1T6NO31").json()
            self.daily = self.data_day["Time Series (Daily)"]
            self.daily_min = self.data_min["Time Series (1min)"]
            self.name = strSymbol
        except:
            print("Error in constructor")

    def show(self, sKeus = "day"):
        if sKeus == "day":
            print(json.dumps(self.data_day, indent=4, sort_keys=True))
        elif sKeus == "min":
            print(json.dumps(self.data_min, indent=4, sort_keys=True))
        else:
            print("Foutieve sleutel opgegeven")

    def get_data(self,strDate,strTime = "", sKeus = "day"):
        if sKeus == "day":
            return single_options(self.data_day["Time Series (Daily)"][strDate])
        elif sKeus == "min":
            if strTime != "":
                return single_options(self.data_min["Time Series (1min)"][strDate + " " + strTime]).close
        else:
            print("Invalid key")

class single_options:
    def __init__(self,data):
        self.open = data["1. open"]
        self.high = data["2. high"]
        self.low = data["3. low"]
        self.close = data["4. close"]
        self.volume = data["5. volume"]


class stick_min:
    def __init__ (self,strSymbol):
        Stock.__init__(strSymbol)


