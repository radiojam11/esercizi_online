"""
Esercizio 012: Il Frequenzimetro
Scrivi una funzione a cui passare una stringa come parametro, e che restituisca 
un dizionario rappresentante la "frequenza di comparsa" di ciscun carattere componente la stringa.

Semplicemente, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}!
"""
def frequenzimetro(stringa):
    d = {}
    for elem in stringa:
        if elem not in d:
            d[elem] = 0
        d[elem]+=1

    print(d)
    riprova = 0
    for el in d:
        riprova = riprova + d[el] 

    print(riprova)
                


frequenzimetro("supercalifragili")


