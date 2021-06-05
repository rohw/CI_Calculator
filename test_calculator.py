"""
test for calculator app
"""
import calculator


class TestCalculatorApp:
    def test_add(self):
        assert 5 == calculator.add(3, 2)

    def test_subtract(self):
        assert 5 == calculator.subtract(10, 5)

    def test_multiply(self):
        assert 50 == calculator.multiply(10, 5)

    def test_division(self):
        assert 2 == calculator.div(10, 5)
