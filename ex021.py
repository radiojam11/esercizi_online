"""
Esercizio 021: La Libreria
Scrivi una funzione "vendi_libri" che:

Controlla se il libro richiesto è presente sugli scaffali 
della libreria
Qualora il libro sia presente, ne decrementa il numero di 
copie (eventualmente rimuovendo il titolo) e ci segnala che 
la vendita ha avuto successo
Se il libro non è disponibile, viene messo in un elenco di 
libri da ordinare e ci viene comunicato che la vendita non 
ha avuto successo
La funzione restituisce valore Booleano True o False in base 
all'esito della vendita.
"""

def vendi(libro):
    libreria=[{
        "titolo":"viaggio sulla luna",
        "prezzo": 20,
        "stock": 120}, 
        {"titolo":"ritorno di fiamma",
        "prezzo": 13,
        "stock":0}]
    esistenza = False
    for book in libreria:
        if libro in book["titolo"]:
            esistenza = True
            if book["stock"] > 0:
                book["stock"] -= 1
                print("Vendita effettuata con successo")
                return True 
            else:
                print("Il libro non e disponibile, lo abbiamo messo in ordine")
                return False
        else:
            pass

    if esistenza == False :
        print("Il libro non e trattato dalla libreria, lo abbiamo messo in ordine")


vendi("ritorno di fiamma")

#return False
#    return True
