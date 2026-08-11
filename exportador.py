import csv

from funcoes import formatar_moeda

class ExportadorCSV:
    def exportar(self, parcelas):
        numero_parcela = 1

        with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(["Parcela", "Valor"])

            for valor in parcelas:
                escritor.writerow([numero_parcela, formatar_moeda(valor)])
                numero_parcela = numero_parcela + 1

