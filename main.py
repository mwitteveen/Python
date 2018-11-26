from API_Stocks import Stock


if __name__ == "__main__":
    stock = Stock("MSFT")
    strDate = "2017-10-10"

    stock.show("min")

    for date in stock.daily:
        print(stock.get_data(date,"12:00:00","min").close)

