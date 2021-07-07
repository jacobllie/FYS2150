"""
Program for bruk i Tid og Frekvens og Masse og kraft. Bruker fotodiode og NI USB-6211
Varighet på datainnsamling og frekvens osv må skrives inn manuelt nederst.
"""
import sys
import nidaqmx
import numpy as  np
from nidaqmx.constants import Edge, AcquisitionType, TerminalConfiguration
import nidaqmx.system
import time
import matplotlib.pyplot as plt
import pandas as pd



def read_daq(sample_rate, duration,inputrange = 10 ):
    """
    Initiates a virtual voltage channel from the ai0 channel (input 15) from the nidaq
    USB 6211. For a given duration, sample rate and input range (voltage range) the
    voltage is read and returned as data.

    args:
        sample_rate(int): sample rate in hertz
        duration (int): How long the data is read for in seconds
        inputrange (int): The range of voltage that is read from the device
    returns:
        data (array): voltage values
        t (array): numpy array of times
    """
    system = nidaqmx.system.System.local()
    for device in system.devices:
        device = str(device)
        dev_index = device.find("=Dev")+1
        #Assuming connected device is named "Devx" x = 1-9
        dev = device[dev_index:dev_index+4]
        print(dev)


    samples_per_channel = int(sample_rate * duration)
    threshold = 3.5
    ts = 1/sample_rate
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("{}/ai0".format(dev),terminal_config 😕
                                             TerminalConfiguration.RSE,\
                                             min_val = -inputrange,\
                                             max_val = inputrange)
        #Referenced Single Ended (RSE) Terminal Configuration Measures
        #the potential difference between the AI and the AI GND


        start = time.time()
        task.timing.cfg_samp_clk_timing(sample_rate, source = " "\
                                                ,sample_mode = AcquisitionType.FINITE\
                                                ,samps_per_chan = samples_per_channel)
        data =  task.read(samples_per_channel)
        data = np.array(data)
        print(time.time()-start)
    t = np.linspace(0,duration, samples_per_channel)
    return data, t


def rising_edge(data, time, edgeskip = False):
    """
    Finds large data in the detected voltage to find passes of the pendel.
    args:
        data (array): the voltage readings from the daq session
        time (np array): time values with same size as data
    returns:
        rising_edge(np array): array of indices that indicate a rising edge
        periods (np array): the time betweet each pass
        mean_period (float): np.mean of periods
    """
    threshold = 0.35 #voltage which when exceeded constitutes a reading
    edge_index = np.argwhere((data[:-1] < threshold) & (data[1:] > threshold))

    try:
        edgeskip = sys.argv[1]
    except:
        edgeskip = input('skriv inn 1 for Tid og Frekvens, og 0 for Masse og Kraft')

    if edgeskip:
        print('Tilpasset Masse og kraft')
    else:
        print('Tilpasset Tid og frekvens')
    rising_edge_index = edge_index[::1+edgeskip]   #removing falling edge
    period = np.zeros(len(rising_edge_index)-1)
    #there are only len(rising_edge_index) - 1 periods

    for i in range(len(rising_edge_index)-1):
        period[i] = t[rising_edge_index[i+1]] - t[rising_edge_index[i]]

    mean_period = np.mean(period)
    std_mean = np.std(period)/np.sqrt(len(period))
    return rising_edge_index, period, mean_period, std_mean


def plot_data(data, time, rising_edge_index, period):
    """
    plots data
    """
    plt.style.use("seaborn")
    plt.plot(time, data)
    plt.plot(time[rising_edge_index], data[rising_edge_index], 'o', label = "Period")
    plt.xlabel('time [s]')
    plt.ylabel('Voltage')
    plt.legend()
    plt.show()
    plt.scatter(time[rising_edge_index[1:]], period, c = "g")
    plt.xlabel('time [s]')
    plt.ylabel('Period [s]')
    plt.title('Period vs time')
    plt.show()

if _name_ == "_main_":
    duration = 10
    sample_rate = 25000
    samples_per_channel = int(sample_rate * duration)
    inputrange = 10

    data, t = read_daq(sample_rate, duration, inputrange)
    df = pd.DataFrame(data)
    df.to_csv("pendel_data.csv")
    np.save("pendel_data.npy",data)

    rising_edge_index, period, mean_period, std_mean = rising_edge(data, t)
    print(period,mean_period,std_mean)
    plot_data(data, t, rising_edge_index, period)
