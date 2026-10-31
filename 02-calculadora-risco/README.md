# Calculadora de Lote e Risco

Meu segundo projeto em Python. Uma calculadora de gerenciamento de risco para trading: a partir do saldo da conta, do risco por operação e do tamanho do stop, o programa informa quanto dinheiro será arriscado e qual lote usar.

## Como funciona

O programa pede quatro dados:

- Saldo atual da conta
- Risco por operação (%)
- Tamanho do stop em pips
- Valor do pip por lote

E calcula:

```
dinheiro_em_risco = saldo * (risco_percentual / 100)
lote = dinheiro_em_risco / (stop_em_pips * valor_do_pip)
```

Exemplo: saldo 1000, risco 1%, stop de 20 pips e pip de 10 por lote resultam em $10 arriscados e lote 0.05.

O valor do pip por lote varia conforme o ativo e a corretora, por isso ele é informado pelo usuário. Após cada cálculo, o programa pergunta se o usuário deseja continuar.

## Como executar

Requisito: Python 3 instalado.

```
python calculadora.py
```

## O que pratiquei

- Criação de funções com parâmetros e `return`
- Números decimais (`float`) e arredondamento com `round`
- Laços de repetição (`while`) e `continue`
- Validação de dados de entrada (evitar divisão por zero)
- Tratamento de maiúsculas e minúsculas com `.lower()`
- Testes de casos extremos, como stop igual a zero

## Próximos passos

- Tratar entradas inválidas (letras no lugar de números) com `try/except`
- Arredondar o lote para baixo, como fazem as corretoras
- Avisar quando o lote calculado for menor que o mínimo permitido