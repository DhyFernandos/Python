#!/usr/bin/env python3
"""
Script de teste para demonstrar as funcionalidades da calculadora.
"""

from calculator import Calculator

def test_calculator():
    """Testa todas as funcionalidades da calculadora."""
    print("="*60)
    print("           TESTE DA CALCULADORA PYTHON")
    print("="*60)
    
    calc = Calculator()
    
    # Teste de operações básicas
    print("\n=== OPERAÇÕES BÁSICAS ===")
    print(f"Soma: 10 + 5 = {calc.add(10, 5)}")
    print(f"Subtração: 10 - 3 = {calc.subtract(10, 3)}")
    print(f"Multiplicação: 4 * 7 = {calc.multiply(4, 7)}")
    print(f"Divisão: 15 / 3 = {calc.divide(15, 3)}")
    
    # Teste de operações avançadas
    print("\n=== OPERAÇÕES AVANÇADAS ===")
    print(f"Potenciação: 2^8 = {calc.power(2, 8)}")
    print(f"Raiz quadrada: √16 = {calc.square_root(16)}")
    print(f"Raiz cúbica: ∛27 = {calc.nth_root(27, 3)}")
    print(f"Logaritmo: log(100) = {calc.logarithm(100)}")
    print(f"Log natural: ln(e) = {calc.natural_log(2.718281828)}")
    
    # Teste de funções trigonométricas
    print("\n=== FUNÇÕES TRIGONOMÉTRICAS ===")
    print(f"Seno 30°: {calc.sine(30, True):.6f}")
    print(f"Cosseno 60°: {calc.cosine(60, True):.6f}")
    print(f"Tangente 45°: {calc.tangent(45, True):.6f}")
    
    # Teste de fatorial
    print("\n=== FATORIAL ===")
    print(f"5! = {calc.factorial(5)}")
    print(f"7! = {calc.factorial(7)}")
    
    # Teste de porcentagem
    print("\n=== PORCENTAGEM ===")
    print(f"25% de 200 = {calc.percentage(200, 25)}")
    print(f"15% de 80 = {calc.percentage(80, 15)}")
    
    # Teste de conversões
    print("\n=== CONVERSÕES DE BASE ===")
    print(f"42 em binário: {calc.to_binary(42)}")
    print(f"42 em octal: {calc.to_octal(42)}")
    print(f"42 em hexadecimal: {calc.to_hexadecimal(42)}")
    
    # Teste de expressões
    print("\n=== AVALIAÇÃO DE EXPRESSÕES ===")
    print(f"2 + 3 * 4 = {calc.evaluate_expression('2 + 3 * 4')}")
    print(f"(5 + 3) ** 2 = {calc.evaluate_expression('(5 + 3) ** 2')}")
    print(f"20 / 4 + 2 * 3 = {calc.evaluate_expression('20 / 4 + 2 * 3')}")
    
    # Teste de memória
    print("\n=== MEMÓRIA ===")
    calc.memory_store(42.5)
    print(f"Valor armazenado: {calc.memory_recall()}")
    calc.memory_clear()
    print(f"Memória após limpar: {calc.memory_recall()}")
    
    # Mostrar histórico
    print("\n=== HISTÓRICO (últimas operações) ===")
    calc.show_history()
    
    # Teste de tratamento de erros
    print("\n=== TESTE DE TRATAMENTO DE ERROS ===")
    try:
        calc.divide(10, 0)
    except ValueError as e:
        print(f"Divisão por zero: {e}")
    
    try:
        calc.square_root(-4)
    except ValueError as e:
        print(f"Raiz de número negativo: {e}")
    
    try:
        calc.logarithm(0)
    except ValueError as e:
        print(f"Logaritmo de zero: {e}")
    
    print("\n" + "="*60)
    print("           TODOS OS TESTES CONCLUÍDOS!")
    print("="*60)


if __name__ == "__main__":
    test_calculator()