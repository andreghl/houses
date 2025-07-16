from model.Market import Market
import matplotlib.pyplot as plt
import numpy as np

agents = 100
houses = 100
income = 20000
incomeSD = 2050
wealth = 1000000
wealthSD = 1000000
price = 1000000
priceSD = 250
rent = 10000
rentSD = 250
Time = 50
seed = 2025

market = Market(agents, houses, income, wealth, price, rent, incomeSD, wealthSD, priceSD, rentSD, Time)
market.setSeed(seed)
market.simulate()

houses = market.dataset("houses")

x = houses.loc[Time - 1, :].astype(np.int32)
plt.hist(x)
plt.show()