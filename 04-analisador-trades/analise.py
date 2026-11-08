import os
import pandas as pd
import matplotlib.pyplot as plt

os.system("cls")

pasta = os.path.dirname(__file__)
arquivo_csv = os.path.join(pasta, "trades_exemplo.csv")

df = pd.read_csv(arquivo_csv)

num_trades = len(df)
print(f"Foram registrados {num_trades} trades")
somatorio = df["resultado"].sum()
print(f"O resultado final foi de ${somatorio:.2f}")
media = df["resultado"].mean()
print(f"O valor médio por trade é de ${media:.2f}")
maior = df["resultado"].max()
print(f"O maior resultado foi de ${maior:.2f}")
menor = df["resultado"].min()
print(f"O menor resultado foi de ${menor:.2f}")
verif_vencedores = df["resultado"] > 0
vencedores = verif_vencedores.sum()
print(f"A quantidade de resultados vencedores foi de {vencedores}")
tx_acerto = vencedores / num_trades * 100
print(f"A taxa de acerto foi de {tx_acerto:.2f}%")
acumulado = df["resultado"].cumsum()
plt.plot(range(1, len(df) + 1),acumulado)
plt.title("Resultado acumulado")
plt.xlabel("Número de trades")
plt.ylabel("Resultado acumulado ($)")
plt.grid(True)
plt.axhline(0)

agrupar_ativos = df.groupby("ativo")
calcular_ativos = agrupar_ativos["resultado"].agg(["sum","mean","count"])
ordenar_ativos = calcular_ativos.sort_values("sum", ascending=False)
arredondar_ativos = ordenar_ativos.round(2)
ativo_lucrativo = ordenar_ativos["sum"].idxmax()
print(arredondar_ativos)
print(f"O ativo mais lucrativo foi {ativo_lucrativo}")

maior_acumulado = acumulado.cummax()
queda = acumulado - maior_acumulado
dd_max = queda.min()
print(f"O pico do saldo foi de ${maior_acumulado.max():.2f}")
print(f"O DD máximo foi de ${dd_max:.2f}")

arquivo_img = os.path.join(pasta, "grafico.png")
plt.savefig(arquivo_img)
plt.show()