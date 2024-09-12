alunos={"ryan":2,"galvao":8,"rafael":7,"guilherme":10}
verificaraluno=input("qual aluno voçe quer? ")
if verificaraluno in alunos:
    if verificaraluno =="rafael":
        print(f"a sua nota é {alunos['rafael']}")
    if verificaraluno =="ryan":
        print(f"a sua nota é {alunos['ryan']}")
    if verificaraluno =="guilherme":
        print(f"a sua nota é {alunos['guilherme']}")
    if verificaraluno =="galvao":
        print(f"a sua nota é {alunos['galvao']}")        
else:
    print("este aluno nao esta com nota")