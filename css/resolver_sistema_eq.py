# Programa para resolver o sistema de equações M + N = valor1 e M - N = valor2

def calcular_m_n(valor1, valor2):
    print("Resolver o sistema de equações M + N = valor1 e M - N = valor2")

    # Cálculo de M e N
    M = (valor1 + valor2) / 2
    N = (valor1 - valor2) / 2

    # Exibir cálculos passo a passo
    print("\nCálculos passo a passo:")
    print(f"1. Somamos as duas equações: (M + N) + (M - N) = {valor1} + {valor2}")
    print(f"   Isso resulta em: 2M = {valor1 + valor2}")
    print(f"   Logo, M = ({valor1 + valor2}) / 2 = {M}")

    print(f"\n2. Substituímos M na primeira equação para encontrar N:")
    print(f"   {M} + N = {valor1}")
    print(f"   N = {valor1} - {M} = {N}")

    # Exibir resultado final
    print("\nResultado final:")
    print(f"M = {M}")
    print(f"N = {N}")

if __name__ == "__main__":
    # Pedir valores ao usuário
    valor1 = float(input("Digite o valor de M + N: "))
    valor2 = float(input("Digite o valor de M - N: "))
    calcular_m_n(valor1, valor2)