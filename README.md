# Orçamento de Aluguel - Imobiliária R.M.

Projeto desenvolvido em Python para automatizar a geração de orçamentos de locação da Imobiliária R.M.

A aplicação utiliza Programação Orientada a Objetos para representar diferentes tipos de imóveis, calcular o valor mensal do aluguel, aplicar adicionais e descontos, calcular o parcelamento do contrato e gerar um arquivo CSV com as 12 parcelas do orçamento.

## Funcionalidades

- Cadastro dos dados do cliente
- Escolha entre Apartamento, Casa e Estúdio
- Cálculo automático do valor do aluguel
- Adicional de quartos para Apartamento e Casa
- Adicional de garagem para Apartamento e Casa
- Estacionamento e vagas extras para Estúdio
- Desconto de 5% para Apartamento quando o cliente não possui filhos
- Parcelamento do contrato de R$ 2.000,00 entre 1 e 5 vezes
- Geração das 12 parcelas do orçamento
- Exportação das parcelas para arquivo CSV
- Validação das entradas informadas pelo usuário

## Regras de negócio

### Apartamento
- Valor-base: R$ 700,00
- 2 quartos: adicional de R$ 200,00
- Garagem: adicional de R$ 300,00
- Cliente sem filhos: desconto de 5%

### Casa
- Valor-base: R$ 900,00
- 2 quartos: adicional de R$ 250,00
- Garagem: adicional de R$ 300,00

### Estúdio
- Valor-base: R$ 1.200,00
- Pacote de estacionamento com 2 vagas: R$ 250,00
- Cada vaga extra: R$ 60,00

### Contrato
- Valor do contrato: R$ 2.000,00
- Parcelamento entre 1 e 5 vezes
- O orçamento é gerado para 12 parcelas

## Tecnologias utilizadas

- Python
- Programação Orientada a Objetos
- Biblioteca `csv`
- Git
- GitHub

## Estrutura do projeto

```text
orcamento-aluguel/
├── main.py
├── modelos.py
├── orcamento.py
├── exportador.py
├── funcoes.py
├── orcamento.csv
├── .gitignore
└── README.md
```

## Como executar

Com o Python instalado, abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

Depois, informe os dados solicitados pelo programa.

Ao final da execução, será gerado o arquivo `orcamento.csv` contendo as 12 parcelas do orçamento.

## Exemplo de resultado

```text
Orçamento gerado com sucesso.
Valor mensal do aluguel: R$ 1.140,00
Contrato parcelado em 5x de R$ 400,00
Arquivo CSV gerado: orcamento.csv
```

## Conceitos utilizados

Durante o desenvolvimento foram utilizados conceitos de Programação Orientada a Objetos, como:

- Classes e objetos
- Atributos
- Métodos
- Herança
- Sobrescrita de métodos

Também foram utilizados tratamento de exceções, funções auxiliares e manipulação de arquivos CSV.

## Autor

Andrey Vitor Nascimento do Carmo

Projeto desenvolvido para a disciplina de Algorithmic Thinking & Introduction to Object-Oriented Programming.
