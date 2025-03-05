#abrir uma escrita
with open("top1.txt","r",encoding="utf-8")as arquivo:
    conteudo=arquivo.read()
    print(conteudo)
#escrever e formatar
with open("top1.txt","w",encoding="utf-8")as arquivo1:
    arquivo1.write("ola amigos!\n")
    arquivo1.write("ola amigos!")
#acrescentar
with open("top1.txt","a",encoding="utf-8")as arquivo2:
    arquivo2.write("\ntexto")