import tkinter as tk
from tkinter import ttk
import random


def pobieranieDanych():
    lista = []
    with open('bazaDanych.txt', 'r') as file:
        for line in file:
            lista.append(list(map(int, line.strip())))
    print('pobieranieDanych: ', lista)
    return lista


def generowanieDanych(listaP):
    lista2 = []
    if len(listaP) < 100:
        for ii in listaP:
            lista2.append(ii)
        print('lista2, początek: ', lista2)
        for iii in range(9):
            print(iii)
            for lista in listaP:
                nowaLista = lista.copy()
                for ii in range(len(lista)):
                    x = random.randint(1, 100)
                    if lista[ii] == 1 and ii - 1 >= 0 and (ii % 5) != 0 and x <= 2:
                        nowaLista[ii] = 0
                        nowaLista[ii - 1] = 1
                    elif lista[ii] == 1 and ii - 5 >= 0 and x <= 4:
                        nowaLista[ii] = 0
                        nowaLista[ii - 5] = 1
                    elif lista[ii] == 1 and ii + 1 < len(lista) and (ii + 1) % 5 != 0 and x <= 6:
                        nowaLista[ii] = 0
                        nowaLista[ii + 1] = 1
                    elif lista[ii] == 1 and ii + 5 < len(lista) and x <= 8:
                        nowaLista[ii] = 0
                        nowaLista[ii + 5] = 1
                lista2.append(nowaLista)
        print(lista2)
        print(len(lista2))
        with open("bazaDanych.txt", "w+") as file:
            for wiersz in lista2:
                file.write("".join(map(str, wiersz)) + "\n")


def rysujTablice(dana, frame):
    for wie in range(7):
        for kol in range(5):
            wartosc = dana[wie * 5 + kol]
            kolor = "black" if wartosc == 1 else "white"
            tk.Label(frame, width=2, height=1, bg=kolor, borderwidth=0.5, relief="solid").grid(row=wie, column=kol)


generowanieDanych(pobieranieDanych())

root = tk.Tk()
root.title("Wyświetlanie tablic")
root.geometry("1050x800")

ramka_glowna = tk.Frame(root)
ramka_glowna.pack(fill="both", expand=1)

ramka_tablic = tk.Canvas(ramka_glowna)
ramka_tablic.pack(side="left", fill="both", expand=1)
ramka_tablic.bind('<MouseWheel>', lambda event: ramka_tablic.yview_scroll(int(event.delta / 60), "units"))

suwak_pionowy = ttk.Scrollbar(ramka_glowna, orient="vertical", command=ramka_tablic.yview)
suwak_pionowy.pack(side="right", fill="y")

ramka_tablic.configure(yscrollcommand=suwak_pionowy.set)
ramka_tablic.bind('<Configure>', lambda e: ramka_tablic.configure(scrollregion=ramka_tablic.bbox("all")))

ramka_zawartosci = tk.Frame(ramka_tablic)
ramka_tablic.create_window((0, 0), window=ramka_zawartosci, anchor="nw")

tablica = []
with open('bazaDanych.txt', 'r') as file:
    for line in file:
        tablica.append(list(map(int, line.strip())))
        '''
        i=0
        while i <len(line):
            print(line[i:i+5])
            i+=5
        '''
for row in range(10):
    for column in range(10):
        ramka_tablica = tk.Frame(ramka_zawartosci, borderwidth=1, relief="solid")
        rysujTablice(tablica[row * 10 + column], ramka_tablica)
        ramka_tablica.grid(row=row, column=column, padx=5, pady=5)

root.mainloop()
