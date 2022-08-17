import time
import pyautogui

# NOTA: Los valores de la posición x e y no son iguales para todos los dispositivos

print("BIENVENIDO AL PASADOR DE HISTORIAS")
print("-----------------------------------")
print("Iniciando...")

time.sleep(8) # Tiempo para poner instagram en pantalla completa

pyautogui.moveTo(1361, 680, 1) # Ratón se mueve a la posición donde se encuentra el botón de pasar historia (>)
time.sleep(2)

n = 200 # Número de historias que se desean pasar
while n > 0:
    pyautogui.click()
    n = n - 1
    



