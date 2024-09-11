nome=input("digite seu Nome: ")
sobrenome=nome.split()

ultimonome=(len(sobrenome))

if ultimonome> 1:
    print(sobrenome[-1])
else:
    print("digite seu sobrenome!")