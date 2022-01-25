"""
Program for bruk i Tid og Frekvens og Masse og kraft. Bruker fotodiode og NI USB-6211
Varighet på datainnsamling og frekvens osv må skrives inn manuelt nederst.

Jacob Lie og Anders Bråte v2021.
"""
import sys
import numpy as  np
import matplotlib.pyplot as plt
import nidaqmx
import numpy as  np
from nidaqmx.constants import Edge, AcquisitionType, TerminalConfiguration
import nidaqmx.system
import time



def read_daq(sample_rate, duration,inputrange = 10):
    """
    Initierer en virtuell spennings kanal fram ai0, fra nidaq USB 6211.
    For en gitt opptakstid, sample rate og input range (spennings range),
    spenningen blir avlest og returnert som data

    args:
        sample_rate(int): sample rate i hertz
        duration (int): Hvor lang opptakstid i sekunder
        inputrange (int): hvor stor range i spenning kan nidaq'en forvente.
    returns:
        data (array): spenningsverdier
        t (array): tidsarray
    """
    #henter ut informasjon om hardware som trengs når man kjører nidaqmx API.
    system = nidaqmx.system.System.local()
    for device in system.devices:
        device = str(device)
        dev_index = device.find("=Dev")+1
        #Anntar at device i system.devices er på formen "Device(name=Devx)"
        #hvor x er mellom 1 og 9.
        dev = device[dev_index:dev_index+4]



    samples_per_channel = int(sample_rate * duration)
    with nidaqmx.Task() as task:
        task.ai_channels.add_ai_voltage_chan("{}/ai0".format(dev),\
                                             terminal_config = TerminalConfiguration.RSE,\
                                             min_val = -inputrange,\
                                             max_val = inputrange)
        #Referenced Single Ended (RSE) Terminal Configuration Measures
        #the potential difference between the AI and the AI GND

        print("Data acquisition started...")
        start = time.time()
        task.timing.cfg_samp_clk_timing(sample_rate, source = " "\
                                                ,sample_mode = AcquisitionType.FINITE\
                                                ,samps_per_chan = samples_per_channel)
        data =  task.read(samples_per_channel, timeout = duration + 2)
        data = np.array(data)
        #print(time.time()-start)
    t = np.linspace(0,duration, samples_per_channel)
    return data, t


def rising_edge(data, t):
    """
    Undersøker datasett med spenningsverdier, og sjekker om de inneholder
    rising edge (a.k.a. hvor spenningen går til 0 når pendelen passerer fotodioden.)
    args:
        data (array): the voltage readings from the daq session
        t (np array): time values with same size as data
    returns:
        rising_edge(np array): array of indices that indicate a rising edge
        periods (np array): the time betweet each pass
        mean_period (float): np.mean of periods
    """
    #Dersom spenningen som avleses er under 3.5 V så regnes det som en rising edge.
    threshold = 3.5
    #betingelse for at vi har en rising edge
    edge_index = np.argwhere((data[:-1] < threshold) & (data[1:] > threshold))

    edgeskip = int(input('Skriv inn 1 dersom pendel passerer diode to ganger hver periode, og 0 dersom den passerer èn gang. '))

    if edgeskip:
        print('Tilpasset to passeringer per periode.')
    else:
        print('Tilpasset èn passering per periode.')
    print("------------------------------")
    rising_edge_index = edge_index[::1+edgeskip]   #removing falling edge
    if len(rising_edge_index) == 0:
        print("Ingen fall i spenning ved pendel passering, er alt satt opp riktig?\n")
        sys.exit(1)
    else:
        period = np.zeros(len(rising_edge_index)-1)

    #there are only len(rising_edge_index) - 1 periods

    for i in range(len(rising_edge_index)-1):
        period[i] = t[rising_edge_index[i+1]] - t[rising_edge_index[i]]

    mean_period = np.mean(period)
    std_period = np.std(period)
    return rising_edge_index, period, mean_period, std_period


def plot_data(data, time, rising_edge_index, period):
    """
    plots data
    """
    plt.style.use("seaborn")

    """fig, ax= plt.subplots()

    ax.plot(time,data)

    ax.set_xlabel("tid [s]")
    ax.set_ylabel("Spenning")

    ax2 = ax.twinx()

    ax2.plot(time[rising_edge_index], data[rising_edge_index], 'o', label = "Period")
    #ax2.scatter(time[rising_edge_index[1:]], period, c = "g")

    ax2.set_ylabel("Periode [s]")

    plt.legend()
    plt.show()"""



    plt.subplot(121)

    plt.plot(time, data)
    plt.plot(time[rising_edge_index], data[rising_edge_index], 'o', label = "Period")
    plt.xlabel('tid [s]')
    plt.ylabel('Spenning')
    plt.legend()
    #plt.show()

    plt.subplot(122)
    plt.scatter(time[rising_edge_index[1:]], period, c = "g")
    plt.xlabel('tid [s]')
    plt.ylabel('Periode [s]')
    plt.show()
