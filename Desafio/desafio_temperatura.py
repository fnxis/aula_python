def graus(temperatura):
    return (temperatura-32)/(1.8)

def fahrenheit(temperatura):
    return (temperatura*1.8) + 32

def main():
    qualTemperatura=input("qual o tipo de temperatura? (F/C)")
    temperatura=float(input("qual a temperatura?"))
    if qualTemperatura.upper() =="C":
        print(f"{fahrenheit(temperatura):.2f}°f")
    if qualTemperatura.upper() =="F":
        print(f"{graus(temperatura):.2f}°C")
main()