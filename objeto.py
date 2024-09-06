pessoa={"nome":"ana" ,"idade":30}
print("pessoa:",pessoa)
#ira printar somente o nome
print("nome:",pessoa["nome"])
#adiçao de outro elemento na lista
pessoa["cidade"]="Sao Paulo"
print("pessoa atualizada:",pessoa)
#classe inteira
pessoa2={"nome":"brenda","idade1":26,"filhos":{"nome":"caitlyn","idade2":4}}
#chamada de atributos da lista
print(pessoa2)
print(pessoa2["nome"])
print(pessoa2["filhos"])
print(pessoa2["filhos"]["nome"])
print(pessoa2["idade1"])
#deleta algum atributo desta lista
del pessoa2["nome"]
print (pessoa2)