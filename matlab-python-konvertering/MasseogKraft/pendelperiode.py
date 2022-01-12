"""
Program for bruk i Tid og Frekvens og Masse og kraft. Bruker fotodiode og NI USB-6211
Varighet på datainnsamling og frekvens osv må skrives inn manuelt nederst.

Jacob Lie og Anders Bråte v2021.
"""
import numpy as  np
import pandas as pd
from daq import read_daq, rising_edge, plot_data

duration = 10
sample_rate = 500
samples_per_channel = int(sample_rate * duration)
inputrange = 10

data, t = read_daq(sample_rate, duration, inputrange)
print(t)

"""
df = pd.DataFrame(data)
df.to_csv("pendel_data.csv")
np.save("pendel_data.npy",data)
"""
rising_edge_index, period, mean_period, std_period = rising_edge(data, t)
print("Periodetider:",end=" ")
print(period)
print("Gjennomsnittlig Periode:",end=" ")
print(mean_period)
print("Standardavvik i periodetidene:",end=" ")
print(std_period)
plot_data(data, t, rising_edge_index, period)
     

