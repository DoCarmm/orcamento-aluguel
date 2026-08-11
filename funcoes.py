def ler_sim_nao(mensagem):
    resposta = input(mensagem).strip().lower()

    while resposta != "s" and resposta != "n":
        print("Você deve responder com s ou n.")
        resposta = input(mensagem).strip().lower()

    if resposta == "s":
        return True
    else:
        return False

def ler_quantidade_quartos():
    while True:
        try:
            quantidade_quartos = int(input("Digite a quantidade de quartos (1 ou 2): "))

            if quantidade_quartos == 1 or quantidade_quartos == 2:
                return quantidade_quartos
            else:
                print("A quantidade de quartos precisa ser 1 ou 2.")

        except ValueError:
            print("Digite apenas números.")

def ler_quantidade_parcelas():
    while True:
        try:
            quantidade_parcelas = int(
                input("Em quantas parcelas deseja dividir o contrato? (1 a 5): ")
            )

            if 1 <= quantidade_parcelas <= 5:
                return quantidade_parcelas
            else:
                print("A quantidade de parcelas precisa ser entre 1 e 5.")

        except ValueError:
            print("Digite apenas números.")

def ler_quantidade_vagas_extras():
    while True:
        try:
            quantidade_vagas_extras = int(
                input("Quantas vagas extras você quer? ")
            )

            if quantidade_vagas_extras > 0:
                return quantidade_vagas_extras
            else:
                print("A quantidade de vagas extras deve ser pelo menos 1.")

        except ValueError:
            print("Digite apenas números.")

def formatar_moeda(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")

    return f"R$ {valor_formatado}"

