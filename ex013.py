"""
Esercizio 013: Solamente per Soci
Scrivi una funzione a cui vengono passati come parametro
 un elemento e una lista di elementi, e che ti dica in output
  se l'elemento passato sia presente o meno nella lista.

Qualora l'elemento sia presente nella lista, la funzione dovrà 
inoltre comunicarci l'indice dell'elemento.

"""

def controlla(elem, lista):
    if elem in lista:
        print(f"elemento {elem} e' presente nella lista")
        return lista.index(elem)

print(controlla("mario", ["pino", "mario", "beppe"]))
