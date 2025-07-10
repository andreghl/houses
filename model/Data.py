import pandas as pd
import numpy as np

class Data():

    def __init__(self, model, agents:int, houses:int, steps:int):

        self.model = model
        self.agents = agents
        self.houses = houses
        self.steps = steps
        self.index = 0
        
        self.agentStatus = np.empty([self.agents, self.steps + 1], dtype = str)
        self.agentIncome = np.zeros([self.agents, self.steps + 1])
        self.agentWealth = np.zeros([self.agents, self.steps + 1])
        self.agentBudget = np.zeros([self.agents, self.steps + 1])
        self.agentHouses = np.zeros([self.agents, self.steps + 1])
        self.agentRent = np.zeros([self.agents, self.steps + 1])

        self.housePrice = np.zeros(self.houses)
        self.houseRent = np.zeros(self.houses)
        self.houseStatus = np.empty([self.houses, self.steps + 1], dtype = str)


    def collect(self, time):

        self.index = time

        for agent in self.model.agents:

            self.agentStatus[agent.id, self.index] = agent.status
            self.agentIncome[agent.id, self.index] = agent.income
            self.agentWealth[agent.id, self.index] = agent.wealth
            self.agentBudget[agent.id, self.index] = agent.budget
            self.agentHouses[agent.id, self.index] = len(agent.houses)
            self.agentRent[agent.id, self.index] =  0 if agent.lease == None else agent.lease.rent

        for house in self.model.houses:
            
            self.housePrice[house.id] = house.price
            self.houseRent[house.id] = house.rent
            self.houseStatus[house.id, self.index] = house.status


    def status(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentStatus)
        else:
            return pd.DataFrame(self.agentStatus.transpose())
            
    def share(self):
        factors = {"u": [0 for x in range(self.steps + 1)], 
                       "r": [0 for x in range(self.steps + 1)], 
                       "i": [0 for x in range(self.steps + 1)], 
                       "o": [0 for x in range(self.steps + 1)]}
            
        for col in range(self.steps + 1):
            for row in range(self.agents):

                for factor in factors.keys():
                    if self.agentStatus[row, col] == factor:
                        factors[factor][col] +=1
        return factors 
    
    def income(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentIncome)
        else:
            return pd.DataFrame(self.agentIncome.transpose())
    
    def wealth(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentWealth)
        else:   
            return pd.DataFrame(self.agentWealth.transpose())
    
    def budget(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentBudget)
        else:
            return pd.DataFrame(self.agentBudget.transpose())
    
    def house(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentHouses)
        else:
            return pd.DataFrame(self.agentHouses.transpose())
    
    def rent(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.agentRent.transpose())
        else:
            return pd.DataFrame(self.agentRent.transpose())
        
    def housesPrice(self):
            return pd.DataFrame(self.housePrice)
    
    def housesRent(self):
        return pd.DataFrame(self.houseRent)
        
    def housesStatus(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.houseStatus)
        else:
            return pd.DataFrame(self.houseStatus.transpose())
        
    def shareHouse(self):
        factors = {"o": [0 for x in range(self.steps + 1)], 
                        "r": [0 for x in range(self.steps + 1)],
                        "t": [0 for x in range(self.steps + 1)],
                        "e": [0 for x in range(self.steps + 1)]}
            
        for col in range(self.steps + 1):
            for row in range(self.houses):

                for factor in factors.keys():
                    if self.houseStatus[row, col] == factor:
                        factors[factor][col] +=1
        return factors 




