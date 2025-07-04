import numpy as np

from House import House
from Agent import Agent
from Data import Data

class Market():
    
    def __init__(self, nAgents:int, nHouses:int, income:float, wealth:float, price:float, rent:float, incomeSD:float, wealthSD:float, priceSD:float, rentSD:float, Time:int = 1):
        self.nAgents = nAgents
        self.nHouses = nHouses
        self.income = income
        self.wealth = wealth
        self.price = price
        self.rent = rent
        self.incomeSD = incomeSD
        self.wealthSD = wealthSD
        self.priceSD = priceSD
        self.rentSD = rentSD
        
        
        self.houses = []
        self.agents = []
        self.time = 0
        self.Time = Time
        self.seed = 2025
        self.min = 0.2
        self.max = 0.6

        self.data = Data(self, nAgents, Time)

    def setSeed(self, seed):
        self.seed = seed

    def create(self):
        np.random.seed(self.seed)

        for i in range(self.nAgents):
            income = np.random.normal(self.income, self.incomeSD)
            wealth = np.random.normal(self.wealth, self.wealthSD)
            budget = abs(np.random.uniform(self.min, self.max))

            agent = Agent(i, self, income, wealth, budget)
            self.agents.append(agent)

        for i in range(self.nHouses):
            price = np.random.normal(self.price, self.priceSD)
            rent = np.random.normal(self.rent, self.rentSD)

            house = House(i, price, rent)
            self.houses.append(house)

    def run(self):

        self.create()

        while self.time <= self.Time: 

            for agent in self.agents:
                agent.step()

            self.data.collect(self.time)
            self.time += 1

    def summarize(self):
        summary = f"""The simulation contains {self.nAgents} agents and {self.nHouses} houses. The agents were endowned with an average income of {self.income} (sd: {self.incomeSD}) and an average wealth of {self.wealth} (sd: {self.wealthSD}).
                """
        print(summary)

    def simulate(self, summarize:bool = True):

        self.run()
        if summarize:
            self.summarize()

    def dataset(self, dataset:str, transpose:bool = False):

        match dataset:
            case "status":
                dataframe = self.data.status(transpose)
            case "income":
                dataframe = self.data.income(transpose)
            case "wealth":
                dataframe = self.data.wealth(transpose)
            case "budget":
                dataframe = self.data.budget(transpose)
            case "houses":
                dataframe = self.data.houses(transpose)
            case "rent":
                dataframe = self.data.rent(transpose)
            case "share":
                dataframe = self.data.share()    
            case _:
                dataframe = {}
        
        return dataframe