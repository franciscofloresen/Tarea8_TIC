def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: División por cero."

if __name__ == "__main__":
    print("Mini Calculadora")
    print("Ingrese dos números y la operación a realizar (suma, resta, multiplicación, división).")

    x = float(input("Ingrese el primer número: "))
    y = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación: ").lower()

    if operacion == 'suma':
        resultado = suma(x, y)
    elif operacion == 'resta':
        resultado = resta(x, y)
    elif operacion == 'multiplicación':
        resultado = multiplicacion(x, y)
    elif operacion == 'división':
        resultado = division(x, y)
    else:
        resultado = "Operación no válida."

    print(f"Resultado: {resultado}")
