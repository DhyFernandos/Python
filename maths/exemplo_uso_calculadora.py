#!/usr/bin/env python3
"""
Exemplo de uso da classe Calculator

Este arquivo mostra como usar a calculadora diretamente no código
sem precisar da interface interativa.
"""

from calculator import Calculator

# Criar uma instância da calculadora
calc = Calculator()

print("=== EXEMPLO DE USO DA CALCULADORA ===\n")

# Operações básicas
resultado1 = calc.add(25, 17)
print(f"25 + 17 = {resultado1}")

resultado2 = calc.multiply(8, 9)
print(f"8 × 9 = {resultado2}")

# Operações avançadas
raiz = calc.square_root(144)
print(f"√144 = {raiz}")

potencia = calc.power(3, 4)
print(f"3⁴ = {potencia}")

# Trigonometria
seno_90 = calc.sine(90, degrees=True)
print(f"sen(90°) = {seno_90}")

# Expressões matemáticas
expressao = calc.evaluate_expression("(2 + 3) * 4 - 1")
print(f"(2 + 3) × 4 - 1 = {expressao}")

# Conversões
binario = calc.to_binary(255)
hex_val = calc.to_hexadecimal(255)
print(f"255 em binário: {binario}")
print(f"255 em hexadecimal: {hex_val}")

# Mostrar histórico das operações
print("\n=== HISTÓRICO DAS OPERAÇÕES ===")
calc.show_history()

print("\n=== USO INDIVIDUAL CONCLUÍDO ===")