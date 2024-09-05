#variaveis de preço
preços=[100,200,2]
#soma dos preços
total=sum(preços)
print("Total antes do desconto:", total,"Reais")
#formula do desconto
if total>500:
    desc=total*0.1
    valor_final=total-desc
    print("Total com desconto é de:", valor_final,"Reais")
    print("desconto é de:", desc,"Reais")
else:
    valor_final=total
    diferença= 500 - valor_final
    print("faltou",diferença,"para o desconto ser aplicado")