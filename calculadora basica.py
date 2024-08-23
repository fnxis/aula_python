var1= input("digite sua funçao:")
var2= int(input("digite seu numero:"))
var3= int(input("digite seu numero:"))
var4= int(input("digite seu numero:"))


if var1 == "soma":
    def somar(x,y):
        return x+y
    print(f"a soma é: {somar (var2,var3)}")

if var1 == "subi" :
    def sub(x,y):
        return x-y
    print(f"a subtraçao é: {sub(var2,var3)}")
    
if var1 == "mult" :
    def multi(x,y):
        return x*y
    print (f"a multiplicaçao é: {multi(var2,var3)}")

if var1 =="quadratica":
    def quadrado(x,y,z):
        return y*y -4*x*z
    print (f"a funçao quadratica é: {quadrado(var2,var3,var4)}")

if var1 == "div" :
    def divi(x,y):
        return x/y
    print(f"a divisao é: {divi(var2,var3)}")