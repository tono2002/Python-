import time
import pyautogui


print("BIENVENIDO AL PASADOR DE HISTORIAS")
print("-----------------------------------")
print("Iniciando...")

time.sleep(8) #Tiempo para poner instagram en pantalla completa

pyautogui.moveTo(1361, 680, 1)
time.sleep(2)

n = 200
while n > 0:
    pyautogui.click()
    n = n - 1
    



