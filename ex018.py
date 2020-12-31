"""
Esercizio 018: Generatore di Password
Scrivi una funzione generatrice di password.

La funzione deve generare una stringa alfanumerica 
di 8 caratteri qualora l'utente voglia una password semplice,
 o di 20 caratteri ascii qualora desideri una password 
 più complicata.

"""




def mkpassw():
        
    from random import randint
    s = input("Come vuoi la password? semplice S o complicata C ? ")
    passw = ""
    if s == "s" or s == "S":
        L = 8
    else :
        L = 20
    for i in range(L):
        a=randint(64, 126)
        passw += chr(a)  #chr converte il numero nel carattere ascii corrispondente - inverso e' ord("c") che converte il carattere in numero
    print (passw)

mkpassw()