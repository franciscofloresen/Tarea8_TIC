import sys

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
    if len(sys.argv) != 4:
        print("Uso: script.py <numero1> <numero2> <operacion>")
        sys.exit(1)

    x = float(sys.argv[1])
    y = float(sys.argv[2])
    operacion = sys.argv[3].lower()

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

