#variaveis
idade=int(input("qual a sua idade? "))

#definir a categoria dependendo da idade
def validarIdadeTotal(idade):
    mensagemFormal= "A pessoa é classificada como "
    MensagemInformal= "ele é um "
    if idade < 13:
        return mensagemFormal+"Criança"
    elif idade >= 13 and idade < 18:
        return mensagemFormal+"Adolescente"
    elif idade >=18 and idade <70:
        return mensagemFormal+"Adulto"  
    elif idade >=70 and idade <100:
        return mensagemFormal+"Idoso"  
    else:
        return MensagemInformal+"Fossil"

#chamar a funçao novamente
categoriaIdade = validarIdadeTotal(idade)
print(categoriaIdade)