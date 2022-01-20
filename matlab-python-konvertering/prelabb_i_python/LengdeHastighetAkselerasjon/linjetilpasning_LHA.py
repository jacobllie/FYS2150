import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
a = 3.5
b = 5.0
x = np.arange(0,10,0.1)
y = a + b*x + (np.random.randn(len(x)))
plt.style.use("seaborn")
plt.plot(x,y,"*",label="data")

fit = stats.linregress(x,y)

m = fit.slope
c = fit.intercept

plt.plot(x,m*x+c,label="linfit:{:.3f} x + {:.3f}".format(m,c))
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()


#standardfeil i estimatene

dm = fit.stderr
dc = fit.intercept_stderr

#R2 sier not om goodness of fit. 0 er veldig dårlig, 1 er veldig bra.
R2 = fit.rvalue**2

print("SE(m) = {:.3f}".format(dm))
print("SE(c) = {:.3f}".format(dc))
print("R2 = {:.3f}".format(R2))
