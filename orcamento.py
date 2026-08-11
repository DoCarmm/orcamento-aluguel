class Orcamento:
    def __init__(self, valor_aluguel, quantidade_parcelas_contrato):
        self.valor_aluguel = valor_aluguel
        self.quantidade_parcelas_contrato = quantidade_parcelas_contrato

    def validar_parcelas(self):
        if 1 <= self.quantidade_parcelas_contrato <= 5:
            return True
        else:
            return False

    def calcular_parcela_contrato(self):
        valor_contrato = 2000

        if self.validar_parcelas():
            valor_parcela = valor_contrato / self.quantidade_parcelas_contrato
            return valor_parcela
        else:
            raise ValueError("Quantidade de parcelas inválida. Escolha entre 1 e 5 parcelas.")

    def gerar_parcelas(self):
        parcela = 1
        valor_parcela_contrato = self.calcular_parcela_contrato()
        parcelas = []

        while parcela <= 12:
            
            if parcela <= self.quantidade_parcelas_contrato:
                parcela_atual = self.valor_aluguel + valor_parcela_contrato
            else:
                parcela_atual = self.valor_aluguel

            parcelas.append(parcela_atual)

            parcela = parcela + 1

        return parcelas

