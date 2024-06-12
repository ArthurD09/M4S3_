import pytest

def multiplicacao(x , y):

    return x*y;
     

def test_multiplicacao():
    assert multiplicacao(10, 2) == 20

#pytest test_multiplicacao.py

#pytest -vv –cov= nome_do_arquivo.py