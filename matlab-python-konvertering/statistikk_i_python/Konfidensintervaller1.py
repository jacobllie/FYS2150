import numpy as np
import random


random.seed(2150)

def confidence_generator(N,print_=False):

    #Simulerer normalfordelte data med forventningsverdi 10 og standardavvik 1

    norm = sigma * np.random.randn(N) + X
    xMean = np.mean(norm)
    mean_stderr = np.std(norm)/np.sqrt(N) #finner standard feil i gjennomsnittet

    """
    Finner lavre og øvre grense for konfidensintervallet, med en 95% sannsynlighet
    for at gjennomsnittet ligger innenfor konfidensintervallet.
    Derfor multipliserer vi standard feilen med 1.96.
    Se mer om konfidensintervaller i kompendiet.
    """
    lower_ci = xMean - 1.96 * mean_stderr
    upper_ci = xMean + 1.96 * mean_stderr
    if print_ == True:
        print("\n For N = {}".format(N))
        print("xMean = {:.4}".format(xMean))
        print("Konfidensintervallet er mellom [{:.4},{:.4}]".format(lower_ci,upper_ci))
    return lower_ci,upper_ci




"""
Vi ønsker å verifisere at vi får et gjennomsnitt som faktisk ligger i konfidensintervallet
95% av gangene.
"""
sigma = 1
X = 10
reps = 5000
sum = 0
n = 10
for i in range(reps):
    xSim = sigma*np.random.randn(n) + X
    xMean = np.mean(xSim)
    lower_ci_sim , upper_ci_sim = confidence_generator(n)
    if lower_ci_sim <= 10 <= upper_ci_sim:
        sum += 1
print("\n {}% av gangene, er gjennomsnittet innenfor konfidensintervallet".format(sum/reps*100))



"""
Vi ser at det ikke stemmer. Gjennomsnittet er ikke innenfor konfidensintervallet 95% av gangene.
Problemet er at N ikke er stor nok. Det som skjer da er at antakelsen om at sigma = std/sqrt(n) ikke
stemmer, og vi får ikke 95% dekningsgrad.
Vi prøver igjen, men med N = 50
"""

sum = 0
n = 100
for i in range(reps):
    xSim = sigma*np.random.randn(n) + X
    lower_ci_sim , upper_ci_sim = confidence_generator(n)
    if lower_ci_sim <= 10 <= upper_ci_sim:
        sum += 1
print("\n {}% av gangene, er gjennomsnittet innenfor konfidensintervallet".format(sum/reps*100))


"""
Her ser vi at den estimerte verdien 10 nesten ligger innenfor 95 % av gangene, og konfidensintervallet stemmer.
Da kan vi si at n = 100 er tilstrekkelig for å kunne si at sigma = standard error
"""


"""
Hver gang vi gjør en rep (i.e. trekker n tall fra randn) så telles det som ett
eksperiment, og  hver gang man henter ut en sample, så må man ha et nytt konfidensintervall.

Det gir også mening å se at det er 10 som skal ligge innenfor lower_ci_sim og upper_ci_sim, fordi
det er den sanne population parameter.
"""
