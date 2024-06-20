import tkinter as tk
from tkinter import messagebox, filedialog
from threading import Thread
from automation import processar_empresas

def start_automation():
    periodo = periodo_entry.get()
    if not periodo:
        messagebox.showwarning("Entrada Inválida", "Por favor, preencha o campo de período.")
        return
    
    csv_path = filedialog.askopenfilename(title="Selecione o arquivo CSV", filetypes=[("CSV files", "*.csv")])
    if not csv_path:
        messagebox.showwarning("Arquivo Não Selecionado", "Por favor, selecione um arquivo CSV.")
        return
    
    thread = Thread(target=processar_empresas, args=(csv_path, periodo))
    thread.start()

app = tk.Tk()
app.title("Automação ECF")

tk.Label(app, text="Período:").grid(row=0)

periodo_entry = tk.Entry(app)
periodo_entry.grid(row=0, column=1)

tk.Button(app, text="Iniciar", command=start_automation).grid(row=1, column=0, columnspan=2)

app.mainloop()
