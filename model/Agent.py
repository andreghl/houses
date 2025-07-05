class Agent():

    def __init__(self, id, market, income, wealth, budget):
        self.id = id
        self.market = market
        self.income = income
        self.wealth = wealth
        self.budget = budget

        self.status = "unhoused"
        self.houses = []
        self.rentPrice = -1
        self.lease = None

    def buy(self):

        for house in self.market.houses:
            if house.status == "empty" and house.price <= self.wealth:
                house.status = "rent" if len(self.houses) >= 1 else "owned"
                house.owner = self.id
                self.wealth -= house.price
                self.houses.append(house)
                self.rentPrice = 0
                self.lease = None
                break
    
    def rent(self):
        for house in self.market.houses:
            if house.status == "rent" and house.rent <= self.budget * self.income and len(self.houses) == 0:
                house.status = "rented"
                self.status = "renter"
                self.rentPrice = house.rent
                self.lease = house.id

    def landlord(self):
        for house in self.houses:
            if house.status == "rented":
                self.wealth += house.rent

    def tenant(self):
        self.income -= self.rentPrice

    def step(self):

        if len(self.houses) > 1:
            self.status = "investor"
        elif len(self.houses) == 1:
            self.status = "owner"
        elif self.lease != None:
            self.status = "renter"
        else:
            self.status = "unhoused"
        
        self.buy()
        self.rent()
        self.landlord()
        self.tenant()

        