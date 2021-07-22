import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("terminal_hastighet_rdata.dat")
r = np.log(data[:,0])
theory1 = np.log(data[:,1])
theory2 = np.log(data[:,2])
theory3 = np.log(data[:,3])

plt.style.use("seaborn")
plt.plot(r,theory1,"o",label="Teori 1")
plt.plot(r,theory2,"o",label="Teori 2")
plt.plot(r,theory3,"o",label="Teori 3")
plt.xlabel("Radius [m]")
plt.ylabel("Hastighet [m/s]")


theory1_fit = np.polyfit(r,theory1,1)
theory2_fit = np.polyfit(r,theory2,1)
theory3_fit = np.polyfit(r,theory3,1)

def linear(slope,intercept,x,label):
    print("Tilpasning for {}.".format(label))
    print("{:.4f}x + {:.4f}".format(slope,intercept))
    line = slope*x + intercept
    return line

r_extra = np.linspace(np.min(r),np.max(r),100)   #using this to interpolate


plt.plot(r_extra,linear(theory1_fit[0],theory1_fit[1],r_extra,"Teori 1"))
plt.plot(r_extra,linear(theory2_fit[0],theory2_fit[1],r_extra,"Teori 2"))
plt.plot(r_extra,linear(theory3_fit[0],theory3_fit[1],r_extra,"Teori 3"))
plt.legend()
plt.show()
