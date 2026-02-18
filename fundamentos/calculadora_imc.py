"""Calculadora do Índice de Massa Corporal (IMC) com classificação.

Este módulo implementa o cálculo do IMC (peso/altura²) e classificação automática
de acordo com as faixas etárias da OMS adaptadas para adultos. Inclui validação
de entradas e tratamento de exceções para entradas inválidas.

O programa solicita peso (kg) e altura (m) via console, calcula o IMC,
classifica o resultado e exibe tanto o valor numérico quanto a categoria.

Parameters
----------
None
    Programa executável standalone via função `main()`.

Returns
-------
None
    Exibe resultados no console.

Functions
---------
calcular_imc(peso : float, altura : float)
    Calcula IMC = peso / (altura²).
classificar_imc(imc : float)
    Classifica IMC nas faixas: Abaixo do peso, Normal, Sobrepeso, 
    Obesidade, Obesidade Grave.

"""

def calcular_imc(peso: float, altura: float) -> float:
    """Calcula o Índice de Massa Corporal (IMC)"""
    return peso / (altura ** 2)

def classificar_imc(imc: float) -> str:
    """Classifica o IMC de acordo com as categorias estabelecidas"""
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 40:
        return "Obesidade"
    else:
        return "Obesidade Grave"
    
def main():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        
        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos.")
            return
        
        imc = calcular_imc(peso, altura)
        classificacao = classificar_imc(imc)
        
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Classificação: {classificacao}")
        
    except ValueError:
        print("Entrada inválida. Por favor, insira números para peso e altura.")
        
if __name__ == "__main__":
    main()