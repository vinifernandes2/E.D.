from lista_encadeada import ListaEncadeada

lista = ListaEncadeada()

print("Lista está vazia?", lista.esta_vazia())
lista.inserir(1, 10)
lista.inserir(2, 20)
lista.inserir(3, 30)
lista.inserir(2, 15)
lista.imprimir()  # Esperado: 10 -> 15 -> 20 -> 30

print("Tamanho da lista:", lista.obter_tamanho())
print("Elemento na posição 2:", lista.obter_valor(2))

lista.modificar_valor(2, 17)
print("Após modificar posição 2 para 17:")
lista.imprimir()  # Esperado: 10 -> 17 -> 20 -> 30

print("Removendo da posição 3:", lista.retirar(3))
lista.imprimir()  # Esperado: 10 -> 17 -> 30

print("Lista está vazia?", lista.esta_vazia())
print("Tamanho final da lista:", lista.obter_tamanho())