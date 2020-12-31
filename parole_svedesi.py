#conversione di una parola in giochino svedese che aggiunge ad ogni consonante della parola data, la consonante seguita da una o
P_sv=""
P_or=input("digita una parola da convertire in giochino svedese -:")
for i in range (len( P_or )):
    L= P_or[i]
    if (L == "a" or L == "e" or L == "i" or L == "o" or L == "u"):
        vocale = True
        P_sv = P_sv + P_or[i]
    else:
        P_sv = P_sv + P_or[i] + "o" + P_or[i]
        vocale = False

print("la parola convertita in giochino svedese e' : ")
print (P_sv)

#conversione inversa

print ( "converto di nuovo in parola italiana")
P_or = ""
for i in range (len(P_sv)):
    #se vocale
    if (P_sv[i] == "a" or P_sv[i] == "e" or P_sv[i] == "i"  or P_sv[i] == "u"):
        P_or = P_or + P_sv[i]
    #se e' una "o"
    elif (P_sv[i] == "o"):
        # se e' la lettera di partenza o finale della parola
        if i == 0 or i  == (len(P_sv)): 
             P_or = P_or + P_sv[i]
        else:   #altrimenti : e' una "o" e sta nel mezzo della parola - se ha una vocale prima:
            if (P_sv[i-1] == "a" or P_sv[i-1] == "e" or P_sv[i-1] == "i"  or P_sv[i-1] == "u" or P_sv[i-1] == "o"):
                P_or = P_or + P_sv[i]
            elif (P_sv[i-1] == P_sv[i+1] ):  #se e' una "o" e non ha una vocale prima e la lettera precedente e quella successiva sono uguali non la considerare (da vedere la eccezione "cocomero")
                pass
            else:   #qui abbiamo una "o" che scritta nel mezzo della parola, non e' tra due lettere uguali, allora si puo' aggiungere:
                 P_or = P_or + P_sv[i]


    else:  # e' una consonante - se la lettera successiva e' una "o" e la lettera dopo ancora e' uguale a se stessa
        if (i < (len(P_sv)-2)):
            if (P_sv[i+1] == "o" and P_sv[i+2] == P_sv[i]):
                P_or = P_or + P_sv[i]
print (P_or)

