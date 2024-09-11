from sistema_bancario.sistema import SistemaBancario


def main():
    banco = SistemaBancario()

    banco.criar_conta(123, "João", 500)

    conta_joao = banco.ver_conta(123)
    conta_joao.depositar(500)
    conta_joao.sacar(200)
    conta_joao.extrato()


if __name__ == "__main__":
    main()
