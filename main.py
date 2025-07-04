import matplotlib.pyplot as plt
import numpy as np

from model.Market import Market

agents = 100
houses = 100
income = 20000
incomeSD = 2050
wealth = 1000000
wealthSD = 1000000
price = 10000
priceSD = 250
rent = 10000
rentSD = 250
Time = 10
seed = 2025
time = np.linspace(0, Time, Time + 1)

market = Market(agents, houses, income, wealth, price, rent, incomeSD, wealthSD, priceSD, rentSD, Time)
market.simulate()
income = market.dataset("income", True)
wealth = market.dataset("wealth", True)
status = market.dataset("status", True)
houses = market.dataset("houses", True)

share = market.dataset("share")

share["unhoused"] = share.pop("u")
share["renter"] = share.pop("r")
share["investor"] = share.pop("i")
share["owner"] = share.pop("o")

fig, ax = plt.subplots()
ax.stackplot(time, share.values(), labels = share.keys())
plt.title("Agent Status")
ax.legend(loc = "upper right", reverse = True)
plt.xlabel("Time")
plt.grid()

plt.savefig(f"img/{market.seed}.png")
plt.show()