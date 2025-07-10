class House():

    def __init__(self, id, price, rent):
        self.id = id
        self.price = price
        self.rent = rent

        self.owner = None
        self.status = "empty"

    def isAvailable(self, toRent:bool = False) -> bool:
        isAvailable:bool = False
        if toRent and self.status == "to rent":
            isAvailable = True
        elif not toRent and self.status == "empty":
            isAvailable = True 
        return isAvailable
    
    def isAffordable(self, agent, toRent:bool = False) -> bool:
        isAffordable:bool = False
        if not toRent and agent.wealth >= self.price:
            isAffordable = True
        elif toRent and (agent.budget * agent.income) >= self.rent:
            isAffordable = True
        return isAffordable
    
    def canBeBought(self, agent) -> bool:
        return self.isAvailable() and self.isAffordable(agent)
    
    def canBeRented(self, agent) -> bool:
        return self.isAvailable(True) and self.isAffordable(agent, True)
    
    def buy(self, agent):
        self.owner = agent.id
        if len(agent.houses) >= 1:
            self.status = "to rent"
        else:
            self.status = "owned"

    def rental(self):
        self.status = "rented"

    def isRented(self, agent = None) -> bool:
        isRented:bool = False

        if agent != None and self.status == "rented":
            if agent.id == self.owner:
                isRented = True
        elif agent == None and self.status == "rented":
            isRented = True
        return isRented



