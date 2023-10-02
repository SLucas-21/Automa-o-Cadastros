#ABRINDO CRE
import pyautogui
from time import sleep
pyautogui.PAUSE = 0.5

pyautogui.press('win')
pyautogui.write('Edge')
pyautogui.press('enter')
sleep(3)
for c in range(1, 11):
    pyautogui.press('tab')
for n in range(1, 4):
    pyautogui.press('Right')
pyautogui.press('enter')
sleep(3)
for c in range(1, 5):
    pyautogui.press('tab')
pyautogui.press('enter')
#PESQUISAR DC E ABRIR CADASTRO DE PRODUÇÃO:
