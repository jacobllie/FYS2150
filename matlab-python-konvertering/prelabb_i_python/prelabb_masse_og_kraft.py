import matplotlib.pyplot as plt
import numpy as np


def regression(x,y):
    """
    Funksjon for å lage ekstrapoleringspunkter fra lineærtilpasningen
    """
    n = len(x)
    D = np.sum(x**2)-1/n*np.sum(x)**2
    E = np.sum(x*y)-1/n*np.sum(x)*np.sum(y)
    F = np.sum(y**2)-1/n*np.sum(y)**2

    x_bar = 1/n*np.sum(x)
    y_bar = 1/n*np.sum(y)

    m = E/D
    c = y_bar - m*x_bar
    d = y - m*x -c

    dm = np.sqrt(1/(n-2) *(D*F - E**2)/D**2)
    dc = np.sqrt(1/(n-2)*(D/n+x_bar**2)*(D*F - E**2)/D**2)
    return m, dm, c, dc

def linear(m,c,x):
    """
    Funksjon for å lage ekstrapoleringspunkter fra lineærtilpasningen
    """
    #print("{:.4}x + {:4}".format(m,c))
    line = m*x + c
    return line

if __name__ == "__main__":

    data = np.loadtxt("maalinger_deformasjon.dat")
    mass = data[:,0]
    d = data[:,1]

    A,dA,c,dc = regression(mass,d)

    print("-----------------")
    print("Least squares fit:")
    x = np.linspace(np.min(mass),np.max(mass),100)
    plt.style.use("ggplot")
    plt.plot(mass,d,"o",label="Data")
    plt.title("Datapunkter med tilpasning")
    plt.xlabel("Masse [kg]")
    plt.ylabel("Utslag [mm]")
    plt.plot(x,linear(A,c,x),label="fit")
    plt.legend()
    plt.show()

    print("Slope = m = {:.4} dm = {:.4}\nIntercept = c = {:.4}\
          dc = {:.4}".format(A,dA,c,dc))
    print("-----------------")


    tau=np.array([4.12, 4.04, 4.16, 4.02, 4.03, 4.04, 3.89, 4.2, 4.12, 4.05])
    dtau = np.std(tau)

    print("STD(tau) = {:.4f} ".format(dtau))


    def k(tau,mass):
        return 4*mass*(np.pi/(np.mean(tau)))**2

    print("Estimated spring constant {:.4}".format(k(tau,2)))

    s_dtau = dtau/np.sqrt(len(tau))
    print("Estimated SE(tau) {:.5}".format(s_dtau))

    def dm(s_dtau,m,tau_mean):
        return 2*m*s_dtau/tau_mean

    def dm_alt(tau,s_dtau,k):
        return tau/(2*np.pi**2)*k*s_dtau

    print("dm using squires page 29.")
    print("dm = {:.5}".format(dm(s_dtau,2,np.mean(tau))*1000))


    print("dm using formula for pendulum:")
    print("dm = {:.5}".format(dm_alt(np.mean(tau),s_dtau,k(tau,2))*1e3))
