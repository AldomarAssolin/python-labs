# Fila de Atendimento

Uma **fila de atendimento** segue o princípio **FIFO (First In, First Out)**:
o primeiro cliente que entra é o primeiro a ser atendido.

## Operações

- `enqueue(cliente)`: adiciona o cliente ao final da fila.
- `dequeue()`: remove e retorna o cliente do início da fila.
- `front()`: consulta quem é o próximo a ser atendido, sem remover.
- `is_empty()`: verifica se a fila está vazia.

## Exemplo de fluxo

1. Cliente A entra na fila.
2. Cliente B entra na fila.
3. Cliente C entra na fila.
4. Atende A → fila fica com B, C.
5. Atende B → fila fica com C.
6. Atende C → fila fica vazia.
