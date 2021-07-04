# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:46:36 2020

@author: salaz
"""

from matplotlib import pyplot as plt
import numpy as np
import scipy as sig
pi=np.pi
plt.close('all')
#filtro que va desde 0 hasta M
def pasabajas(window,wc, M):
    pi=np.pi
    filtro=np.zeros(M+1)
    n1=np.arange(0,M/2,1)
    n2=np.arange((M/2)+1,M+1,1)
    filtro[0:int(M/2)]=np.sin(wc*(n1-M/2))/(pi*(n1-M/2));
    filtro[int(M/2)+1:M+1]=np.sin(wc*(n2-M/2))/(pi*(n2-M/2));
    filtro[int(M/2)]=wc/pi
    
    if window=='hanning':
        w=np.hanning(M+1)
    else:
        if window=='hamming':
            w=np.hamming(M+1)
        else:
            if window=='rectangular':
                w=np.ones(M+1)
            else:
                if window=='blackman':
                    w=np.blackman(M+1)
                else:
                    if window=='barlett':
                        w=np.bartlett(M+1)
    filtro=w*filtro            
    return filtro

filtro=pasabajas('blackman',pi/3, 120)

Fm=1000;
t=np.arange(0,1,1/Fm);
f1=np.sin((2*pi*10)*t);
f2=np.sin((2*pi*400)*t);
f=f1+f2;
plt.figure()
plt.plot(f);

filtered=np.convolve(filtro,f)
plt.figure()
plt.plot(filtered)
plt.figure()
dom=np.arange(-pi,pi,2*pi/(1024));
plt.plot(dom,np.abs(np.fft.fftshift(sig.fft(f,1024))));
plt.figure()
plt.plot(dom,np.abs(np.fft.fftshift(sig.fft(filtered,1024))));
plt.figure()
plt.stem(filtro)
fft_filtro=np.fft.fftshift(sig.fft(filtro,1024))
delta=(2*pi)/(len(fft_filtro))
dom=np.arange(-pi,pi,delta)
plt.figure()
plt.plot(dom, 20*np.log10(np.abs(fft_filtro)))
#plt.xlim([-pi,pi])
#plt.ylim([np.min(np.abs(fft_filtro)),np.max(np.abs(fft_filtro))])
