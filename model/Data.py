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

        self.isTenant = np.zeros([self.agents, self.steps + 1])
        self.isOwn = np.zeros([self.agents, self.steps + 1])
        self.isInvested = np.zeros([self.agents, self.steps + 1])
        self.isHomeless = np.zeros([self.agents, self.steps + 1])

        self.isUnhoused = np.zeros([self.agents, self.steps + 1])
        self.isRenter = np.zeros([self.agents, self.steps + 1])
        self.isInvestor = np.zeros([self.agents, self.steps + 1])
        self.isOwner = np.zeros([self.agents, self.steps + 1])


    def collect(self, time):

        self.index = time

        for agent in self.model.agents:

            self.agentIncome[agent.id, self.index] = agent.income
            self.agentWealth[agent.id, self.index] = agent.wealth
            self.agentBudget[agent.id, self.index] = agent.budget
            self.agentHouses[agent.id, self.index] = int(len(agent.houses))
            self.agentRent[agent.id, self.index] =  0 if agent.lease == None else agent.lease.rent

            self.agentStatus[agent.id, self.index] = "unhoused" if agent.lease == None and len(agent.houses) == 0 else "renter" if agent.lease != None else "owner" if len(agent.houses) == 1 else "investor"

            self.isTenant[agent.id, self.index] = 0 if agent.lease == None else 1
            self.isOwn[agent.id, self.index] = 0 if len(agent.houses) == 0 else 1
            self.isInvested[agent.id, self.index] = 0 if len(agent.houses) < 1 else 1
            self.isHomeless[agent.id, self.index] = 0 if agent.lease != None or len(agent.houses) > 0 else 1

            self.isRenter[agent.id, self.index] = 1 if agent.status == "renter" else 0
            self.isOwner[agent.id, self.index] = 1 if agent.status == "owner" else 0
            self.isInvestor[agent.id, self.index] = 1 if agent.status == "investor" else 0
            self.isUnhoused[agent.id, self.index] = 1 if agent.status == "unhoused" else 0

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
            return pd.DataFrame(self.agentRent)
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
    
    def tenant(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isTenant)
        else:
            return pd.DataFrame(self.isTenant.transpose())
        
    def own(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isOwn)
        else:
            return pd.DataFrame(self.isOwn.transpose())

    def invested(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isInvested)
        else:
            return pd.DataFrame(self.isInvested.transpose())
        
    def homeless(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isHomeless)
        else:
            return pd.DataFrame(self.isHomeless.transpose())
    
    def renter(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isRenter)
        else:
            return pd.DataFrame(self.isRenter.transpose())

    def owner(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isOwner)
        else:
            return pd.DataFrame(self.isOwner.transpose())
        
    def investor(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isInvestor)
        else:
            return pd.DataFrame(self.isInvestor.transpose())
        
    def unhoused(self, transpose:bool = False):
        if transpose:
            return pd.DataFrame(self.isUnhoused)
        else:
            return pd.DataFrame(self.isUnhoused.transpose())
    
    def default(self):
        return pd.DataFrame()


