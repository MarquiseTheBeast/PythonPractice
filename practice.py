class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def flip_to_tails(self):
        self.sideup = 'Tails'

def flip_it(coin):
    coin.flip_to_tails()

my_coin = Coin()
flip_it(my_coin)
print(my_coin.sideup)