# Invariante de laço

## Marge-sort  O(n log n)

O Marge-sort é um algoritmo de ordenação eficiente que divide recursivamente uma lista não ordenada pela metade, ordena cada metade e depois mescla as duas metades ordenadas. Sua notação O() é O(n log n), o que significa que sua complexidade de tempo é proporcional a n vezes o logaritmo de n, onde n é o número de elementos a serem ordenados. Isso o torna eficiente para grandes conjuntos de dados.

## Selection-sort  O(n^2)

Selecione o menor colocamos na primeira posição ou selecionamos o maior e colocamos na ultima posição.

A cada interação  os valores de l ate [0....i] são os i + 1 menores valores e estao ordenados.

## Bubble-sort  O(n^2)

Ele percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. Após cada iteração, o maior elemento flutua para o final da lista. Essa repetição continua até que não seja necessário fazer mais trocas, o que indica que a lista está ordenada. A complexidade de tempo do Bubble Sort é O(n^2) no pior caso. As trocas consomem muito processamento

## Inserction-sort  O(n^2)

O Insertion-sort é um algoritmo de ordenação simples que percorre a lista da esquerda para a direita, inserindo cada elemento na posição correta entre os elementos já ordenados. Sua notação O() é O(n^2), o que significa que sua complexidade de tempo é proporcional a n ao quadrado, onde n é o número de elementos a serem ordenados. Isso o torna menos eficiente do que algoritmos como o Marge-sort para grandes conjuntos de dados, mas pode ser mais eficiente para conjuntos de dados pequenos.
