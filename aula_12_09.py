def calcular (numero1,numero2):
    soma=numero1+numero2
    subtracao=numero1-numero2
    return(soma,subtracao)

numero1=float(input("digite seu 1 numero"))
numero2=float(input("digite seu 2 numero"))

valorSoma,valorSubtraçao=calcular(numero1,numero2)
print(f"a soma é{valorSoma}")
print(f"a subtraçao é{valorSubtraçao}")