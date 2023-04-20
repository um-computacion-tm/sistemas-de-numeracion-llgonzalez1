import unittest
from sistemas_numeracion import decimal_binario
class TestDecimalBianrio(unittest.TestCase):
    def test_uno(self):
        resultado = decimal_binario(10)
        self.assertEqual(1010, resultado)
if __name__ == '__main__':
    unittest.main()