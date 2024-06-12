# test_pytest_M4S3_funcoes.py
'''                 01
import pytest

from pytest_M4S3_funcoes import calcula_desconto, calcula_valor_total, calcula_valor_sem_desconto

def test_calcula_desconto():
    assert calcula_desconto(5) == 1.0 
    assert calcula_desconto(10) == 0.95  
    assert calcula_desconto(50) == 0.95 
    assert calcula_desconto(100) == 0.90  
    assert calcula_desconto(500) == 0.90  
    assert calcula_desconto(1000) == 0.85  
    assert calcula_desconto(5000) == 0.85  

def test_calcula_valor_total():
    assert calcula_valor_total(10, 1.0, 5) == 50.00  
    assert calcula_valor_total(10, 0.95, 10) == 95.00  
    assert calcula_valor_total(10, 0.90, 100) == 900.00  
    assert calcula_valor_total(10, 0.85, 1000) == 8500.00  

def test_calcula_valor_sem_desconto():
    assert calcula_valor_sem_desconto(10, 5) == 50.00  
    assert calcula_valor_sem_desconto(10, 10) == 100.00  
    assert calcula_valor_sem_desconto(10, 100) == 1000.00  
    assert calcula_valor_sem_desconto(10, 1000) == 10000.00  
'''


'''                   02                                '''

import pytest
from pytest_M4S3_funcoes import lanches

def lanches():
    assert lanches(100) == 100





