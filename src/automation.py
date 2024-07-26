import pyautogui
import time
import pandas as pd
import shutil
import os
import logging
from tkinter import Tk, filedialog, simpledialog, messagebox
from socketio import Client

# logging
logging.basicConfig(filename='automacao.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

sio = Client()
sio.connect('http://localhost:5000')

def log_event(message):
    logging.info(message)
    sio.emit('log_update', {'message': message})

def log_error(message):
    logging.error(message)
    sio.emit('log_update', {'message': message})

def take_screenshot(filename):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    log_event(f"Screenshot salva como {filename}")

def move_files(source_folder, destination_folder):
    try:
        files = os.listdir(source_folder)
        for file in files:
            shutil.move(os.path.join(source_folder, file), destination_folder)
        log_event(f"Arquivos movidos de {source_folder} para {destination_folder}")
    except Exception as e:
        log_error(f"Erro ao mover arquivos: {e}")
        take_screenshot('erro_mover_arquivos.png')

def select_csv_file():
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        title="Selecione o arquivo CSV",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    return file_path

def select_folder(title):
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title=title)
    return folder_path

def get_sleep_multiplier():
    root = Tk()
    root.withdraw()
    multiplier = simpledialog.askfloat(
        "Multiplicador de Tempo",
        "Informe o multiplicador para time.sleep e pyautogui.PAUSE:",
        minvalue=0.1, maxvalue=10.0
    )
    return multiplier

# Mostrar mensagem informativa sobre a resolução
def show_resolution_message():
    root = Tk()
    root.withdraw()
    messagebox.showinfo("Resolução Padrão", "Resolução padrão: 1366 x 768")

# Selecionar o arquivo CSV
show_resolution_message()
tabela_path = select_csv_file()
if not tabela_path:
    log_error("Nenhum arquivo CSV selecionado")
    raise Exception("Nenhum arquivo CSV selecionado")

# Selecionar a pasta source_folder
source_folder = select_folder("Selecione a pasta de origem (source_folder)")
if not source_folder:
    log_error("Nenhuma pasta de origem selecionada")
    raise Exception("Nenhuma pasta de origem selecionada")

# Selecionar a pasta destination_folder
destination_folder = select_folder("Selecione a pasta de destino (destination_folder)")
if not destination_folder:
    log_error("Nenhuma pasta de destino selecionada")
    raise Exception("Nenhuma pasta de destino selecionada")

# Obter o multiplicador de tempo
sleep_multiplier = get_sleep_multiplier()
if sleep_multiplier is None:
    log_error("Multiplicador de tempo não foi definido")
    raise Exception("Multiplicador de tempo não foi definido")

# Configuração de pausa para o PyAutoGUI
pyautogui.PAUSE = 0.60 * sleep_multiplier

# Carregar a tabela
try:
    tabela = pd.read_csv(tabela_path)
    log_event(f"Tabela carregada de {tabela_path}")
except FileNotFoundError:
    log_error(f"Tabela não encontrada em {tabela_path}")
    take_screenshot('erro_carregar_tabela.png')
    raise

def automate_process():
    for linha in tabela.index:
        try:
            pyautogui.click(x=28, y=34)
            pyautogui.click(x=76, y=77)
            pyautogui.click(x=448, y=266)
            pyautogui.press('enter')
            pyautogui.click(x=516, y=266)  # 1 arquivo
            pyautogui.press('enter')
            pyautogui.click(x=640, y=533)  # ok
            time.sleep(15 * sleep_multiplier)
            pyautogui.click(x=639, y=443)
            pyautogui.click(x=670, y=444)
            time.sleep(15 * sleep_multiplier)
            pyautogui.click(x=675, y=387)

            pyautogui.click(x=728, y=100)
            pyautogui.click(x=772, y=454)
            pyautogui.click(x=834, y=510)
            time.sleep(5 * sleep_multiplier)

            pyautogui.click(x=645, y=393)
            pyautogui.click(x=678, y=388)
            pyautogui.click(x=880, y=463)
            time.sleep(5 * sleep_multiplier)

            pyautogui.click(x=447, y=312)
            pyautogui.click(x=643, y=507)
            pyautogui.click(x=510, y=326)
            pyautogui.click(x=897, y=494)
            pyautogui.click(x=682, y=392)
            pyautogui.click(x=732, y=391)
            time.sleep(5 * sleep_multiplier)

            # Reassina
            pyautogui.click(x=890, y=458)
            pyautogui.click(x=447, y=309)
            pyautogui.click(x=641, y=507)
            pyautogui.click(x=577, y=326)
            pyautogui.click(x=902, y=500)
            pyautogui.click(x=683, y=395)
            time.sleep(5 * sleep_multiplier)

            # Transmissão
            pyautogui.click(x=983, y=459)
            pyautogui.click(x=451, y=293)
            pyautogui.click(x=650, y=561)
            time.sleep(20 * sleep_multiplier)

            # Lixo
            pyautogui.click(x=724, y=561)

            pyautogui.click(x=198, y=175)
            pyautogui.click(x=67, y=190)
            pyautogui.click(x=190, y=208)
            pyautogui.click(x=82, y=64)
            pyautogui.click(x=636, y=395)
            pyautogui.click(x=689, y=394)
            time.sleep(10 * sleep_multiplier)

            log_event(f"Processo para a linha {linha} concluído com sucesso")

        except Exception as e:
            log_error(f"Erro ao processar linha {linha}: {e}")
            take_screenshot(f'erro_linha_{linha}.png')

    # Mover arquivos
    move_files(source_folder, destination_folder)

if __name__ == "__main__":
    automate_process()
    sio.disconnect()
