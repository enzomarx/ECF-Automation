import unittest
from src.automation import enviar_ecf

class TestAutomation(unittest.TestCase):
    def test_enviar_ecf(self):
        # 
        try:
            enviar_ecf('12345678000195', '01/2023')
        except Exception as e:
            self.fail(f"enviar_ecf raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
