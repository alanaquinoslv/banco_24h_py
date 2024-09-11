from datetime import datetime


class Transacao:
    def __init__(self, tipo_transacao, valor):
        self.tipo_transacao = tipo_transacao
        self.valor = valor
        self.data = datetime.now()

    def __str__(self) -> str:
        return f"{self.tipo_transacao} de {self.valor} em {self.data.strftime('%d/%m/%Y %H:%M:%S')}"