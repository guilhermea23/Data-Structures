# Grafos
- Grafos dirigidos -> Existe uma única direção, nesse caso as arestas são pares ordenados de vértices, vai apenas da origem para o destino. Se origem e destino forem iguais temos um laço.

- Grafos não dirigidos -> Não tem uma direção, vai tanto da origem ao destino quanto do destino a origem. Pares não ordenados de vértices, não existe laço.

# Grafo adjacente
- Se (u,v) é uma aresta no grafo, então dizemos que ```v``` é adjacente a ```u``` ou que ```v``` é vizinho de ```u```.
- Interpretando o par ordenado ```(u,v)```:
  - a aresta sai de ```u``` e entra em ```v```.
- Em grafos não dirigidos tanto faz a ordem porque são pares não ordenados de vértices, ou seja a relação é simétrica.

```python
(u,v) is (v,u)
```
- Já em grafos dirigidos não existe tal simetria.
```python
(u,v) is not (v,u)
```

# Grau de vértice ```grauVertice```
- Em grafos não dirigidos:
  - é o número de arestas que chegam até ele

- Em grafos dirigidos:
  - ```Grau de Saida (gDeSaida)```: nº de arestas que saem do vértice.
  - ```Grau de entrada (gDeEntrada)```:
  nº de vértices que chegam até ele.
  - Assim temos que:
    ```python
     grauVertice = gDeSaida + gDeEntrada
    ``` 

# Conectividade
- Grafo ND:
  - É conexo ou conectado se cada par de vertices nele tiver conectado por um caminho.

- Grafo Direcionado
  - Grafo fortemente conexo: existe um caminho entre qualquer par de vértices no grafo.
  - Grafo conexo: existe apenas um caminha de ida ou apenas um caminho de volta.
  - Grafo fracamente conexo: se a substituição de todas arestas por arestas não direcionadas produz um grafo conexo.

# Pesos
- Grafos podem ser ponderados.
  - Caso em que possuem pesos associados às suas arestas. Tais pesos podem representar custos,distâncias, etc.


```As árvores são grafos acíclicos (não tem ciclo), conexos e não-dirigido.```


# Matriz de Adjacência
- Uma ```matriz de adjacência``` A de um grafo com ```n vértices``` é uma matriz ```n x n``` de bits, em que:
  - A[i,j] = 1, se houver uma aresta indo do vértice ```i``` ao vértice ```j``` no grafo.
  - A[i,j] = 0, se não houver arestas indo de ```i``` para ```j```.
