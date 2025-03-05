bandeiras={54:"mastercard",53:"Visa",33:"Elo",}
digito=None

while True:
    try:
        digito=int(input("digite o numero da bandeira do cartao(digite-1 para sair)"))
        if digito == -1:
            print("encerando processo.")
            break
        if digito in bandeiras:
            print(f"a bandeira correspondente é: {bandeiras[digito]}")
            break
        else:
            print("digite um numero valido")
    except ValueError:
        print("nao foi digitado um numero inteiro")
    except Exception:
        print("erro ::", Exception)