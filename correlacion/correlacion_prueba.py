import pyaudio
import numpy as np
import scipy.io.wavfile as wavfile
import matplotlib.pylab as plt

from playsound import playsound 
import wave



longitud = []

fs, y1 = wavfile.read('/home/angie/Git/python_dsp/principio_fin_palabra/resultado (3).wav')
amax = max(y1)
amin = min(y1)
n = np.array([amax, amin*-1])
amax = max(n)
y1 = y1/amax
fs, y2 = wavfile.read('/home/angie/Git/python_dsp/principio_fin_palabra/resultado (4).wav')
amax = max(y2)
amin = min(y2)
n = np.array([amax, amin*-1])
amax = max(n)
y2 = y2/amax
fs, y3 = wavfile.read('/home/angie/Git/python_dsp/principio_fin_palabra/resultado (5).wav')
amax = max(y3)
amin = min(y3)
n = np.array([amax, amin*-1])
amax = max(n)
y3 = y3/amax


l = len(y1)
longitud.append(l)
l = len(y2)
longitud.append(l)
l = len(y3)
longitud.append(l)


longitud = np.array(longitud)
print(longitud)
ymax = max(longitud)
print(ymax)
print(len(y1))
print(len(y2))
print(len(y3))

if len(y1) < ymax:
    x = ymax - len(y1)
    y1 = np.pad(y1, (0, x), 'constant')
    print(len(y1))

if len(y2) < ymax:
    x = ymax - len(y2)
    y2 = np.pad(y2, (0, x), 'constant')
    print(len(y1))

if len(y3) < ymax:
    x = ymax - len(y3)
    y3 = np.pad(y3, (0, x), 'constant')
    print(len(y1))





a = np.corrcoef(y1,y1)
print(a)
b = np.corrcoef(y1,y2)
print(b)
c = np.corrcoef(y1,y3)
print(c)





