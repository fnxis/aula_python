alunos={"ryan":2,"galvao":8,"rafael":7,"guilherme":10}

def recuperarNota(aluno):
    if aluno in alunos:
        print(f"a nota de {aluno} é {alunos[aluno]}") 
    else:
        print("este aluno nao esta com nota")
        main()

        operacao=input("deseja tentar novamente?(s/n)")
        if operacao.upper() == "s":
            main()
        elif operacao.upper() == "n":
            print("programa finalizado")
        else:
            print("digite corretamente")
def main():
    aluno=input("digite seu nome")
    recuperarNota(aluno)
main()