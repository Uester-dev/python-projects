import os
import csv

nome_arq = "trades.csv"
cabecalho = ["ativo","direcao","resultado"]
if (not os.path.exists(nome_arq)):
    with open(nome_arq, "w", newline="", encoding="utf-8") as csv_arq:
        escritor = csv.DictWriter(csv_arq, fieldnames=cabecalho)
        escritor.writeheader()

while (True):
    os.system("cls")
    print("DIÁRIO DE TRADES")
    print("1 - Registrar trade")
    print("2 - Listar trades")
    print("3 - Resumo")
    print("4 - Sair")
    try:
        op = int(input("Informe o número da opção escolhida: "))
    except ValueError:
        op = 0
    if (op == 1):
        print("REGISTRAR TRADE")
        while (True):
            ativo = input("Ativo: ").upper().strip()
            if (ativo != ""):
                break
            print("É preciso que você digite o nome do ativo!")
            input("Pressione ENTER para continuar")
        while (True):
            direcao = input("Direção (C/V): ").upper().strip()
            if (direcao != "C" and direcao != "V"):
                print("Só serão aceitas as letras C ou V!")
                input("Pressione ENTER para continuar")
            else:
                break
        while (True):
            try:
                resultado = float(input("Resultado da operação: "))
                break
            except ValueError:
                print("Digite apenas números!")
                input("Pressione ENTER para continuar")        
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
            if (cont == 0):
                print("Nada registrado ainda!")
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
                print(f"Resultado: ${soma_dos_resultados:.2f}")
                print(f"Taxa de acerto de {tx_de_acerto:.2f}%")
            input("Pressione ENTER para retornar ao menu")
    elif (op == 4):
        break
    else:
        print("Digite apenas os números indicados no menu!")
        input("Pressione ENTER para retornar ao menu")