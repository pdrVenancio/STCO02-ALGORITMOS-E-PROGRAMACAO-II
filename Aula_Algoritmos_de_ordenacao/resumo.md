# Invariante de laço

## Teorema

Todo algoritmo de oredenação baseado em comparação tem um tempo de pior caso O(n log n).

## Tim-sort

len(l) / run ==> é bom ser uma potencia de 2. Assim sabemos o número de niveis que vamos ter. Algoritmo usado quando damos .sort()

## Heap-sort

Ordenação através de fila de prioridade :Pega o maior, coloca na última posição,

pega o segundo maior coloca na penúltima posição.

Implementar o HEAP

    Inserção: O(logn)

    Remoção: O(logn)

    Pick: O(1)

Heap:

    -Árvore binária quase completa

    -Todos os níveis completamente preenchidos menos o último

    -Os elementos do último nível estão o mais a esquerda possível

    -Max heap: O pai sempre é maior que todos os filhos (O q vai ser usado)

    -Min heap: O pai sempre é menor que todos os filhos

O heap, por ser comportado, pode ser organizado em um vetor, de modo que cada índice representa o próximo elemento do heap.

    esq(i) = 2i + 1

    dir(i) = 2i + 2

    pai(i) = floor( (i-1)/2 )

-Se um elemento novo inserido e ele desequilibrar o heap, ele e seu pai devem ser trocados (será uma função recursiva)

COMO FUNCIONA A ORGANIZAÇÂO COM HEAP

-O elemento da raiz é sempre o maior. Retira-se ele e coloca como maior da lista ordenada

-desce_heap: Função que equilibra o heap é chamada

-> Dado um vetor, le-se ele como se fosse heap

-> Organiza o heap recursivamente

    -Todos os elementos do último nível estão de acordo com as regras do heap

    -Olha o penúltimo nível. Se um elemento e seus filhos não são heap, o pai sempre troca com o maior dos filhos

    -Continua assim recursivamente

-> Ao se ter a árvore equilibrada, retira-se o elemento da raiz, o guarda e diminui o tamanho do heap

-> Joga o último elemento do heap como a nova raíz

-> Joga o elemento guardado na última posição do vetor

-> Volta no segundo passo até que o vetor esteja organizado

-HeapSort é garantidamente nlogn e tudo é feito em apenas um vetor

-Porém as constantes deles são muito mais altas que o quickSort, mergeSort e timSort

## Quick-sort O(n log n)

O QuickSort é um algoritmo de ordenação eficiente que utiliza o método "dividir para conquistar". Ele seleciona um elemento como pivô, rearranja os elementos de forma que os menores que o pivô fiquem à esquerda e os maiores à direita, e então recursivamente ordena os subconjuntos. Sua complexidade média é O(n log n), mas pode degradar para O(n^2) em casos raros(quando o pivot é um valor "ruim" sendo o menor ou o maior valor).

## Marge-sort  O(n log n)

O Marge-sort é um algoritmo de ordenação eficiente que divide recursivamente uma lista não ordenada pela metade, ordena cada metade e depois mescla as duas metades ordenadas. Sua notação O() é O(n log n), o que significa que sua complexidade de tempo é proporcional a n vezes o logaritmo de n, onde n é o número de elementos a serem ordenados. Isso o torna eficiente para grandes conjuntos de dados.

## Selection-sort  O(n^2)

Selecione o menor colocamos na primeira posição ou selecionamos o maior e colocamos na ultima posição.

A cada interação  os valores de l ate [0....i] são os i + 1 menores valores e estao ordenados.

## Bubble-sort  O(n^2)

Ele percorre a lista várias vezes, comparando elementos adjacentes e trocando-os se estiverem na ordem errada. Após cada iteração, o maior elemento flutua para o final da lista. Essa repetição continua até que não seja necessário fazer mais trocas, o que indica que a lista está ordenada. A complexidade de tempo do Bubble Sort é O(n^2) no pior caso. As trocas consomem muito processamento

## Inserction-sort  O(n^2)

O Insertion-sort é um algoritmo de ordenação simples que percorre a lista da esquerda para a direita, inserindo cada elemento na posição correta entre os elementos já ordenados. Sua notação O() é O(n^2), o que significa que sua complexidade de tempo é proporcional a n ao quadrado, onde n é o número de elementos a serem ordenados. Isso o torna menos eficiente do que algoritmos como o Marge-sort para grandes conjuntos de dados, mas pode ser mais eficiente para conjuntos de dados pequenos.
