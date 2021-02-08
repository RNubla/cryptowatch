import cryptocompare
from win10toast import ToastNotifier
import locale
import time


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
        # toaster = ToastNotifier()
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
    cc = CryptocurrencyNotif('DOGE', 'USD', quantityOwned=1142)
    oldPrice = cc.getCurrentPrice()
    while True:
        time.sleep(3)
        newPrice = cc.getCurrentPrice()
        if oldPrice > newPrice:  # means that the price is droppping
            print('new price d ', newPrice)
            cc.notification(5, 'down')
        elif oldPrice < newPrice:
            print('new price u ', newPrice)
            cc.notification(5, 'up')
