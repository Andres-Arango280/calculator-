import math

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b if b != 0 else "Error: División por cero... vuelva a intentarlo"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    return math.sqrt(a) if a >= 0 else "Error: Raíz de número negativo... vuelva a intentarlo"

def calculadora():
    while True:
        print("\nOperaciones disponibles:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Potencia")
        print("6. Raíz Cuadrada")
        print("7. Salir")
        
        opcion = input("Seleccione una operación (1-7) solo valor numericos : ")
        
        if opcion == "7":
            print("Saliendo... por favor esperar el sistema")
            break
        
        if opcion in ["1", "2", "3", "4", "5"]:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if opcion == "1":
                print("Resultado:", suma(a, b))
            elif opcion == "2":
                print("Resultado:", resta(a, b))
            elif opcion == "3":
                print("Resultado:", multiplicacion(a, b))
            elif opcion == "4":
                print("Resultado:", division(a, b))
            elif opcion == "5":
                print("Resultado:", potencia(a, b))
        elif opcion == "6":
            a = float(input("Ingrese el número: "))
            print("Resultado:", raiz_cuadrada(a))
        else:
            print("Opción no válida, intente de nuevo.... vuelva a intentarlo")

if __name__ == "__main__":
    calculadora()
