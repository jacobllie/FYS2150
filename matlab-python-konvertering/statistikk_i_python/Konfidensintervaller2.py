import numpy as np
from scipy import stats

n = 10
"""
Vi ønsker å beregne bruke t-statistikk framfor z-statistikk, hvor antakelsen
om at vi kan tilnærme sigma (det sanne standardavviket), med standard error, ikke stemmer.
"""

sigma = 1
X = 10

norm = sigma*np.random.randn(n) + X
mean = np.mean(norm)
alpha = 0.05 #tilsvarer 95% dekningsgrad

"""
Her bruker vi noe som heter t-distribution, som nettopp er en z-distribution hvor
vi ikke vet hva sigma er.

Skriv mer i jupyter
"""
#CI_coeff = stats.t.ppf(1-(alpha/2),n-1)

CI_coeff = stats.t.ppf(0.95,n-1)
print(CI_coeff)
lower_ci = mean - CI_coeff * np.std(norm)/np.sqrt(n)
upper_ci = mean + CI_coeff * np.std(norm)/np.sqrt(n)

print("Konfidensintervall med t-distribution og N = {} er [{:.2},{:.2}]".format(n,lower_ci,upper_ci))

"""
Nå skal vi undersøke om N = 10 er tilstrekkelig for å få dekningsgrad 95%, med vårt
nye konfidensintervall
"""
reps = 5000
sum = 0
for i in range(reps):
    xSim = sigma*np.random.randn(n) + X
    xMean = np.mean(xSim)
    lower_ci_sim = xMean - CI_coeff * np.std(norm)/np.sqrt(n)
    upper_ci_sim = xMean + CI_coeff * np.std(norm)/np.sqrt(n)
    if lower_ci_sim <= 10 <= upper_ci_sim:
        sum += 1
print("\n {}% av gangene, er gjennomsnittet innenfor konfidensintervallet".format((sum/reps*100)))



"""
Vi er ikke helt der, med ca. 94%, men allikevel et bedre resultat sammenlignet med
z-distribution metoden.
"""
