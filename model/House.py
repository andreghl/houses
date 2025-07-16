class House():
    """
    A class representing a house.

    Attributes:
        id (int): unique identifier.
        price (int): market price.
        rent (int): rental price.
        owner (Agent): agent owning the house when bought.
        tenant (Agent): agent renting the house when rented.
        status (str): status of the house:
            - empty
            - to rent
            - rented
            - owned
    """

    def __init__(self, id:int, price:int, rent:int):
        """
        Initializes a House object.

        Parameters:
            id (int): unique identifer.
            price (int): market price.
            rent (int): rental price.
        """
        self.id = id
        self.price = price
        self.rent = rent

        self.owner = None
        self.tenant = None
        self.status = "empty"

    def isAvailable(self, toRent:bool = False) -> bool:
        """
        Checks whether the house is on the rental or purchase market.

        Parameters:
            toRent (bool) = False: signals whether the agent desires to buy or rent.
        """
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
        self.owner = agent
        self.status = "to rent"
        if len(self.owner.houses) == 0:
            self.status = "owned"

    def rental(self, agent):
        self.status = "rented"
        self.tenant = agent

    def moving(self, agent):
        if self.tenant != None:
            if self.tenant.id == agent.id:
                self.status = "to rent"
                self.tenant = None


    def isRented(self, agent = None) -> bool:
        isRented:bool = False

        if agent and self.owner != None and self.status == "rented":
            if agent.id == self.owner.id:
                isRented = True
        elif agent == None and self.status == "rented":
            isRented = True
        return isRented



