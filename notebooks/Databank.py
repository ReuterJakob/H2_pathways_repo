import pandas as pd

# import cost data from EWI Supply cost paper
#Define variables for LCOH calculation
#%%
# read Capex for NGR in  year y
ngr_time_inputs = pd.read_csv("/Users/jakob/PycharmProjects/H2_pathways_repo/data/raw/ngr_time_inputs.csv", sep=';')
ngr_time_inputs
# References:
# Capex
# Opex
# Natural gas prices
# EU CO2 price projections: https://www.reuters.com/markets/commodities/analysts-raise-eu-carbon-price-forecasts-downside-risks-remain-2022-07-29/
## 2022: average 88.36 € ($90.29) a tonne
### 2023: 97.66 €
#### 2024: 101.96 €/t

#read techno-economic assumptions for hydrogen production from NG
tea_ngr = pd.read_csv("/Users/jakob/PycharmProjects/H2_pathways_repo/data/raw/techno_economics.csv", sep = ';', decimal=",")
tea_ngr


