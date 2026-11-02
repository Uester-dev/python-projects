import os
import csv

nome_arq = "trades.csv"
cabecalho = ["ativo","direcao","resultado"]
if (not os.path.exists(nome_arq)):
    with open(nome_arq, "w", newline="", encoding="utf-8") as csv_arq:
        escritor = csv.DictWriter(csv_arq, fieldnames=cabecalho)
        escritor.writeheader()

op = 0
while (op != 4):
    os.system("cls")
    print("DIÁRIO DE TRADES")
    print("1 - Registrar trade")
    print("2 - Listar trades")
    print("3 - Resumo")
    print("4 - Sair")
    op = int(input("Informe o número da opção escolhida: "))
    if (op == 1):
        print("REGISTRAR TRADE")
        ativo = input("Ativo: ")
        direcao = input("Direção (C/V): ")
        resultado = float(input("Resultado da operação: "))
        dados = {"ativo": ativo, "direcao": direcao, "resultado": resultado}
        with open(nome_arq, "a", newline="", encoding="utf-8") as csv_arq:
            escritor = csv.DictWriter(csv_arq, fieldnames=cabecalho)
            escritor.writerow(dados)
        input("Trade registrado! Pressione ENTER para retornar ao menu")
    elif (op == 2):
        print("LISTAR TRADES")
        with open(nome_arq, "r", newline="", encoding="utf-8") as csv_arq:
            leitor = csv.DictReader(csv_arq)
            cont = 0
            for linha in leitor:
                cont += 1
                print(f"Registro {cont} = {linha['ativo']} - {linha['direcao']} - {linha['resultado']}")
            input("Pressione ENTER para retornar ao menu")
    elif (op == 3):
        print("RESUMO")
        total_de_trades = 0
        soma_dos_resultados = 0
        trades_positivos = 0
        with open(nome_arq, "r", newline="", encoding="utf-8") as csv_arq:
            leitor = csv.DictReader(csv_arq)
            for linha in leitor:
                total_de_trades += 1
                soma_dos_resultados += float(linha['resultado'])
                if (float(linha["resultado"]) > 0):
                    trades_positivos += 1
            if (total_de_trades == 0):
                print("Não foram registrados trades")    
            else:
                tx_de_acerto = (trades_positivos / total_de_trades) * 100
                print(f"Foram registrados {total_de_trades} trades")
                print(f"Resultado: ${soma_dos_resultados}")
                print(f"Taxa de acerto de {tx_de_acerto:.2f}%")
            input("Pressione ENTER para retornar ao menu")
