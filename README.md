# Relatório de Consórcio

Script Python que lê bases de venda de consórcio e gera um Excel comparativo mês a mês (jun/25 vs jun/26) e YTD (jan-jun), com volume de contratos, média de valor de carta e clientes distintos.

Base sintética simulando operação de consórcio e cartões PF.

## O que ele faz

1. Lê os arquivos `consorcio_detalhes.csv` e `produtos_contratados.csv`
2. Cruza as bases por `contrato_id`
3. Calcula volume, média de valor de carta e clientes distintos por mês
4. Exporta `relatorio_consorcio.xlsx` com duas abas: Comparativo Jun e YTD Jan-Jun

## Arquivos necessários

- `consorcio_detalhes.csv`
- `produtos_contratados.csv`

## Como rodar

Coloque os dois arquivos na mesma pasta do script e execute:

```
python relatorio_consorcio.py
```
