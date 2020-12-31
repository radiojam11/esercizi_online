#struttura dati che adeguata a contenere i CAP e le relative citta' 
# #scrivere prgramma che inserisca nuove citta' e CAP 
#scrivere un programma che chieda una citta' all'utente e stampi il relativo CAP

struttura = {
    "Roma": "10100",
    "Grosseto" : "58100",
    "Trento" : "38100"
}

def inserisci(citta, cap):
    struttura[citta]=cap

def richiesta(citta):
    print(struttura[citta])

inserisci("Bari", "70100")
richiesta("Grosseto")
print(struttura)