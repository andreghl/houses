class Agent():

    def __init__(self, id, market, income, wealth, budget):
        self.id = id
        self.market = market
        self.income = income
        self.INCOME = income
        self.wealth = wealth
        self.budget = budget

        self.status = "unhoused"
        self.houses = []
        self.lease = None

    def update(self):
        if len(self.houses) > 1:
            self.status = "investor"
        elif len(self.houses) == 1:
            self.status = "owner"
        elif self.lease != None:
            self.status = "renter"
        else:
            self.status = "unhoused"

    def buy(self):
        for house in self.market.houses:
            if house.canBeBought(self):
                house.buy(self)
                self.wealth -= house.price
                self.houses.append(house)

                for home in self.houses:
                    if home.isRented(self):
                        home.status = "empty"

                self.lease = None
        self.update()
    
    def rent(self):
        if len(self.houses) == 0:
            for house in self.market.houses:
                if house.canBeRented(self):
                    house.rental()
                    self.lease = house
        self.update()

    def landlord(self):
        for house in self.houses:
            if house.isRented(self):
                self.wealth += house.rent

    def tenant(self):
        if self.lease != None:
            self.income -= self.lease.rent

    def step(self):
        
        self.buy()
        self.rent()
        self.landlord()
        self.tenant()


        self.wealth += self.income
        self.income = self.INCOME



        