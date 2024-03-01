# Imprimir un rango de un numero
def imprimirRango (n1, n2):
    for i in range (n1, n2+1):
        print (i)
imprimirRango (5,17)
imprimirRango (6,20)

num1= int(input("n1="))
num2= int(input("n2="))
imprimirRango (num1, num2)
