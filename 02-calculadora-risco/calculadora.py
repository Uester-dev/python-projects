import os

os.system("cls" if os.name == "nt" else "clear")
def calcular_risco(saldo, risco_percent):
    return round(saldo * (risco_percent / 100), 2)

def calcular_lote(dinheiro_em_risco, stop_em_pips, valor_pip):
    return round(dinheiro_em_risco / (stop_em_pips * valor_pip), 2)

print("CALCULADORA DE LOTE E RISCO")

sair = "s"
while (sair == "s"):
    saldo = float(input("Saldo atual da conta: "))
    risco_percent = float(input("Risco % por operação: "))
    stop_em_pips = int(input("Tamanho do stop em pips: "))
    valor_pip = float(input("Valor do pip por lote: "))

    if (stop_em_pips <= 0) or (valor_pip <= 0):
        print("Erro: o stop e o valor do pip precisam ser maiores que zero.")
        continue

    dinheiro_em_risco = calcular_risco(saldo, risco_percent)
    lote = calcular_lote(dinheiro_em_risco, stop_em_pips, valor_pip)
    print(f"O valor que será arriscado é de ${dinheiro_em_risco}")
    print(f"O lote é de {lote}")
    sair = input("Deseja continuar (s/n)?: ").lower()