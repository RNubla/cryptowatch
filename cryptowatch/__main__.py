import cryptocompare
from win10toast import ToastNotifier
import locale
import time
import json


class CryptocurrencyNotif:
    def __init__(self, ticker, currency, quantityOwned):
        self.quantityOwned = quantityOwned
        self.ticker = ticker
        self.currency = currency
        locale.setlocale(locale.LC_ALL, '')
        self.toaster = ToastNotifier()

    def notification(self, interval, status):

        crypto = cryptocompare.get_price(self.ticker, currency=self.currency)
        cryptoTuple = ''
        for k, v in crypto.items():
            cryptoTuple = k, crypto.get(k).get(self.currency)
        if status == 'up':
            self.toaster.show_toast("The Price of {coin} is ${price} per Quantity 📈 ".format(coin=cryptoTuple[0], price=(cryptoTuple[1])),
                                    msg="You have made {profit}".format(
                profit=locale.currency(self.calcProfit(), grouping=True)),
                icon_path='assets/crypto_icon.ico',
                duration=interval)
        elif status == 'down':
            self.toaster.show_toast("The Price of {coin} is ${price} per Quantity 📉  ".format(coin=cryptoTuple[0], price=(cryptoTuple[1])),
                                    msg="You have made {profit}".format(
                profit=locale.currency(self.calcProfit(), grouping=True)),
                icon_path='assets/crypto_icon.ico',
                duration=interval)

    def getCurrentPrice(self) -> float:
        crypto = cryptocompare.get_price(self.ticker, currency=self.currency)
        cryptoTuple = ''
        for k, v in crypto.items():
            cryptoTuple = k, crypto.get(k).get(self.currency)
        return cryptoTuple[1]

    def calcProfit(self) -> float:
        profit = self.quantityOwned * self.getCurrentPrice()
        return round(profit, 2)


if __name__ == '__main__':
    """ Load user prefences stored in json format
        extract the data and pass the values as 
        arguements for methods
    """
    f = open('./preference.json',)
    prefData = json.load(f)
    cryptoCurrency = ''
    quantityOwned = ''
    currency = ''
    intervals = ''
    for k, v in prefData.items():
        """ Gets the key of the json, which returns a list, then take the 0 index
            which consist of CryptoCurrency, QuantityOwn, etc and gets each of 
            their values repectively
        """
        cryptoCurrency = prefData.get(k)[0].get('CryptoCurrency')
        quantityOwned = prefData.get(k)[0].get('QuantityOwned')
        currency = prefData.get(k)[0].get('Currency')
        intervals = prefData.get(k)[0].get('Intervals')
        # print(prefData.get(k)[0].get('CryptoCurrency'))
        # print(prefData.get(k)[0].get('QuantityOwned'))
        # print(prefData.get(k)[0].get('Currency'))
        # print(prefData.get(k)[0].get('Intervals'))

    f.close()
    cc = CryptocurrencyNotif(cryptoCurrency, currency,
                             quantityOwned=quantityOwned)
    oldPrice = cc.getCurrentPrice()
    while True:
        time.sleep(3)
        newPrice = cc.getCurrentPrice()
        if oldPrice > newPrice:  # means that the price is droppping
            print('new price d ', newPrice)
            cc.notification(int(intervals), 'down')
        elif oldPrice < newPrice:
            print('new price u ', newPrice)
            cc.notification(int(intervals), 'up')
