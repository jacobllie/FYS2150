import numpy as np
import matplotlib.pyplot as plt
#setter opp skjerm med spalter
n = 1024
screen = np.zeros((n,n)) #genererer skjerm med 0 gjennomsiktighet
middle = n//2
n_slits = 10 #antall spalter
slit_width = 5 #enkeltspalte bredde
slit_dist = 2*slit_width #avstand mellom spalter
slit_length = 100 #må være partall

#legg til to spalter i midten av skjermen


first_slit = middle - n_slits*(slit_dist+slit_width)//2


"""
    Først plasserer vi oss ved den første spalten hvor slit = 0.
    Så må vi traversere fra toppen av spalten screen[middle + slit_length//2],
    ned til bunnen screen[middle - slit_length//2]. Samtidig som vi beveger oss fra venstre
    av spalten screen[][middle + slit_pos] til høyre screen[][middle + slit_pos slit_width]. Og setter alle
    disse verdiene til 1.
"""


for slit in range(n_slits):
    slit_pos = (slit)*(slit_dist)
    screen[middle - slit_length//2:middle + slit_length//2,\
          first_slit + slit_pos:first_slit + slit_pos +  slit_width] = 1

#plt.subplot(1,2,1,sharey="all")
#plt.title("Diffraction screen")
#plt.imshow(screen,cmap="gray")

#Skal nå gjøre en fourier transformasjon på skjermen for å få diffraksjonsmønsteret
#vi er bare interessert i den reelle delen av signalet, og skifter hele matrisen slik at 0
#kommer i midten.

pattern = np.fft.fftshift(np.abs(np.fft.fft2(screen)))


fig, axs = plt.subplots(1,2, sharex=True, sharey=True,squeeze=True)
(ax1,ax2) = axs
plt.style.use("seaborn")
plt.tight_layout()
ax1.set_title("Diffraction screen")
ax2.set_title("Diffraction pattern")
ax1.imshow(screen,cmap="gray")
ax2.imshow(pattern,cmap="magma")

plt.show()
