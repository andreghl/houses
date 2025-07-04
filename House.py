class House():

    def __init__(self, id, price, rent):
        self.id = id
        self.price = price
        self.rent = rent

        self.owner = None
        self.status = "empty"