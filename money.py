#money.py

print ("Money\n")
print ("Determina il numero minimo di banconote")

#input
n = input("Inserire l'importo (in dollari): ")

#controllo variabile
if int (n) < 0:
    print ("Hai inserito un valore minore a zero!!!")
#esercizio
else:
    x = float(n)/ 20
    print ("Banconote da 20$ utilizzate: ",int(x))
    n = float(n) - (int(x)*20)
    x = float(n) /10
    print ("Banconote da 10$ utilizzate: ",int(x))
    n = float(n) - (int(x)*10)
    x = float(n) /5
    print ("Banconote da 5$ utilizzate: ",int(x))
    n = float(n) - (int(x)*5)
    x = n
    print ("Banconote da 1$ utilizzate: ",int(x))

