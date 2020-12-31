"""
Esercizio 017: Il Signore del Tempo
Scrivi una semplice funzione che converta un dato 
numero di giorni, ore e minuti, passati dall'utente 
tramite funzione input, in secondi.

"""

def secondi(lista):
    a =(lista[0]*24*60*60)+(lista[1]*60*60)+(lista[2]*60)
    print(a)
secondi([11,2,25])