"""
Esercizio 025: Info di Sistema
Scrivi una funzione che fornisca in output il nome del Sistema Operativo utilizzato con eventuali relative informazioni sulla release corrente.
"""

import os
f = os.popen('uname -a') #per linux va bene
s = f.read()
print (s)
