frutas=["abacate", "pera", "maça"]
print("as frutas que temos sao:", frutas)

#adiciona na lista
frutas.append('uva')
print("lista de frutas att:",frutas)

#remove na lista
frutas.remove('maça')
print("lista de frutas att:",frutas)

#remove na lista com o indice
frutas.remove(frutas[1])
print("lista de frutas att:",frutas)

#chama a fruta que foi colocada no indice
print("primeira fruta:",frutas[0])