"""
Esercizio 020: Poesia Elettronica
Scrivi una semplice funzione rimario, 
a cui viene passato un elenco di parole come parametro e 
che riceva una parola inserita dall'utente tramite la funzione input.

La funzione rimario dovra confrontare la parola inserita 
dall'utente con quelle presenti nell'elenco passato, alla ricerca di rime,
 intese come parole le cui ultime 3 lettere siano uguali alla parola inserita dall'utente.

Le rime dovranno essere quindi mostrate in output dall'utente.
"""

def rimario(lista):
    parola = input("inserisci parola  -->")
    rima = parola[-3:]
    for el in lista:
        if rima == el[-3:]:
            print(f"{parola}  fa rima con {el}")


rimario({"mario", "armadio", "credenza", "pendenza"})