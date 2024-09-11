from sistema_bancario.conta import ContaBancaria


class SistemaBancario:
    def __init__(self):
        self._contas = {}

    def criar_conta(self, num_conta, dono, saldo_inicial=0.0):
        if num_conta in self._contas:
            raise ValueError("Conta já existe.")
        nova_conta = ContaBancaria(num_conta, dono, saldo_inicial)
        self._contas[num_conta] = nova_conta
        print(f"Conta criada com sucesso: {nova_conta}, Saldo: {saldo_inicial}")

    def ver_conta(self, num_conta):
        conta = self._contas.get(num_conta)
        if not conta:
            raise ValueError(f"Essa conta {num_conta} não existe.")
        return conta

    def listar_contas(self):
        print("Lista de contas:")
        for conta in self._contas.values():
            print(conta)
