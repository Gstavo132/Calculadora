def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def subtracao(a, b):
    """Retorna a subtração de dois números."""
    return a - b

def multiplicacao(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b

def divisao(a, b):
    """Retorna a divisão de dois números. Lança erro se b for 0."""
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return a / b

def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    print("\n=== Calculadora ===")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

def main():
    """Função principal para executar a calculadora."""
    while True:
        exibir_menu()
        escolha = input("Escolha uma operação (1-5): ")

        if escolha == "5":
            print("Encerrando a calculadora. Até mais!")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if escolha == "1":
                print(f"Resultado da soma: {soma(num1, num2)}")
            elif escolha == "2":
                print(f"Resultado da subtração: {subtracao(num1, num2)}")
            elif escolha == "3":
                print(f"Resultado da multiplicação: {multiplicacao(num1, num2)}")
            elif escolha == "4":
                try:
                    print(f"Resultado da divisão: {divisao(num1, num2)}")
                except ValueError as e:
                    print(e)
            else:
                print("Escolha inválida! Por favor, tente novamente.")
        except ValueError:
            print("Erro: Digite apenas números válidos!")

if __name__ == "__main__":
    main()
