import pandas as pd

df_consorcio = pd.read_csv("dados_exemplo/consorcio_detalhes.csv")
df_contrato = pd.read_csv("dados_exemplo/produtos_contratados.csv")

df_merge = df_consorcio.merge(df_contrato, on="contrato_id")
df_consorcio_filtrado = df_merge[df_merge["categoria_produto"] == "consorcio"]

df_mensal = df_consorcio_filtrado.groupby(["ano", "mes"]).agg(
    volume=("contrato_id", "count"),
    media_valor_bem=("valor_bem", "mean"),
    clientes_distintos=("cliente_id", "nunique")
).reset_index()

df_jun_25 = df_mensal[(df_mensal["ano"] == 2025) & (df_mensal["mes"] == 6)]
df_jun_26 = df_mensal[(df_mensal["ano"] == 2026) & (df_mensal["mes"] == 6)]

df_ytd_25 = df_mensal[(df_mensal["ano"] == 2025) & (df_mensal["mes"] <= 6)]
df_ytd_26 = df_mensal[(df_mensal["ano"] == 2026) & (df_mensal["mes"] <= 6)]

df_comparativo = pd.concat([df_jun_25, df_jun_26])
df_ytd = pd.concat([df_ytd_25, df_ytd_26])

with pd.ExcelWriter("relatorio_consorcio.xlsx") as writer:
    df_comparativo.to_excel(writer, sheet_name="Comparativo Jun", index=False)
    df_ytd.to_excel(writer, sheet_name="YTD Jan-Jun", index=False)

    print(df_jun_25)