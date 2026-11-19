import pytest

from logica import dividir, multiplicar, restar, sumar


# suma
@pytest.mark.parametrize(
    "num, num2, resultado",
    [(2, 3, 5), (2, -3, -1), (-2, -3, -5), (2, 0, 2), (-2, 0, -2)],
)
def test_probar_suma_parametrizada(num, num2, resultado):
    assert sumar(num, num2) == resultado


# resta
@pytest.mark.parametrize(
    "num, num2, resultado",
    [(2, 3, -1), (2, -3, 5), (-2, -3, 1), (2, 0, 2), (-2, 0, -2)],
)
def test_resta_parametrizada(num, num2, resultado):
    assert restar(num, num2) == resultado


# multiplicar
@pytest.mark.parametrize(
    "num, num2, resultado", [(2, 3, 6), (-2, -3, 6), (-2, 3, -6), (2, 0, 0)]
)
def test_multiplicacion_parametrizada(num, num2, resultado):
    assert multiplicar(num, num2) == resultado


# division
@pytest.mark.parametrize(
    "num, num2, resultado",
    [
        (12, 3, 4.0),
        (-12, -3, 4.0),
        (12, -3, -4.0),
        (0, 5, 0),
    ],
)
def test_division_parametrizada(num, num2, resultado):
    assert dividir(num, num2) == resultado
    
    
def test_dividir_cero():
    with pytest.raises(ValueError):
        dividir(2, 0)
