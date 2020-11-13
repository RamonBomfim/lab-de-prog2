import tkinter as tk


def calculateImc():
    peso = float(pesoEntry.get())
    altura = float(alturaEntry.get())
    imc = peso / (altura * altura)
    tk.Label(gui, text=f"Seu IMC é {imc:.2f}").grid(row=4, column=1)


gui = tk.Tk()

gui.title("Entrada de dados")

tk.Label(gui, text="Peso").grid(row=0)
tk.Label(gui, text="Altura").grid(row=1)

imc = tk.Button(gui, text="IMC", command=calculateImc)

pesoEntry = tk.Entry(gui)
alturaEntry = tk.Entry(gui)

pesoEntry.grid(row=0, column=1)
alturaEntry.grid(row=1, column=1)
imc.grid(row=2, column=1)

gui.mainloop()
