class Cliente:
    def __init__(self, nome, possui_filhos):
        self.nome = nome
        self.possui_filhos = possui_filhos

class Imovel:
    def __init__(self, valor_base):
        self.valor_base = valor_base

class Apartamento(Imovel):
    def __init__(self, valor_base, quantidade_quartos, tem_garagem):
        super().__init__(valor_base)
        self.quantidade_quartos = quantidade_quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self, cliente):
        valor = self.valor_base
        if self.quantidade_quartos == 2:
            valor = valor + 200

        if self.tem_garagem:
            valor = valor + 300

        if not cliente.possui_filhos:
            valor = valor * 0.95

        return valor
    
class Casa(Imovel):
    def __init__(self, valor_base, quantidade_quartos, tem_garagem):
        super().__init__(valor_base)
        self.quantidade_quartos = quantidade_quartos
        self.tem_garagem = tem_garagem

    def calcular_aluguel(self, cliente):
        valor = self.valor_base

        if self.quantidade_quartos == 2:
            valor = valor + 250

        if self.tem_garagem:
            valor = valor + 300

        return valor
    
class Estudio(Imovel):
    def __init__(self, valor_base, tem_estacionamento, quantidade_vagas_extras):
        super().__init__(valor_base)
        self.tem_estacionamento = tem_estacionamento
        self.quantidade_vagas_extras = quantidade_vagas_extras

    def calcular_aluguel(self, cliente):
        valor = self.valor_base

        if self.tem_estacionamento:
            valor = valor + 250

            if self.quantidade_vagas_extras > 0:
                valor = valor + (self.quantidade_vagas_extras * 60)

        return valor

