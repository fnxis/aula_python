frutas=["maça", "banana", "laranja"]
print("as frutas que temos sao:", frutas) 

novafruta=input("qual fruta colocar?")
adicionar=frutas.append(novafruta)
print(frutas)

dele=input("qual fruta tirar?")



if dele in frutas:
    frutas.remove(dele)
    print(frutas)
else:
    print("fruta nao encontrada!")