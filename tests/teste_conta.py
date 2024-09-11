import unittest
from sistema_bancario.conta import ContaBancaria

class TesteContaBancaria(unittest.TestCase):
    def setUp(self):
        self.conta = ContaBancaria(123, "João", 500)

    def teste_deposito(self):
        self.conta.depositar(500)
        self.assertEqual(self.conta.saldo, 1000)

    def teste_saque(self):
        self.conta.sacar(200)
        self.assertEqual(self.conta.saldo, 300)

    def teste_saldo_insuficiente(self):
        with self.assertRaises(ValueError):
            self.conta.sacar(1000)

    def teste_deposito_invalido(self):
        with self.assertRaises(ValueError):
            self.conta.depositar(-100)

if __name__ == "__main__":
    unittest.main()
