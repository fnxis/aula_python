#variaveis
idade=int(input("qual a sua idade? "))

#definir a categoria dependendo da idade
def validarIdadeTotal(idade):
    if idade < 13:
        return"Criança"
    elif idade >= 13 and idade < 18:
        return"Adolescente"
    elif idade >=18 and idade <70:
        return"Adulto"  
    elif idade >=70 and idade <100:
        return"Idoso"  
    else:
        return "Fossil"

categoriaIdade = validarIdadeTotal(idade)
print(f"A pessoa é classificada como: {categoriaIdade}")    