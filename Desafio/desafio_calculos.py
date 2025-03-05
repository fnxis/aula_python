def calcular(operacao,a,b):
    if(operacao == "+"):
        soma=a+b
        return soma
    elif(operacao == "-"):
        menos=a-b
        return menos
    elif(operacao == "/"):
        divi=a/b
        return divi
    elif(operacao =="*"):
        vezes=a*b
        return vezes
def main():
    listaop=["+","-","*","/"]
    numero1=float(input("digite seu primeiro numero: "))
    numero2=float(input("digite seu segundo numero: "))
    tipo_op=input("qual operaçao voce quer?")

    if tipo_op not in listaop:
        print("operaçao nao encntrada.Deseja tentar novamente?")
    else:
        resultado=calcular(tipo_op,numero1,numero2)
        if isinstance(resultado,str):
            print(resultado)
        else:
            print(f"resultado {numero1} {tipo_op} {numero2} = {resultado}")
main()