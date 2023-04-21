def add(a, b):
    vastaus = a + b
    print(str(a) + " + " + str( b) + " = " + str(vastaus) + "\n")
def sub(a, b):
    vastaus = a - b
    print(str(a) + " - " + str(b ) + " = " + str(vastaus) + "\n")
def mul(a, b):
    vastaus = a*b
    print(str(a) + " * " + str(b) + " = " + str(vastaus) + "\n")
def div(a, b):
    vastaus = a / b
    print(str(a) + " / " + str(b) + " = " + str(vastaus) + "\n")

while True:
    print("A. Summa")
    print("B. Vähennyslasku")
    print("C. Kertolasku")
    print("D. Jakolasku")
    print("E. Exit")
    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Summa")
        a = int(input("laita ensimmäinen numero: "))
        b = int(input("laita toinen numero: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Vähennyslasku")
        a = int(input("laita ensimmäinen numero:"))
        b = int(input("laita toinen numero: "))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Kertolasku")
        a = int(input("laita ensimmäinen numero:"))
        b = int(input("laita toinen numero: "))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Jakolasku" )
        a = int(input("laita ensimmäinen numero:"))
        b = int(input("laita toinen numero: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit() 