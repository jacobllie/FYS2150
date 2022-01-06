import scipy.io
import pandas as pd
import numpy as np

#Gjør om alle .mat filer til .csv


"""path = "M:\\Documents\\FYS2150_main\\FYS2150\\matlab-python-konvertering\\prelabb_i_python\\tid og frekvens\\"
mat = scipy.io.loadmat(path + "data1.mat")
df = pd.DataFrame(mat["data1"][:,0])
df.to_csv(path + "data1.csv", index = False)
"""

"""
path = "M:\\Documents\\FYS2150_main\\FYS2150\\matlab-python-konvertering\\prelabb_i_python\\gamma\\"
mat = scipy.io.loadmat(path + "poisson.mat")
df = pd.DataFrame(mat["data"][:,0])
df.to_csv(path + "poisson.csv", index = False)
"""

"""
path = "M:\\Documents\\FYS2150_main\\FYS2150\\matlab-python-konvertering\\prelabb_i_python\\gamma\\"
mat = scipy.io.loadmat(path + "spektrum.mat")
df = pd.DataFrame(mat["spektrum"][:,0])
df.to_csv(path + "spektrum.csv", index = False)
"""

"""
path = "M:\\Documents\\FYS2150_main\\FYS2150\\matlab-python-konvertering\\prelabb_i_python\\magnetisme\\"
mat = scipy.io.loadmat(path + "faraday.mat")
tmp = np.array([mat["B"][0,:], mat["theta"][0,:]]).T
df = pd.DataFrame(tmp, columns= ["B", "theta"])
df.to_csv(path + "faraday.csv", index = False)
"""

"""
path = "M:\\Documents\\FYS2150_main\\FYS2150\\matlab-python-konvertering\\prelabb_i_python\\strøm og spenning\\"
mat = scipy.io.loadmat(path + "RC_data.mat")
tmp = np.array([mat['Vu_over_Vi'][0,:], mat['frekvens'][0,:]]).T
df = pd.DataFrame(tmp, columns= ['Vu_over_Vi', 'frekvens'])
df.to_csv(path + "RC_data.csv", index = False)
"""