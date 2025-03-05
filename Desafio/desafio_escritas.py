def escritas(strings):
    stringmaiuscula=strings.upper()
    strinminuscula=strings.lower()
    stringcaracteres=len(strings)

    return(stringmaiuscula,strinminuscula,stringcaracteres)



def main():
    palavra=input("digite sua string para ser modificada.")

    resulmaiusculo,resulminusculo,caracteres=escritas(palavra)

    print(f"sua palavra em maisuculo é: {resulmaiusculo}")
    print(f"sua palavra em minusculo é: {resulminusculo}")
    print(f"sua palavra em caracteres é: {caracteres}")
main()