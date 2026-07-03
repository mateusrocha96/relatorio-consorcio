# Relatório de Consórcio

Script Python que lê bases de venda de consórcio e gera um Excel comparativo mês a mês (jun/25 vs jun/26) e YTD (jan-jun), com volume de contratos, média de valor de carta e clientes distintos.

Base sintética simulando operação de consórcio e cartões PF.

## O que ele faz

1. Lê `consorcio_detalhes.csv` e `produtos_contratados.csv` da pasta `dados_exemplo/`
2. Cruza as bases por `contrato_id`
3. Calcula volume, média de valor de carta e clientes distintos por mês
4. Exporta `relatorio_consorcio.xlsx` com duas abas: Comparativo Jun e YTD Jan-Jun

## Estrutura de pastas

```
relatorio-consorcio/
├── dados_exemplo/
│   ├── consorcio_detalhes.csv
│   └── produtos_contratados.csv
├── relatorio_consorcio.py
├── .gitignore
└── README.md
```

## Como rodar

```
python relatorio_consorcio.py
```

O arquivo `relatorio_consorcio.xlsx` será gerado na mesma pasta do script.

## Substituindo pelos seus dados

Substitua os arquivos em `dados_exemplo/` pelos seus próprios CSVs, mantendo os mesmos nomes de colunas.
