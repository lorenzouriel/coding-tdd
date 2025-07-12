from code.bytebank import Funcionario
import pytest
from pytest import mark

class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2000'
        esperado = 25

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        assert resultado == esperado

    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lorenzo  Uriel '
        esperado = 'Uriel'

        lorenzo = Funcionario(entrada, '20/12/2000', 1200)
        resultado = lorenzo.sobrenome()

        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000
        esperado = 90000

        funcionario_teste = Funcionario('Uriel', '20/12/2000', entrada_salario)
        funcionario_teste.decrescimo_salario()
        resultado = funcionario_teste.salario

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000
        esperado = 100

        funcionario_teste = Funcionario('teste', '11/12/2000', entrada)
        resultado = funcionario_teste.calcular_bonus()

        assert resultado == esperado
    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            entrada = 100000

            funcionario_teste = Funcionario('teste', '11/12/2000', entrada)
            resultado = funcionario_teste.calcular_bonus()

            assert resultado

    # def test_retorno_str(self):
    #     nome, data_nascimento, salario = 'Teste', '12/03/2000', 1000 # given
    #     esperado = 'Funcionario(Teste, 12/03/2000, 1000)'

    #     funcionario_teste = Funcionario (nome, data_nascimento, salario)
    #     resultado = funcionario_teste.__str__() # when

    #     assert resultado == esperado #then