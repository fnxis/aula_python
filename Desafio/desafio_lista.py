contatos=[]
pessoa1={"nome": "alice", "telefone":"123-456-789"}
pessoa2={"nome": "carlos", "telefone":"987-654-321"}

def adicionarctt(contatos):
    contatos.append(pessoa1)
    contatos.append(pessoa2)
    return contatos
def verificar(verificado):
    verificar_quantidade=len(verificado)
    return verificar_quantidade
def main():
    print(f"os contatos existentes sao {contatos}")
    print(f"os contatos novos sao {adicionarctt(contatos)}")
    print(f"a quantidade de contatos sao {verificar(contatos)}")
main()