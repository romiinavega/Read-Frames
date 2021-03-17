import wave 
import numpy as np
import matplotlib.pyplot as plt

#Cargar archivo wav en la variable 

goodmorning = wave.open('good-morningMan.wav', 'r')
goodafternoon = wave.open('good-afternoon.wav', 'r')

#Obtener todos los frames del objeto wave
frames = goodmorning.readframes(-1)
frames_ga = goodafternoon.readframes(-1)

#Mostrar el resultado de frames
#print(frames [:10])

ondaconvertida = np.frombuffer(frames, dtype='int16')
ondaconvertida_ga = np.frombuffer(frames_ga, dtype='int16')
#print(ondaconvertida [:10])

framerate_gm = goodmorning.getframerate()
framerate_ga = goodafternoon.getframerate()

print(framerate_gm)
print(framerate_ga)

time_gm = np.linspace(start = 0, stop = len(ondaconvertida ) /framerate_gm, num= len(ondaconvertida))
time_ga = np.linspace(start = 0, stop = len(ondaconvertida_ga ) /framerate_ga, num= len(ondaconvertida_ga))

print(time_gm[:10])
print(time_ga[:10])

#Generación de la gráfica

plt.title('Good morning vs Good afternoon')

#etiquetas de los ojos
plt.xlabel('Tiempo segundos')
plt.ylabel('Amplitud')

#Agregar la informacion
plt.plot(time_gm, ondaconvertida, label='Good morning')
plt.plot(time_ga, ondaconvertida_ga, label='Good afternoon', alpha = 0.5)

plt.legend()
plt.show()