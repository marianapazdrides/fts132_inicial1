import csv

import pytest

from main import somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros, \
    elevar_um_numero_pelo_outro, calcular_a_area_do_quadrado, calcular_a_area_do_triangulo, calcular_a_area_do_circulo, \
    calcular_a_area_do_retangulo, calcular_volume_do_paralelograma

somar_dois_numeros, subtrair_dois_numeros, dividir_dois_numeros, multiplicar_dois_numeros, \
elevar_um_numero_pelo_outro, calcular_a_area_do_quadrado, calcular_a_area_do_retangulo, \
calcular_a_area_do_triangulo, calcular_a_area_do_circulo


def testar_somar_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 8
    resultado_atual = somar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_subtrair_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 4
    resultado_atual = subtrair_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_dividir_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 3
    resultado_atual = dividir_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_multiplicar_dois_numeros():
    num1 = 6
    num2 = 2
    resultado_esperado = 12
    resultado_atual = multiplicar_dois_numeros(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_elevar_um_numero_pelo_outro():
    num1 = 6
    num2 = 2
    resultado_esperado = 36
    resultado_atual = elevar_um_numero_pelo_outro(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_calcular_a_area_do_quadrado():
    num1 = 6
    resultado_esperado = 36
    resultado_atual = calcular_a_area_do_quadrado(num1)
    assert resultado_atual == resultado_esperado


def testar_calcular_a_area_do_retangulo():
    num1 = 6
    num2 = 2
    resultado_esperado = 12
    resultado_atual = calcular_a_area_do_retangulo(num1, num2)
    assert resultado_atual == resultado_esperado


def testar_calcular_a_area_do_triangulo():
    num1 = 5
    num2 = 2
    resultado_esperado = 5
    resultado_atual = calcular_a_area_do_triangulo(num1, num2)
    assert resultado_atual == resultado_esperado


# Anotação para utilizar como massa de teste
@pytest.mark.parametrize('raio, resultado_esperado', [
    # valores
    (1, 3.14),  # Teste 1
    (2, 12.56),  # Teste 2
    (3, 28.26),  # Teste 3
    ('a', 'Falha no cálculo - Raio não é um número'),
    (' ', 'Falha no cálculo - Raio não é um número')

])
def testar_calcular_a_area_do_circulo(raio, resultado_esperado):
    # raio = 1
    # resultado_esperado = 3.14
    resultado_atual = calcular_a_area_do_circulo(raio)
    assert resultado_atual == resultado_esperado


# Ler dados de um csv para usar no teste sequinte
def ler_dados_csv():
    dados_csv = []  # Criação de uma lista vazia
    nome_arquivo = 'C:/Users/Rafael/Desktop/Mariana/Iterasys/fts132_inicial/Test/db/massa_caixa.csv'  # Local e nome do arquivo de massa
    try:
        with open(nome_arquivo, newline='') as csvfile:  # repetir a leitura até o final do arquivo
            campos = csv.reader(csvfile, delimiter=',')
            next(campos)
            for linha in campos:
                dados_csv.append(linha)
        return dados_csv
    except FileNotFoundError:
        print(f'Arquivo não encontrado: {nome_arquivo}')
    except Exception as fail:
        print(f'Falha imprevista: {fail}')

@pytest.mark.parametrize('id, largura, comprimento, altura, resultado_esperado', ler_dados_csv())
def testar_calcular_volume_do_paralelograma(id, largura, comprimento, altura, resultado_esperado):

# Configura
    largura = 5
    comprimento = 10
    altura = 2
    resultado_esperado = 100

# Executa
    resultado_atual = calcular_volume_do_paralelograma (int (largura), int (comprimento), int (altura))

# Confirma
    assert resultado_atual == int(resultado_esperado)