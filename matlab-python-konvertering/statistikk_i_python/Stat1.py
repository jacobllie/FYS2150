import matplotlib.pyplot as plt
import numpy as np
import random

def histogram(x,tittel,normalisering = False):
    """
    Et histogram teller antall hendelser. X aksen er hendelsen f.eks. om du har
    kastet mynt eller krone. Y aksen er hvor mange ganger du har fått enten mynt eller krone.
    """
    bin_count = int(np.ceil(np.log2(len(x)) + 1))  #Sturge's regel
    plt.figure(figsize=(14,7)) # Make it 14x7 inch
    plt.style.use('seaborn-whitegrid') # nice and clean grid
    plt.hist(x, bins=bin_count,density = normalisering, facecolor = '#2ab0ff', edgecolor='#169acf', linewidth=0.5)
    plt.title(tittel)
    plt.xlabel('Bins')
    plt.ylabel('Values')

n = 1
X = 10
sigma = 1
x = sigma * np.random.randn(int(n)) + X

print(x)

"""
Èn måling sier oss lite,
og vi kan ikke, uten detaljert
informasjon om måleinstrumentet, si
f.eks om det er mye støy i målingene.
"""

"""
For å gjøre dette, trenger vi å vite fordelingen til målingene.
Denne kan tilnærmes med histogrammet til mange målinger.
"""
n = 50
x = sigma * np.random.randn(int(n)) + X

histogram(x,"{} målinger".format(n))
plt.show()

"""
Man kan få en bedre presentasjon av normalfordelingen, dersom man øker antall
"målinger", og flere tall i spekteret rundt gjennomsnittet blir representert.
"""

n = 50000
x = sigma * np.random.randn(int(n)) + X
histogram(x,"{} målinger".format(n))
plt.show()

"""
Når histogrammet teller opp antall ganger den har fått 9, 10, 9.5 osv. Så gir
den et visuelt bilde av sannsynlighetsfordelingen, men det er ikke en sannsynlighetsfordeling.
For å oppnå det, normaliserer vi den slik at arealet under grafen blir 1.
"""


normalisering  = True

histogram(x,"{} målinger med normalisering".format(n),normalisering)
#plt.legend("Målinger")
#plt.show()

"""
Dette gir en veldig god tilnærming av normalfordelingen.
Merk deg at den er fortsatt ikke perfekt, ettersom antall målinger n, ikke er uendelig.
Men den kan fortsatt brukes som en teoretisk benchmark.
"""


"""
Legger en teoretisk fordeling over målingene og ser at det stemmer godt med normalfordelingen.
"""
sigma = 1
X = 10
x = np.linspace(X-10,X+10,1000)
theoretical_norm = 1/(sigma*np.sqrt(2*np.pi))*np.exp(-1/2*((x-X)/sigma)**2)

plt.plot(x,theoretical_norm)
plt.legend(["Teoretisk fordeling","Målinger"])
plt.show()
