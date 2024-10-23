num1 = int(input("Escribe un numero bro:"))
num2 = int(input("Escribe otro numero bro:"))

op = input("Escribe un + o - para hacer la operacion")
if op == '-':
    res = num1-num2
elif op == '+':
    res = num1-num2

print(f"Tu Resultado fue: {res}")