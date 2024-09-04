#variaveis de preço
preços=[100,200,300]
desc=0

#soma dos preços
total=sum(preços)

#formula do desconto
if total>500:
    desc=total*0.1

#calculo dos descontos
valor_final=total-desc

#respostas do codigo
print("Total antes do desconto:", total,"Reais")
print("Desconto aplicado é de:", desc,"Reais")
print("Total com desconto é de:", valor_final,"Reais")
