"""
Esercizio 024: La Serie di Fibonacci
Nella serie di Fibonacci, ciascun numero della serie è la somma dei due numeri nella serie che lo precedono, ad esempio:

1, 1, 2, 3, 5, 8, 13 (...)

Scrivi una funzione ricorsiva che restituisce in output i numeri della sequenza di Fibonacci, entro una soglia specifica impostata dall'utente.
"""

def fibonacci():
    soglia = int(input("dimmi quanti numeri vuoi calcolare "))
    fibo =[1,1]
    for i in range(2,soglia):
        fibo.append(fibo[i-1] + fibo[i-2])
    print(fibo)

fibonacci()


"""
soluzione 

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

limite = int(input("Inserisci il numero di valori della serie che desideri vedere: "))

for num in range(1, limite+1):
    print(fibonacci(num))
"""