# Diário de Trades

Meu terceiro projeto em Python. Um diário de operações para trading, com menu no terminal: registra os trades, guarda tudo em um arquivo CSV e mostra um resumo com o resultado acumulado e a taxa de acerto. Os dados continuam salvos depois de fechar o programa.

## Como funciona

Menu principal:

1. **Registrar trade:** pede o ativo, a direção (C/V) e o resultado da operação, e grava no arquivo.
2. **Listar trades:** mostra todos os trades registrados, numerados.
3. **Resumo:** mostra o total de trades, o resultado acumulado e a taxa de acerto.
4. **Sair**

Os trades ficam no arquivo `trades.csv`, criado automaticamente (com cabeçalho) na primeira execução:

```
ativo,direcao,resultado
EURUSD,C,25.5
XAUUSD,V,-10.0
```

A taxa de acerto é calculada assim:

```
taxa de acerto = (trades positivos / total de trades) * 100
```

Exemplo: trades de +10, -5 e +20 resultam em 3 trades, $25 de resultado e 66,67% de acerto.

## Como executar

Requisito: Python 3 instalado. Entre na pasta do projeto e rode:

```
python diario.py
```

O arquivo `trades.csv` é criado na pasta de onde o programa é executado.

## O que pratiquei

- Leitura e escrita de arquivos CSV (`csv.DictWriter` e `csv.DictReader`)
- Modos de abertura de arquivo (`"w"`, `"a"`, `"r"`) e o bloco `with`
- Dicionários (chave e valor) para representar cada trade
- Menu em loop com `while` e `if/elif`
- Acumuladores e contadores, conversão de texto em número com `float`
- Cuidado com divisão por zero
- Formatação de saída com f-strings
- Depuração de erros (`KeyError`, modo de arquivo errado, arquivo antigo com cabeçalho diferente)

## Próximos passos

- Tratar entradas inválidas (letras no lugar de números) com `try/except`
- Registrar a data de cada trade automaticamente
- Avisar quando não houver trades na listagem
- Validar a direção (aceitar apenas C ou V)