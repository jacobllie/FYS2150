import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import random
def mean(data):
    """
    finner gjennomsnitt
    """
    f = 1/len(data)*np.sum(data)
    return f


def std(data):
    """
    Finner standardavvik
    """
    f = mean(data)
    s = np.sqrt(1/(len(data)-1)*np.sum((data-f)**2))
    return s

def mean_std(data):
    """
    Finner standardavviket i gjennomsnittet
    """
    return std(data)/np.sqrt(len(data))

if __name__ == "__main__":

    #loader inn matlab dataframe
    mat = scipy.io.loadmat('data1.mat')
    data = np.array(mat["data1"])

    """
    Undersøker hvor mange datapunkter som ligger innenfor
    ett standardavvik.
    """
    sigma = std(data)
    mu = mean(data)
    sum = 0
    for i in range(len(data)):
        if mu-sigma < data[i] < mu + sigma:
            sum += 1

    print("Gjennomsnitt = {:.2f}".format(mu))
    print("Standardavvik = {:.2f}".format(sigma))
    print("Standard Error i Gjennomsnitt = {:.2f}".format(sigma/np.sqrt(len(data))))
    print("{:.2f}% av målepunktene ligger innenfor ett standardavvik.".format(sum/len(data)*100))


    """
    Her undersøker vi hvordan gjennomsnitt, standardavvik og standardavviket i
    gjennomsnittet utvikler seg for økende n.
    """

    n = np.array([2,20,40,60,80,100,150,250,500,1000])
    a = 1
    b = 2
    xmid = np.zeros(len(n))
    s = np.zeros(len(n))
    sm = np.zeros(len(n))

    random.seed(1)
    for i in range(len(n)):
        x = a+b*np.random.randn(n[i],1)
        xmid[i] = mean(x)
        s[i] = std(x)
        sm[i] = mean_std(x)

    plt.style.use("seaborn")
    plt.plot(n,xmid,label="Gjennomsnitt")
    plt.plot(n,s,label="Standardavvik")
    plt.plot(n,sm,label="Standardavviket i gjennomsnittet")
    plt.legend()
    plt.show()
