#!/usr/bin/env python3
"""
Calculadora completa em Python

Esta calculadora oferece:
- Operações básicas (+, -, *, /, %)
- Operações avançadas (potenciação, raiz quadrada, logaritmo)
- Funções trigonométricas (sin, cos, tan e suas inversas)
- Conversões de base numérica (binário, octal, hexadecimal)
- Histórico de operações
- Interface interativa

Autor: Assistente IA
"""

import math
import re
from typing import List, Optional, Union


class Calculator:
    """Classe principal da calculadora com todas as funcionalidades."""
    
    def __init__(self):
        """Inicializa a calculadora com histórico vazio."""
        self.history: List[str] = []
        self.memory: float = 0.0
        
    def add(self, a: float, b: float) -> float:
        """Soma dois números."""
        result = a + b
        self._add_to_history(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtrai dois números."""
        result = a - b
        self._add_to_history(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplica dois números."""
        result = a * b
        self._add_to_history(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide dois números."""
        if b == 0:
            raise ValueError("Erro: Divisão por zero não é permitida")
        result = a / b
        self._add_to_history(f"{a} / {b} = {result}")
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """Calcula a potência de um número."""
        result = base ** exponent
        self._add_to_history(f"{base} ^ {exponent} = {result}")
        return result
    
    def square_root(self, number: float) -> float:
        """Calcula a raiz quadrada de um número."""
        if number < 0:
            raise ValueError("Erro: Raiz quadrada de número negativo")
        result = math.sqrt(number)
        self._add_to_history(f"√{number} = {result}")
        return result
    
    def nth_root(self, number: float, n: float) -> float:
        """Calcula a raiz n-ésima de um número."""
        if n == 0:
            raise ValueError("Erro: Raiz com índice zero")
        if number < 0 and n % 2 == 0:
            raise ValueError("Erro: Raiz par de número negativo")
        
        result = number ** (1/n)
        self._add_to_history(f"{n}√{number} = {result}")
        return result
    
    def logarithm(self, number: float, base: Optional[float] = None) -> float:
        """Calcula o logaritmo de um número (base 10 por padrão)."""
        if number <= 0:
            raise ValueError("Erro: Logaritmo de número não positivo")
        
        if base is None:
            result = math.log10(number)
            self._add_to_history(f"log({number}) = {result}")
        else:
            if base <= 0 or base == 1:
                raise ValueError("Erro: Base do logaritmo inválida")
            result = math.log(number, base)
            self._add_to_history(f"log_{base}({number}) = {result}")
        
        return result
    
    def natural_log(self, number: float) -> float:
        """Calcula o logaritmo natural (ln) de um número."""
        if number <= 0:
            raise ValueError("Erro: Logaritmo natural de número não positivo")
        result = math.log(number)
        self._add_to_history(f"ln({number}) = {result}")
        return result
    
    def sine(self, angle: float, degrees: bool = False) -> float:
        """Calcula o seno de um ângulo."""
        if degrees:
            angle = math.radians(angle)
        result = math.sin(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"sin({angle if not degrees else math.degrees(angle)}{unit}) = {result}")
        return result
    
    def cosine(self, angle: float, degrees: bool = False) -> float:
        """Calcula o cosseno de um ângulo."""
        if degrees:
            angle = math.radians(angle)
        result = math.cos(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"cos({angle if not degrees else math.degrees(angle)}{unit}) = {result}")
        return result
    
    def tangent(self, angle: float, degrees: bool = False) -> float:
        """Calcula a tangente de um ângulo."""
        if degrees:
            angle = math.radians(angle)
        result = math.tan(angle)
        unit = "°" if degrees else "rad"
        self._add_to_history(f"tan({angle if not degrees else math.degrees(angle)}{unit}) = {result}")
        return result
    
    def factorial(self, n: int) -> int:
        """Calcula o fatorial de um número."""
        if n < 0:
            raise ValueError("Erro: Fatorial de número negativo")
        if not isinstance(n, int):
            raise ValueError("Erro: Fatorial apenas para números inteiros")
        
        result = math.factorial(n)
        self._add_to_history(f"{n}! = {result}")
        return result
    
    def percentage(self, value: float, percent: float) -> float:
        """Calcula a porcentagem de um valor."""
        result = (value * percent) / 100
        self._add_to_history(f"{percent}% de {value} = {result}")
        return result
    
    def to_binary(self, number: int) -> str:
        """Converte um número para binário."""
        if not isinstance(number, int):
            raise ValueError("Erro: Conversão binária apenas para números inteiros")
        result = bin(number)
        self._add_to_history(f"{number} em binário = {result}")
        return result
    
    def to_octal(self, number: int) -> str:
        """Converte um número para octal."""
        if not isinstance(number, int):
            raise ValueError("Erro: Conversão octal apenas para números inteiros")
        result = oct(number)
        self._add_to_history(f"{number} em octal = {result}")
        return result
    
    def to_hexadecimal(self, number: int) -> str:
        """Converte um número para hexadecimal."""
        if not isinstance(number, int):
            raise ValueError("Erro: Conversão hexadecimal apenas para números inteiros")
        result = hex(number)
        self._add_to_history(f"{number} em hexadecimal = {result}")
        return result
    
    def memory_store(self, value: float) -> None:
        """Armazena um valor na memória."""
        self.memory = value
        self._add_to_history(f"Valor {value} armazenado na memória")
    
    def memory_recall(self) -> float:
        """Recupera o valor da memória."""
        self._add_to_history(f"Valor da memória: {self.memory}")
        return self.memory
    
    def memory_clear(self) -> None:
        """Limpa a memória."""
        self.memory = 0.0
        self._add_to_history("Memória limpa")
    
    def evaluate_expression(self, expression: str) -> float:
        """
        Avalia uma expressão matemática simples.
        Suporta +, -, *, /, %, ** (potenciação), parênteses
        """
        # Remove espaços
        expression = expression.replace(" ", "")
        
        # Valida caracteres permitidos
        allowed_chars = set("0123456789+-*/%().^")
        if not all(c in allowed_chars for c in expression):
            raise ValueError("Erro: Caracteres inválidos na expressão")
        
        # Substitui ^ por ** para potenciação
        expression = expression.replace("^", "**")
        
        try:
            # Avalia a expressão de forma segura
            result = eval(expression, {"__builtins__": {}}, {})
            self._add_to_history(f"{expression} = {result}")
            return float(result)
        except Exception as e:
            raise ValueError(f"Erro na expressão: {str(e)}")
    
    def show_history(self) -> None:
        """Mostra o histórico de operações."""
        if not self.history:
            print("Histórico vazio")
            return
        
        print("\n=== HISTÓRICO DE OPERAÇÕES ===")
        for i, operation in enumerate(self.history[-10:], 1):  # Últimas 10 operações
            print(f"{i:2d}. {operation}")
        print("=" * 31)
    
    def clear_history(self) -> None:
        """Limpa o histórico de operações."""
        self.history.clear()
        print("Histórico limpo")
    
    def _add_to_history(self, operation: str) -> None:
        """Adiciona uma operação ao histórico."""
        self.history.append(operation)


def show_menu():
    """Mostra o menu principal da calculadora."""
    print("\n" + "="*50)
    print("           CALCULADORA PYTHON")
    print("="*50)
    print("1.  Operações básicas (+, -, *, /, %)")
    print("2.  Potenciação (x^y)")
    print("3.  Raiz quadrada")
    print("4.  Raiz n-ésima")
    print("5.  Logaritmo")
    print("6.  Logaritmo natural (ln)")
    print("7.  Funções trigonométricas")
    print("8.  Fatorial")
    print("9.  Porcentagem")
    print("10. Conversões de base")
    print("11. Avaliar expressão")
    print("12. Memória")
    print("13. Histórico")
    print("14. Ajuda")
    print("0.  Sair")
    print("="*50)


def main():
    """Função principal que executa a calculadora interativa."""
    calc = Calculator()
    
    print("Bem-vindo à Calculadora Python!")
    print("Digite 'help' ou '14' para ver as opções disponíveis")
    
    while True:
        try:
            show_menu()
            choice = input("\nEscolha uma opção: ").strip()
            
            if choice == '0' or choice.lower() == 'sair':
                print("Obrigado por usar a Calculadora Python!")
                break
            
            elif choice == '1':
                print("\nOperações básicas:")
                print("+ (soma), - (subtração), * (multiplicação), / (divisão), % (módulo)")
                a = float(input("Digite o primeiro número: "))
                op = input("Digite a operação (+, -, *, /, %): ")
                b = float(input("Digite o segundo número: "))
                
                if op == '+':
                    result = calc.add(a, b)
                elif op == '-':
                    result = calc.subtract(a, b)
                elif op == '*':
                    result = calc.multiply(a, b)
                elif op == '/':
                    result = calc.divide(a, b)
                elif op == '%':
                    result = a % b
                    calc._add_to_history(f"{a} % {b} = {result}")
                else:
                    print("Operação inválida!")
                    continue
                
                print(f"Resultado: {result}")
            
            elif choice == '2':
                base = float(input("Digite a base: "))
                exp = float(input("Digite o expoente: "))
                result = calc.power(base, exp)
                print(f"Resultado: {result}")
            
            elif choice == '3':
                num = float(input("Digite o número: "))
                result = calc.square_root(num)
                print(f"Resultado: {result}")
            
            elif choice == '4':
                num = float(input("Digite o número: "))
                n = float(input("Digite o índice da raiz: "))
                result = calc.nth_root(num, n)
                print(f"Resultado: {result}")
            
            elif choice == '5':
                num = float(input("Digite o número: "))
                base_input = input("Digite a base (Enter para base 10): ").strip()
                base = float(base_input) if base_input else None
                result = calc.logarithm(num, base)
                print(f"Resultado: {result}")
            
            elif choice == '6':
                num = float(input("Digite o número: "))
                result = calc.natural_log(num)
                print(f"Resultado: {result}")
            
            elif choice == '7':
                print("\nFunções trigonométricas:")
                print("1. Seno")
                print("2. Cosseno") 
                print("3. Tangente")
                trig_choice = input("Escolha: ")
                
                angle = float(input("Digite o ângulo: "))
                unit = input("Graus (g) ou Radianos (r)? ").lower()
                degrees = unit == 'g'
                
                if trig_choice == '1':
                    result = calc.sine(angle, degrees)
                elif trig_choice == '2':
                    result = calc.cosine(angle, degrees)
                elif trig_choice == '3':
                    result = calc.tangent(angle, degrees)
                else:
                    print("Opção inválida!")
                    continue
                
                print(f"Resultado: {result}")
            
            elif choice == '8':
                n = int(input("Digite o número: "))
                result = calc.factorial(n)
                print(f"Resultado: {result}")
            
            elif choice == '9':
                value = float(input("Digite o valor: "))
                percent = float(input("Digite a porcentagem: "))
                result = calc.percentage(value, percent)
                print(f"Resultado: {result}")
            
            elif choice == '10':
                print("\nConversões de base:")
                print("1. Para binário")
                print("2. Para octal")
                print("3. Para hexadecimal")
                conv_choice = input("Escolha: ")
                
                num = int(input("Digite o número (inteiro): "))
                
                if conv_choice == '1':
                    result = calc.to_binary(num)
                elif conv_choice == '2':
                    result = calc.to_octal(num)
                elif conv_choice == '3':
                    result = calc.to_hexadecimal(num)
                else:
                    print("Opção inválida!")
                    continue
                
                print(f"Resultado: {result}")
            
            elif choice == '11':
                expr = input("Digite a expressão (ex: 2+3*4, (5+3)**2): ")
                result = calc.evaluate_expression(expr)
                print(f"Resultado: {result}")
            
            elif choice == '12':
                print("\nMemória:")
                print("1. Armazenar valor")
                print("2. Recuperar valor")
                print("3. Limpar memória")
                mem_choice = input("Escolha: ")
                
                if mem_choice == '1':
                    value = float(input("Digite o valor para armazenar: "))
                    calc.memory_store(value)
                elif mem_choice == '2':
                    result = calc.memory_recall()
                    print(f"Valor na memória: {result}")
                elif mem_choice == '3':
                    calc.memory_clear()
                else:
                    print("Opção inválida!")
            
            elif choice == '13':
                print("\nHistórico:")
                print("1. Mostrar histórico")
                print("2. Limpar histórico")
                hist_choice = input("Escolha: ")
                
                if hist_choice == '1':
                    calc.show_history()
                elif hist_choice == '2':
                    calc.clear_history()
                else:
                    print("Opção inválida!")
            
            elif choice == '14' or choice.lower() == 'help':
                print("\n=== AJUDA ===")
                print("Esta calculadora oferece várias funcionalidades:")
                print("• Operações básicas: +, -, *, /, %")
                print("• Potenciação: x^y")
                print("• Raízes: quadrada e n-ésima")
                print("• Logaritmos: base 10, base personalizada, natural (ln)")
                print("• Trigonometria: sin, cos, tan (graus ou radianos)")
                print("• Fatorial: n!")
                print("• Porcentagem: x% de y")
                print("• Conversões: binário, octal, hexadecimal")
                print("• Expressões: avalia expressões como '2+3*4'")
                print("• Memória: armazenar, recuperar, limpar")
                print("• Histórico: ver últimas 10 operações")
            
            else:
                print("Opção inválida! Digite um número de 0 a 14.")
        
        except ValueError as e:
            print(f"Erro: {e}")
        except KeyboardInterrupt:
            print("\n\nCalculadora encerrada pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    main()