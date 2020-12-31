"""
Esercizio 014: Il linguaggio dei furfanti
In Svezia, i bambini giocano spesso utilizzando un 
linguaggio un po' particolare detto "rövarspråket", 
che significa "linguaggio dei furfanti": consiste nel 
raddoppiare ogni consonante di una parola e inserire una "o"
 nel mezzo. Ad esempio la parola "mangiare" diventa
  "momanongogiarore".

Scrivi una funzione in grado di tradurre una parola 
o frase passata tramite input in "rövarspråket".

Dopo aver tradotto una frase, il programma dovrà 
chiedere all'utente se intende tradurne un'altra, e
 in caso di risposta positiva, dovrà attendere 
 l'inserimento di una nuova parola da parte dell'utente.

"""
def furfanti():
    x = 1
    while x != 9:
        parola = input("Dammi la parola da convertire ->")
        vocali =["a","e","i","o","u"]
        nuovap = ""
        for lettera in parola:
            if lettera not in vocali:
                nuovap = nuovap + lettera + "o" + lettera
            else:
                nuovap = nuovap + lettera
        print(nuovap)
    return nuovap
    x = int(input("vuoi fare un altra parola?  1 per si - 9 per no  -->"))

def decode(parola):
    vocali =["a","e","i","o","u"]
    decoded = ""
    for i  in range(len(parola)):
        if parola[i] not in vocali:
            if parola[i+1] == "o" and parola[i]==parola[i+1]:
                decoded += parola[i]
                i += 2
        else:
            if i > 0 or  i != len(parola)-1:
                if parola[i] == "o" and parola[i-1]==parola[i+1]:
                    continue
            else:
                decoded += parola[i]
    print(decoded)
    




#furfanti()


decode("etoteroro")