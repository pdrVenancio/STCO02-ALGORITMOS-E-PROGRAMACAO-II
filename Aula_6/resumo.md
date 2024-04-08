# Invariante de leço

## Selection-sort == O(n^2)
    Selecione o menor colocamos na primeira posição ou selecionamos o maior e colocamos na ultima posição.
    A cada interação  os valores de l ate [0....i] são os i + 1 menores valores e estao ordenados.

## Bubble-sort == O(n^2)
    Ele percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. Após cada iteração, o maior elemento flutua para o final da lista. Essa repetição continua até que não seja necessário fazer mais trocas, o que indica que a lista está ordenada. A complexidade de tempo do Bubble Sort é O(n^2) no pior caso. As trocas consomem muito processamento