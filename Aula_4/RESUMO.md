# Resumo do Código Python - Tabela de Dispersão (Hash Table)

Este código implementa uma tabela de dispersão (hash table) em Python, utilizando sondagem linear para resolver colisões. Aqui está um resumo das principais funcionalidades e conceitos abordados no código:

## Classes

### `HashItem`
- Classe que define um item na tabela de dispersão.
- Cada `HashItem` possui uma chave e um valor associado.

### `HashTable`
- Classe que define a estrutura da tabela de dispersão.
- Inclui métodos para inserir, buscar e redimensionar a tabela.

## Métodos

- `__init__(self, size)`: Inicializa a tabela de dispersão com um tamanho específico.
- `_hash(self, key)`: Método privado que calcula o hash de uma chave.
- `put(self, key, value)`: Insere um par chave-valor na tabela.
- `check_growth(self)`: Verifica se a tabela está muito cheia e precisa ser redimensionada.
- `growth(self)`: Redimensiona a tabela para evitar colisões excessivas.
- `get(self, key)`: Obtém o valor associado a uma chave na tabela.

## Funcionamento

- A inserção de elementos na tabela é feita através do método `put`, que utiliza a técnica de sondagem linear para lidar com colisões.
- A tabela verifica periodicamente sua carga (quantidade de elementos versus tamanho) e a redimensiona se necessário, utilizando o método `growth`.
- Para recuperar valores da tabela, utiliza-se o método `get` informando a chave correspondente.
- Quando a tabela atinge uma carga de 75% ou mais, é redimensionada para o dobro do tamanho atual.

## Exemplo de Uso

- O código inclui um exemplo de criação de uma tabela de dispersão com 10 slots.
- São inseridos vários pares chave-valor na tabela, demonstrando o funcionamento da inserção e resolução de colisões.
- Após a inserção, são feitas algumas buscas na tabela para recuperar valores associados a chaves específicas.
- Por fim, a tabela é redimensionada e seu conteúdo é impresso para demonstrar o resultado da operação.
