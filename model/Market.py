import numpy as np
import matplotlib.pyplot as plt

from model.House import House
from model.Agent import Agent
from model.Data import Data

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

        self.data = Data(self, nAgents, nHouses, Time)

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

    def share(self, dataset:str):

        match dataset:
            case "agent":
                dataframe = self.data.share()
                dataframe["unhoused"] = dataframe.pop("u")
                dataframe["renter"] = dataframe.pop("r")
                dataframe["investor"] = dataframe.pop("i")
                dataframe["owner"] = dataframe.pop("o")
            case "house":
                dataframe = self.data.shareHouse()
                dataframe["empty"] = dataframe.pop("e")
                dataframe["rented"] = dataframe.pop("r")
                dataframe["owned"] = dataframe.pop("o")
                dataframe["to rent"] = dataframe.pop("t")
            case _:
                dataframe = {}
        
        return dataframe
    
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
                dataframe = self.data.house(transpose)
            case "rent":
                dataframe = self.data.rent(transpose)
            case "housePrice":
                dataframe = self.data.housesPrice()
            case "houseRent":
                dataframe = self.data.housesRent()
            case "houseStatus":
                dataframe = self.data.housesStatus(transpose)
            case _:
                dataframe = {}
    
        return dataframe

    def plot(self):
        time = np.linspace(0, self.Time, self.Time + 1)
        agent = self.share("agent")
        house = self.share("house")
        
        fig, ax = plt.subplots()
        ax.stackplot(time, *list(agent.values()), labels = agent.keys())
        plt.title("Agent Status")
        ax.legend(loc = "upper right", reverse = True)
        plt.xlabel("Time")
        plt.grid()
        plt.savefig(f"img/agent/{self.seed}.png")

        fig, ax = plt.subplots()
        ax.stackplot(time, *list(house.values()), labels = house.keys())
        plt.title("House Status")
        ax.legend(loc = "upper right", reverse = True)
        plt.xlabel("Time")
        plt.savefig(f"img/house/{self.seed}.png")
        plt.show()

    def summarize(self):
        summary = f"""The simulation contains {self.nAgents} agents and {self.nHouses} houses. The agents were endowned with an average income of {self.income} (sd: {self.incomeSD}) and an average wealth of {self.wealth} (sd: {self.wealthSD}). The average house price was {self.price} (sd: {self.priceSD}) and the average rent was {self.rent} (sd: {self.rentSD})."""

        print(summary)

    def simulate(self, plot:bool = True):

        self.run()
        self.summarize()
        if plot:
            self.plot()

