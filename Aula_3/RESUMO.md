# Tabela Hash

Uma tabela hash, também conhecida como mapa hash, é uma estrutura de dados que implementa um tipo de array associativo, onde os dados são armazenados e acessados através de chaves. É uma técnica eficiente para armazenar e recuperar dados, pois permite acesso rápido e eficiente aos elementos, especialmente quando o tamanho dos dados é grande.

## Funcionamento Básico

O funcionamento básico de uma tabela hash envolve a aplicação de uma função hash que mapeia as chaves para índices do array. Essa função hash geralmente transforma as chaves em números inteiros menores, que são usados como índices no array.

Quando um valor é inserido na tabela hash, a função hash é aplicada à chave correspondente para determinar o índice onde o valor será armazenado. Se dois ou mais valores tiverem a mesma posição de índice após a aplicação da função hash, ocorre uma colisão.

## Tratamento de Colisões

As colisões ocorrem quando dois ou mais valores têm a mesma posição de índice após a aplicação da função hash. Existem várias maneiras de lidar com as colisões:

1. **Linear Probing (Sondagem Linear):** Neste método, se uma posição de índice estiver ocupada, a busca continua para a próxima posição livre no array.

2. **Lista Ligada:** Uma lista ligada é usada para armazenar múltiplos valores que colidem na mesma posição de índice. Cada posição do array contém uma referência para o início de uma lista ligada, onde os valores com a mesma posição de índice são armazenados sequencialmente.

3. **Árvore Binária:** Similar à lista ligada, mas em vez de uma lista, uma árvore binária é usada para armazenar os valores que colidem na mesma posição de índice. Isso pode ajudar a melhorar o desempenho em cenários onde há muitas colisões.


