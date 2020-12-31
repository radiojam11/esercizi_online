"""
Esercizio 023: Funzione Fattoriale Ricorsiva
Scrivi una funzione ricorsiva che calcola il fattoriale di un numero dato.
"""
#qui ho copiato pari pari la funzione risolta 
#in pratica la funzione puo' chiamere se stessa
#il primo if  fa si' che si esca quando num arriva ad 1
def fattoriale(num):
    if num == 1:
        return num
    else:
        num = num * fattoriale(num-1)
        return num

print(fattoriale(100))

def fat(num):
    for i in range(1,num):
        num = num*i
    return num

print(fat(100))