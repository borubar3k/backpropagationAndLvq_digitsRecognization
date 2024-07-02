import tkinter as tk
from tkinter import ttk


def klikniety(indeks):
    if lista[indeks] == 0:
        przyciski[indeks].config(bg="black")
        lista[indeks] = 1
    elif lista[indeks] == 1:
        lista[indeks] = 0
        przyciski[indeks].config(bg="SystemButtonFace")


def zatwierdz():
    wartosc = combobox.get()
    nrLinii = int(wartosc) + 1
    with open("bazaDanych.txt", "r+") as file:
        lines = file.readlines()
        if nrLinii <= len(lines)+1:
            lines[nrLinii - 1] = ''.join(map(str, lista)) + "\n"
            file.seek(0)
            file.writelines(lines)
        else:
            print(f"Numer linii ({nrLinii}) przekracza liczbę dostępnych linii w pliku.")


def wyczysc():
    for row in range(7):
        for column in range(5):
            if lista[row*5+column] == 1:
                lista[row*5+column] = 0
                przyciski[row*5+column].config(bg="SystemButtonFace")


lista = 35*[0]
przyciski = []

root = tk.Tk()
root.title("Dodawanie cyfr")
root.geometry(f"{245}x{450}")
root.resizable(False, False)


for row in range(7):
    for column in range(5):
        button = tk.Button(root, text=f"{(row*5+column)+1}", width=5, height=2, command=lambda idx=row*5+column : klikniety(idx))
        button.grid(row=row, column=column, padx=2, pady=2)
        przyciski.append(button)

options = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
combobox = ttk.Combobox(root, values=options)
combobox.grid(row=8, column=0, columnspan=5, sticky="ew", padx=2, pady=2)

przyciskZatwierdz = tk.Button(root, text="Accept", command=zatwierdz, width=30, height=2)
przyciskZatwierdz.grid(row=9, column=0, columnspan=5, sticky="ew", padx=2, pady=2)

przyciskWyczysc = tk.Button(root, text="Clear", command=wyczysc, width=30, height=2)
przyciskWyczysc.grid(row=10, column=0, columnspan=5, sticky="ew", padx=2, pady=2)

root.mainloop()
