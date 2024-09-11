class ContaBancaria:
    def __init__(self, num_conta, dono, saldo_inicial=0.0):
        self._num_conta = num_conta
        self._dono = dono
        self._saldo = saldo_inicial
        self._transacoes = []

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self._saldo += valor
        self._transacoes.append(f"Depositado {valor}")
        print(f"Depósito de {valor} efetuado com sucesso. Novo saldo: {self._saldo}")

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self._saldo:
            raise ValueError("Saldo insuficiente.")
        self._saldo -= valor
        self._transacoes.append(f"Sacado {valor}")
        print(f"Saque de {valor} efetuado com sucesso. Novo saldo: {self._saldo}")

    def extrato(self):
        print(f"Extrato da conta de {self._dono} (Conta: {self._num_conta})")
        for transacao in self._transacoes:
            print(transacao)
        print(f"Saldo atual: {self._saldo}")

    def __str__(self) -> str:
        return (
            f"Conta de ({self._dono}, Conta: {self._num_conta}, Saldo: {self._saldo})"
        )
