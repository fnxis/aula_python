listaPessoas=[]

#adiçao de pessoas na lista
pessoa={"nome":"ana","idade":24}
listaPessoas.append(pessoa)
print(listaPessoas)

#adiçao de pessoas na lista
pessoa={"nome":"marcia","idade":34}
listaPessoas.append(pessoa)
print(listaPessoas)

#adiçao de pessoas na lista
pessoa={"nome":"clara","idade":54}
listaPessoas.append(pessoa)
print(listaPessoas)

#chamada de tal pessoa 
marcia=listaPessoas[1]
print(marcia)

#funçao set remove as coisas repetidas
lista={1,2,2,3,3,4}
tirar=set(lista)
print(tirar)

#comando de conjunto
a={1,2,3}
b={3,4,5}
print(a & b) #interseçao
print(a | b) #uniao
print(a - b) #diferença
print(3 in a)#saida true
print(4 in a)#saida false
