"""
Calculadora de IMC (Índice de Massa Corporal)
Autor: profleodresch - projeto de aprendizado
Uso: python imc.py
"""

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o IMC = peso / (altura * altura)."""
    if altura <= 0:
        raise ValueError("Altura deve ser maior que zero.")
    if peso <= 0:
        raise ValueError("Peso deve ser maior que zero.")
    return peso / (altura * altura)


def classificar_imc(imc: float) -> str:
    """Classifica o IMC segundo a OMS."""
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidade grau 1"
    elif imc < 40:
        return "Obesidade grau 2"
    else:
        return "Obesidade grau 3 (mórbida)"


def ler_float(mensagem: str) -> float:
    """Lê um número do usuário, aceitando vírgula como separador decimal."""
    while True:
        try:
            texto = input(mensagem).strip().replace(",", ".")
            valor = float(texto)
            if valor <= 0:
                print("⚠️  Digite um valor maior que zero. Tente novamente.")
                continue
            return valor
        except ValueError:
            print("⚠️  Valor inválido. Digite apenas números. Ex: 70.5")


def main():
    print("=" * 40)
    print("  📊 CALCULADORA DE IMC")
    print("=" * 40)
    print("Fórmula: IMC = peso (kg) / altura² (m)\n")

    peso = ler_float("Digite seu peso em kg (ex: 70.5): ")
    altura = ler_float("Digite sua altura em metros (ex: 1.75): ")

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print("\n" + "-" * 40)
    print(f"  Seu IMC: {imc:.2f}")
    print(f"  Classificação: {classificacao}")
    print("-" * 40)

    print("\nTabela OMS:")
    print("  < 18.5          → Abaixo do peso")
    print("  18.5 - 24.9     → Peso normal")
    print("  25 - 29.9       → Sobrepeso")
    print("  30 - 34.9       → Obesidade grau 1")
    print("  35 - 39.9       → Obesidade grau 2")
    print("  >= 40           → Obesidade grau 3")


if __name__ == "__main__":
    main()
