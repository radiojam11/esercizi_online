"""
Esercizio 011: A ciascuno il suo
Scrivi una funzione che data in ingresso una lista A contenente n parole, 
restituisca in output una lista B di interi che rappresentano la lunghezza delle parole contenute in A.
"""

def lung_parola(lista):
    lista2=[]
    for el in lista:
        lista2.append(len(el))
    print(lista2)

lung_parola(["mamma","pino","mare","supercalifragili"])

