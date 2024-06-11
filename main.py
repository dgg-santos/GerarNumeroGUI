import tkinter as tk
import random

class GeradorNumeroDaSorte:
  def __init__(self, root):
    self.root = root
    self.root.title("Gerador Numero Da Sorte") 
    self.root.geometry("300x200")
    
    self.numero_label = tk.Label(root, text="")
    self.numero_label.pack(pady=30)

    self.gerar_button = tk.Button(root, text="Gerar Numero Na Sorte", command=self.gerar_numero)
    self.gerar_button.pack()

  def gerar_numero(self):
    numero_sorte = random.randint(1, 100)
    self.numero_label.config(text=f"Seu Numero da sorte é: {numero_sorte}")

if __name__ == "__main__":
  root = tk.Tk()
  app = GeradorNumeroDaSorte(root)
  root.mainloop()