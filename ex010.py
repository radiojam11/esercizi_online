"""

Esercizio 010: Generatore di Istogrammi
Scrivi una funzione che, data una lista di numeri, fornisce in output un istogramma basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione dovrà produrre questa sequenza:

***

*******

*********

*****

"""

def istogramma(lista):
    for el in lista:
        print("*"*el)
istogramma([3, 7, 9, 5])


