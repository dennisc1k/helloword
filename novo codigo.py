import tkinter as tk
from tkinter import ttk

# Criar a janela principal
root = tk.Tk()
root.title("Hello World")
root.geometry("300x150")

# Criar um rótulo usando ttk
label = ttk.Label(root, text="Hello, World!", font=("Comicsans", 16))
label.pack(pady=20)

# Criar um botão para fechar a janela
botao = ttk.Button(root, text="Fechar", command=root.destroy)
botao.pack()

# Iniciar o loop da interface
root.mainloop()


