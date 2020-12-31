"""
Esercizio 022: Crittografia ROT-13
Il ROT-13 è un semplice cifrario monoalfabetico, in cui ogni lettera 
del messaggio da cifrare viene sostituita con quella posta 13 posizioni più avanti nell'alfabeto.

Scrivi una semplice funzione in grado di criptare una stringa passata, 
o decriptarla se la stringa è già stata precedentemente codificata.
"""


def cifrario(stringa):
    alfabeto="abcdefghkilmnopqrstuvz"
    newstringa = ""
    for el in stringa:
        pos=alfabeto.index(el)
        if pos < (22-13):
            npos=pos+13
            newstringa += alfabeto[npos]
        else:
            npos = 13-(22-pos)
            newstringa += alfabeto[npos]

    print(newstringa)

cifrario("supercalifragilistichespiralidoso")