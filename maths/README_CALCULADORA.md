# 🧮 Calculadora Python

Uma calculadora completa e interativa desenvolvida em Python com múltiplas funcionalidades matemáticas.

## 📋 Funcionalidades

### ➕ Operações Básicas
- ✅ Adição (+)
- ✅ Subtração (-)
- ✅ Multiplicação (*)
- ✅ Divisão (/)
- ✅ Módulo (%)

### 🔢 Operações Avançadas
- ✅ Potenciação (x^y)
- ✅ Raiz quadrada (√x)
- ✅ Raiz n-ésima (ⁿ√x)
- ✅ Logaritmo base 10
- ✅ Logaritmo natural (ln)
- ✅ Logaritmo base personalizada

### 📐 Funções Trigonométricas
- ✅ Seno (sin)
- ✅ Cosseno (cos)
- ✅ Tangente (tan)
- ✅ Suporte para graus e radianos

### 🔄 Outras Funcionalidades
- ✅ Fatorial (n!)
- ✅ Cálculo de porcentagem
- ✅ Conversões de base (binário, octal, hexadecimal)
- ✅ Avaliação de expressões matemáticas
- ✅ Memória (armazenar, recuperar, limpar)
- ✅ Histórico de operações
- ✅ Tratamento de erros

## 🚀 Como Usar

### Modo Interativo

Execute o arquivo principal para abrir a interface interativa:

```bash
python3 maths/calculator.py
```

Você verá um menu com todas as opções disponíveis:

```
==================================================
           CALCULADORA PYTHON
==================================================
1.  Operações básicas (+, -, *, /, %)
2.  Potenciação (x^y)
3.  Raiz quadrada
4.  Raiz n-ésima
5.  Logaritmo
6.  Logaritmo natural (ln)
7.  Funções trigonométricas
8.  Fatorial
9.  Porcentagem
10. Conversões de base
11. Avaliar expressão
12. Memória
13. Histórico
14. Ajuda
0.  Sair
==================================================
```

### Uso Programático

Você também pode importar e usar a classe `Calculator` diretamente em seu código:

```python
from calculator import Calculator

# Criar uma instância
calc = Calculator()

# Operações básicas
resultado = calc.add(10, 5)  # 15
resultado = calc.multiply(4, 7)  # 28

# Operações avançadas
raiz = calc.square_root(16)  # 4.0
potencia = calc.power(2, 8)  # 256

# Trigonometria
seno = calc.sine(30, degrees=True)  # 0.5

# Expressões
resultado = calc.evaluate_expression("2 + 3 * 4")  # 14

# Conversões
binario = calc.to_binary(42)  # '0b101010'

# Ver histórico
calc.show_history()
```

## 🧪 Testes

Execute o script de teste para ver todas as funcionalidades em ação:

```bash
python3 maths/test_calculator.py
```

Ou execute o exemplo de uso:

```bash
python3 maths/exemplo_uso_calculadora.py
```

## 📝 Exemplos de Uso

### Operações Básicas
```python
calc = Calculator()
print(calc.add(15, 25))      # 40
print(calc.subtract(20, 8))  # 12
print(calc.multiply(6, 7))   # 42
print(calc.divide(100, 4))   # 25.0
```

### Funções Avançadas
```python
# Potenciação
print(calc.power(3, 4))      # 81

# Raízes
print(calc.square_root(64))  # 8.0
print(calc.nth_root(27, 3))  # 3.0

# Logaritmos
print(calc.logarithm(100))           # 2.0 (log base 10)
print(calc.natural_log(2.718281828)) # ≈ 1.0
print(calc.logarithm(8, 2))          # 3.0 (log base 2)
```

### Trigonometria
```python
# Usando graus
print(calc.sine(30, degrees=True))   # 0.5
print(calc.cosine(60, degrees=True)) # 0.5
print(calc.tangent(45, degrees=True)) # 1.0

# Usando radianos
import math
print(calc.sine(math.pi/2))  # 1.0
```

### Expressões Matemáticas
```python
# A calculadora pode avaliar expressões complexas
print(calc.evaluate_expression("(2 + 3) * 4"))     # 20
print(calc.evaluate_expression("2**3 + 4*5"))      # 28
print(calc.evaluate_expression("100 / (2 + 3)"))   # 20.0
```

### Conversões de Base
```python
print(calc.to_binary(255))      # '0b11111111'
print(calc.to_octal(255))       # '0o377'
print(calc.to_hexadecimal(255)) # '0xff'
```

## ⚠️ Tratamento de Erros

A calculadora trata vários tipos de erros matematicamente inválidos:

- Divisão por zero
- Raiz quadrada de números negativos
- Logaritmo de números não positivos
- Fatorial de números negativos
- Expressões inválidas

Exemplo:
```python
try:
    calc.divide(10, 0)
except ValueError as e:
    print(e)  # "Erro: Divisão por zero não é permitida"
```

## 🔧 Requisitos

- Python 3.6 ou superior
- Biblioteca `math` (incluída no Python padrão)

## 📁 Estrutura dos Arquivos

```
maths/
├── calculator.py                # Arquivo principal da calculadora
├── test_calculator.py          # Script de teste completo
├── exemplo_uso_calculadora.py  # Exemplo de uso programático
└── README_CALCULADORA.md       # Esta documentação
```

## 🎯 Funcionalidades da Interface Interativa

- **Menu intuitivo**: Navegação fácil por números ou comandos
- **Validação de entrada**: Verifica se os dados inseridos são válidos
- **Histórico**: Mantém registro das últimas 10 operações
- **Memória**: Armazena temporariamente valores para uso posterior
- **Ajuda integrada**: Digite '14' ou 'help' para ver as opções
- **Saída segura**: Digite '0' ou 'sair' para encerrar

## 💡 Dicas de Uso

1. **Expressões**: Use parênteses para controlar a ordem das operações
2. **Trigonometria**: Escolha entre graus (°) e radianos (rad) conforme necessário
3. **Memória**: Útil para cálculos que precisam reutilizar resultados
4. **Histórico**: Revise operações anteriores para verificar cálculos
5. **Conversões**: Ideais para programação e computação

---

Desenvolvido como uma calculadora educativa e funcional para demonstrar conceitos matemáticos e de programação em Python! 🐍✨