import pytest

from logica import dividir, multiplicar, restar, sumar


@pytest.mark.parametrize("num, num2, resultado", [
    (2, 3, 5),
    (2, -3, -1),
    (-2, -3, -5), 
    (2, 0, 2), 
    (-2, 0, -2)
    ])
    
    
def test_probar_suma_parametrizada(num, num2, resultado):
    assert sumar (num, num2) == resultado
    
    
    
def test_probar_resta_positivos():
    assert restar (2, 3) == -1
    
def test_probar_resta_negativos():
    assert restar (-2, -3) == 1
    
def test_probar_resta_mixta():
    assert restar (-2, 3) == -5

def test_restar_cero():
    assert restar (2, 0) == 2
    
def test_probar_multiplicar_positivos():
    assert multiplicar (2, 3) == 6
    
def test_probar_multiplicar_negativos():
    assert multiplicar (-2, -3) == 6
    
def test_probar_multiplicar_mixta():
    assert multiplicar (-2, 3) == -6

def test_multiplicar_cero():
    assert multiplicar (2, 0) == 0
    
def test_probar_dividir_positivos():
    assert dividir (12, 3) == 4
    
def test_probar_dividir_negativos():
    assert dividir (-12, -3) == 4
    
def test_probar_dividir_mixta():
    assert dividir (-12, 3) == -4

def test_dividir_cero():
    with pytest.raises(ValueError):
     dividir (2, 0)
    