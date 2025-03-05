import time
import webbrowser
url="https://www.youtube.com/watch?v=Vxiw56uvaWc&pp=ygUTaXBob25lIGRlIGJyaW5xdWVkbw%3D%3D"
contadorsleep=1
contador=5
while contador>0:
    print(contador)
    time.sleep(contadorsleep)
    contador-=1
    contadorsleep+=1
print( "parabens!Voce ganhou um iphone.Clique no link e resgate agora!")
webbrowser.open(url)



senhaboa="4759"
senha=""
while senha !=senhaboa:
    senha=input("digite sua senha")
print("acesso concedido")