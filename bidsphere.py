class Auction:
    def __init__(self, start_price):
        self.highest_bid = start_price

    def place_bid(self, amount):
        if amount > self.highest_bid:
            self.highest_bid = amount
            return "Bid Accepted"
        else:
            return "Bid Rejected"

auction = Auction(100)

print(auction.place_bid(120))
print(auction.place_bid(110))
