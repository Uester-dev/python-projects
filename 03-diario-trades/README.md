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

## Validação de entradas

O programa não quebra com dados inválidos:

- Letras ou opções inexistentes no menu mostram um aviso e voltam ao menu.
- O ativo não pode ficar vazio, e é gravado em maiúsculas e sem espaços sobrando.
- A direção aceita apenas C ou V (maiúscula ou minúscula) e é gravada em maiúscula.
- O resultado precisa ser um número. Se não for, a pergunta se repete até a digitação correta.
- A listagem e o resumo avisam quando ainda não há trades registrados.

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
- Menu em loop com `while` e `if/elif/else`
- Tratamento de erros com `try/except`
- Validação de entradas com `while True` e `break`
- Métodos de texto (`.upper()` e `.strip()`)
- Acumuladores e contadores, conversão de texto em número com `float`
- Cuidado com divisão por zero
- Formatação de saída com f-strings
- Testes manuais de casos extremos e depuração de erros (`KeyError`, modo de arquivo errado, arquivo antigo com cabeçalho diferente)

## Próximos passos

- Registrar a data de cada trade automaticamente
- Rejeitar valores como `nan` e `inf` no resultado
- Permitir editar ou apagar um trade
