import numpy as np
import matplotlib.pyplot as plt

def histogram(x,normalisering = False):
    """
    Et histogram teller antall hendelser. X aksen er hendelsen f.eks. om du har
    kastet mynt eller krone. Y aksen er hvor mange ganger du har fått enten mynt eller krone.
    """
    bin_count = int(np.ceil(np.log2(len(x)) + 1))  #Sturge's regel
    plt.hist(x, bins=bin_count,density = normalisering, facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    plt.xlabel('Bins')
    plt.ylabel('Values')

"""
Vi tar for oss en uniform sannsynlighetsfordeling mellom 0 og 1.
Dvs. At det er like sannsynlig å få 0, 1 og alt mellom.
"""

plt.style.use('seaborn')
num_measurements = np.array([10,1e2,1e3])
for index,n in enumerate(num_measurements):
    x = np.random.uniform(0,1,int(n))
    plt.subplot(1,3,index+1)
    plt.title("{} målinger".format(num_measurements[index]))
    histogram(x)
plt.show()


"""
Vi ser at med flere målinger nærmer det seg den uniforme fordelingen.
Det vi skal se på nå er fordelingen av gjennomsnittene for økende antall målinger.
"""

num_measurements = np.array([2,3,5,200])
reps = 1000
meanSim = np.zeros([4,reps])
for index,n in enumerate(num_measurements):
    meanSim[index] = [np.mean(np.random.uniform(0,1,n)) for j in range(reps)]
    plt.subplot(2,2,index+1)
    plt.title("Gjennomsnitts fordeling n = {}".format(num_measurements[index]))
    histogram(meanSim[index])
plt.xlim(0,1)
plt.show()

"""
Her ser vi at selv om målingene i seg selv ikke er normalfordelt,
så blir fordelingen av gjennomsnittene normalfordelt, og følger dermed sentralgrenseteoremet.
"""

"""
En tydeligere måte å illustrere om målinger er normalfordelt er ved å plotte et QQ plot.
Som sammenligner fordelingens kvantiler med teoretiske kvantiler.
Dersom det er et lineært forhold mellom dem, vil målingene være normalfordelt.
"""


from scipy import stats

for i in range(len(num_measurements)):
    plt.subplot(2,2,i+1)
    stats.probplot(np.random.uniform(0,1,num_measurements[i]),plot = plt)
    plt.title("QQ plot med")
plt.show()

"""
Vi ser i plottene at målingene tatt fra en uniform fordeling ikke er normalfordelt,
ettersom de ikke følger linja.
Men hva om vi lager de samme plottene, med gjennomsnittene i steden.
"""

for i in range(len(num_measurements)):
    plt.subplot(2,2,i+1)
    stats.probplot(meanSim[i],plot = plt)
plt.show()

"""
Her ser vi at fordelingen av gjennomsnittene er normalfordelte, dersom
antall målinger er tilstrekkelig.
"""
