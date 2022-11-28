import numpy as np
import pandas as pd
import math
from Databank import *
# Calculation of LCOH for natural gas reformation (NGR)
#ngr_time_inputs = pd.read_csv("/Users/jakob/PycharmProjects/H2_pathways_repo/data/raw/ngr_time_inputs.csv", sep=';')
ngr_time_inputs

#read techno-economic assumptions for hydrogen production from NG
tea_ngr = pd.read_csv("/Users/jakob/PycharmProjects/H2_pathways_repo/data/raw/techno_economics.csv", sep = ';', decimal=",")
tea_ngr

# Interest rate (WACC) in %
i = (tea_ngr.at[1,'NGR with CCS'])

i
#%%
# Economic lifetime of the plant in years
l = (tea_ngr.at[0,'NGR with CCS'])
l
#%%
# Calculate the amortisation factor alpha
alpha = (i * (1 + i)**l)/(1 + i)**(l - 1)
round(alpha,2)
#%%
# Capital expenditures in $/kW in year y
year_in = int(input())
year = year_in - 2020
year
capex_y = ngr_time_inputs.at[year ,'NGR with CCS']
capex_y
#%%
# Operational expenditures in $/kW/a in year y
opex_y = (tea_ngr.at[3,'NGR with CCS'])*capex_y
round(opex_y, 2)

#%%
# Capacity factor as the availability of the plant in %
CF = tea_ngr.at[5, 'NGR with CCS']
CF
#%%
# Natual gas price in year y in $/kWh
# maybe make projections on NG price development
#P_ng = tea_ngr.at[9,'NGR with CCS']
P_ng = 0.262
#%%
# Plant efficiency
n = tea_ngr.at[4,'NGR with CCS']
n
#%%
# Quantity of captured emissions in kg_CO2/kg_H2
Q_ce = tea_ngr.at[6,'NGR with CCS']
Q_ce
#%%
# Quantity of uncaptured emissions in kg_CO2/kg_H2
Q_ue = tea_ngr.at[7,'NGR with CCS']
Q_ue
#%%
# P_ccs is the cost for transporting and storing CO2 in $/t_co2
P_ccs = tea_ngr.at[10,'NGR with CCS']
P_ccs
#%%
# Price for CO2 in year y in $/t_co2
P_co2 = tea_ngr.at[11,'NGR with CCS']
P_co2
#%%
# LHV of hydrogen is 33.33 kWh/kg
LHV_h2 = tea_ngr.at[13,'NGR with CCS']
LHV_h2
#%% md

#%%
# Calculate LCOH_ngr [$/kg_h2] in year y
#%%
lcoh_ngr_y = LHV_h2*((alpha * capex_y + opex_y)/(CF * 8760) + 0.262/n) + (Q_ce * P_ccs + Q_ue * P_co2)/1000
lcoh_ngr_y
#%%
def calculate_lcoh_ngr():
    lcoh_ngr_y = LHV_h2*((alpha * capex_y + opex_y)/CF * 8760 + P_ng/n) + (Q_ce * P_ccs + Q_ue * P_co2)/1000

print('The cost of hydrogen production from NG' + 'in year ' + str(round(lcoh_ngr_y,2)) + ' [$/kg_h2]')
calculate_lcoh_ngr()

# Calculate the cost of hydrogen production from RES
