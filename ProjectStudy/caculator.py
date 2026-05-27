print("-------------Calculadora-------------")

operacao = input("Digite a operação desejada (+, -, *, /): ")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
resultado = None

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    if num2 == 0:
        print("Erro: Divisão por zero não é permitida.")
        
    else:
        resultado = num1 / num2
    
else:
    print("Operação inválida!")
    
if resultado is not None:   
    print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
    
    