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


market = Market(agents, houses, income, wealth, price, rent, incomeSD, wealthSD, priceSD, rentSD, Time)
market.simulate()