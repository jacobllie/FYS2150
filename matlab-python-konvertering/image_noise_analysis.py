import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl


def image_noise_analysis(filename):
    ny = 100;
    nx = 100;
    im1 = cv2.imread(filename)
    im1 = np.flip(im1, axis=2)

    print(im1)
    #plotter bildet

    Ny = im1.shape[0]
    Nx = im1.shape[1]
    print(Ny, Nx)
    cc = [round(Nx/2), round(Ny/2)]

    fig, ax = plt.subplots()
    ax.imshow(im1)
    #lager et rektangulært fokuspunkt
    rect = mpl.patches.Rectangle((cc[0] - round(nx/2),cc[1] - round(ny/2)), nx,ny,
                                 linewidth=1, edgecolor='r', facecolor=None, fill = False)
    plt.plot(cc[0], cc[1], 'r+')
    ax.add_patch(rect)
    plt.show()

    #henter ut grønn channel verdier
    im2 = im1[:,:,2]
    print(np.shape(im1))



    im2 = im1[cc[1] - round(ny/2):cc[1]+round(ny/2)-1, cc[0]-round(nx/2):cc[0] + round(nx/2)-1,2]
    m = np.mean(im2[:])
    im2 = im2.astype('int')
    print(type(im2[0,0]))
    fig2, ax2 = plt.subplots()
    ax2.imshow(im2)
    plt.show()

    #forskjell i intensitet mellom naboer
    im3 = im2[:,1:-2] - im2[:,2:-1]
    #varianse
    v = np.var(im3[:])
    fig3, ax3 = plt.subplots()
    ax3.imshow(im3)
    plt.show()





