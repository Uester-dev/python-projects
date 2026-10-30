# Jogo de Adivinhar o Número

Meu primeiro projeto em Python. O computador sorteia um número de 1 a 100 e o jogador tenta acertar, com dicas de "maior" ou "menor" a cada palpite.

## Como funciona

- O jogador define quantas tentativas deseja ter.
- A cada palpite, o jogo informa se o número sorteado é maior ou menor.
- O jogo mostra quantas tentativas ainda restam.
- Se o jogador acertar, vence. Se as tentativas acabarem, aparece "GAME OVER" e o número sorteado é revelado.

## Como executar

Requisito: Python 3 instalado.

```
python jogo.py
```

## O que pratiquei

- Entrada e saída de dados (`input`, `print`, f-strings)
- Conversão de tipos (`int`)
- Números aleatórios (`random`)
- Condicionais (`if`, `elif`, `else`)
- Laços de repetição (`while`) e operadores lógicos (`and`)
- Depuração de erros de lógica

## Próximos passos

- Tratar entradas inválidas (por exemplo, letras no lugar de números) com `try/except`
- Adicionar níveis de dificuldade