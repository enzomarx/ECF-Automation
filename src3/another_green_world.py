import pyautogui
import time
import os
import shutil
import tkinter as tk
from tkinter import filedialog

def move_files_to_desktop(folder):
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    files = os.listdir(folder)
    
    if len(files) >= 2:
        shutil.move(os.path.join(folder, files[0]), desktop)
        shutil.move(os.path.join(folder, files[1]), desktop)

def run_script(multiplier, folder):
    def sleep():
        time.sleep(4 * multiplier)

    for _ in range(10):  # Você pode ajustar a quantidade de iterações conforme necessário
        pyautogui.click(x=55, y=65)  # janela de import
        sleep()
        sleep()
        pyautogui.click(x=537, y=265)  # selec primeiro
        sleep()

        pyautogui.click(x=838, y=509)  # abrir
        sleep()

        pyautogui.click(x=642, y=530)  # ok
        sleep()

        pyautogui.click(x=678, y=389)  # ok
        sleep()

        pyautogui.click(x=731, y=446)  # nao
        sleep()

        pyautogui.click(x=668, y=465)  # validar
        sleep()
        time.sleep(30 * multiplier)
        pyautogui.click(x=678, y=394)  # ok
        sleep()

        pyautogui.click(x=503, y=98)  # aaba esquer
        sleep()
        pyautogui.click(x=772, y=448)  # gerar
        sleep()

        pyautogui.click(x=836, y=509)  # botao
        sleep()

        pyautogui.click(x=631, y=393)  # sim
        sleep()

        pyautogui.click(x=682, y=391)  # ok
        sleep()

        pyautogui.click(x=882, y=456)  # assinar
        sleep()

        pyautogui.click(x=650, y=313)  # selec prime
        sleep()
        pyautogui.click(x=640, y=506)  # abrr
        sleep()

        pyautogui.click(x=525, y=327)  # julio
        sleep()
        pyautogui.click(x=896, y=497)  # ok
        sleep()

        pyautogui.click(x=677, y=388)  # ok
        sleep()

        pyautogui.click(x=638, y=392)  # sim
        sleep()

        pyautogui.click(x=571, y=310)  # seg linha
        sleep()
        pyautogui.click(x=645, y=504)  # botao
        sleep()

        pyautogui.click(x=532, y=326)  # julio
        sleep()

        pyautogui.click(x=898, y=501)  # ok
        sleep()
        pyautogui.click(x=692, y=393)  # ok
        sleep()

        pyautogui.click(x=994, y=447)  # transmitir
        sleep()
        pyautogui.click(x=544, y=295)  # selec primeiro
        sleep()

        pyautogui.click(x=644, y=563)  # ok
        sleep()
        time.sleep(10 * multiplier)

        pyautogui.click(x=718, y=553)  # fechar
        sleep()

        pyautogui.click(x=67, y=173)  # excluir
        sleep()
        pyautogui.click(x=64, y=192)  # exc
        sleep()
        pyautogui.click(x=117, y=211)  # exc
        sleep()
        pyautogui.click(x=81, y=63)  # esx
        sleep()
        pyautogui.click(x=647, y=396)  # exc
        sleep()
        pyautogui.click(x=684, y=394)  # ok
        sleep()

        move_files_to_desktop(folder)

def select_folder():
    folder = filedialog.askdirectory()
    folder_label.config(text=folder)
    return folder

def start_script():
    multiplier = float(multiplier_entry.get())
    folder = folder_label.cget("text")
    run_script(multiplier, folder)

# Configuração da interface Tkinter
root = tk.Tk()
root.title("Configuração do Script")

multiplier_label = tk.Label(root, text="Multiplicador de Time Sleep:")
multiplier_label.pack()
multiplier_entry = tk.Entry(root)
multiplier_entry.pack()

folder_label = tk.Label(root, text="Nenhuma pasta selecionada")
folder_label.pack()
folder_button = tk.Button(root, text="Selecionar Pasta", command=select_folder)
folder_button.pack()

start_button = tk.Button(root, text="Iniciar Script", command=start_script)
start_button.pack()

root.mainloop()

