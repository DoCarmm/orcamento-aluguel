from modelos import Cliente, Apartamento, Casa, Estudio
from orcamento import Orcamento
from exportador import ExportadorCSV
from funcoes import (ler_sim_nao, ler_quantidade_quartos, ler_quantidade_parcelas, ler_quantidade_vagas_extras, formatar_moeda,)

nome = input("Digite o nome do cliente: ")
possui_filhos = ler_sim_nao("O cliente possui filhos? (s/n): ")

cliente = Cliente(nome, possui_filhos)

tipo_imovel = input("Qual tipo de imóvel você deseja?\n" 
"1 - Apartamento\n" 
"2 - Casa\n"
"3 - Estúdio\n"
"Escolha uma opção: "
)

while tipo_imovel not in ("1", "2", "3"):
    print("Opção inválida. Escolha 1, 2 ou 3.")
    tipo_imovel = input(
    "Qual tipo de imóvel você deseja?\n" 
    "1 - Apartamento\n" 
    "2 - Casa\n"
    "3 - Estúdio\n"
    "Escolha uma opção: "
    )

if tipo_imovel == "1":
    quantidade_quartos = ler_quantidade_quartos()

    tem_garagem = ler_sim_nao("Você quer garagem no seu apartamento? (s/n): ")

    imovel = Apartamento(700, quantidade_quartos, tem_garagem)

elif tipo_imovel == "2":
    quantidade_quartos = ler_quantidade_quartos()

    tem_garagem = ler_sim_nao("Você quer garagem na sua casa? (s/n): ")
    
    imovel = Casa(900, quantidade_quartos, tem_garagem)

elif tipo_imovel == "3":
    tem_estacionamento = ler_sim_nao("Você quer estacionamento no seu estúdio? (s/n): ")

    if tem_estacionamento:
        quer_vagas_extras = ler_sim_nao("Você quer vagas extras no seu estúdio? (s/n): ")

        if quer_vagas_extras:
            quantidade_vagas_extras = ler_quantidade_vagas_extras()

        else:
            quantidade_vagas_extras = 0

    else:
        quantidade_vagas_extras = 0

    imovel = Estudio(1200, tem_estacionamento, quantidade_vagas_extras)

valor_aluguel = imovel.calcular_aluguel(cliente)

quantidade_parcelas_contrato = ler_quantidade_parcelas()

orcamento = Orcamento(valor_aluguel, quantidade_parcelas_contrato)

valor_parcela_contrato = orcamento.calcular_parcela_contrato()

parcelas = orcamento.gerar_parcelas()

exportador = ExportadorCSV()
exportador.exportar(parcelas)

print(
    f"Orçamento gerado com sucesso.\n"
    f"Valor mensal do aluguel: {formatar_moeda(valor_aluguel)}\n"
    f"Contrato parcelado em {quantidade_parcelas_contrato}x de "
    f"{formatar_moeda(valor_parcela_contrato)}\n"
    f"Arquivo CSV gerado: orcamento.csv"
)

