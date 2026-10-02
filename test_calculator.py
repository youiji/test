import pytest
from calculator import calculate_commission

# Тесты для диапазона: от 100 до 1 000 руб.
@pytest.mark.parametrize("amount, expected", [
    (100, 50.0),       # Нижняя граница (минимум)
    (500, 50.0),       # Обычное значение в диапазоне
    (1000, 50.0),      # Верхняя граница
])
def test_commission_up_to_1000(amount, expected):
    assert calculate_commission(amount) == expected

# Тесты для диапазона: от 1 001 до 20 000 руб.
@pytest.mark.parametrize("amount, expected", [
    (1001, 100.0),     # Нижняя граница второго диапазона
    (10000, 100.0),    # Обычное значение
    (20000, 100.0),    # Верхняя граница
])
def test_commission_up_to_20000(amount, expected):
    assert calculate_commission(amount) == expected

# Тесты для диапазона: от 20 001 до 50 000 руб.
@pytest.mark.parametrize("amount, expected", [
    (20001, 400.01),   # Нижняя граница (200 + 20001*0.01)
    (35000, 550.0),    # Обычное значение (200 + 35000*0.01)
    (50000, 700.0),    # Верхняя граница всего сервиса (200 + 50000*0.01)
])
def test_commission_above_20000(amount, expected):
    assert calculate_commission(amount) == expected

# Тесты проверки исключений (недопустимые значения)
@pytest.mark.parametrize("invalid_amount", [
    99,                # Чуть меньше нижней границы
    0,                 # Ноль
    -500,              # Отрицательное число
    50001,             # Чуть больше верхней границы
    100000,            # Сильно больше
])
def test_commission_invalid_amount(invalid_amount):
    # Проверяем, что функция вызывает ValueError с правильным текстом
    with pytest.raises(ValueError, match="Сумма перевода должна быть от 100 до 50 000 руб."):
        calculate_commission(invalid_amount)