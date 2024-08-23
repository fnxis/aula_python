var1= input("?")
var2= 27
var3= 41



if var1 == "soma":
    def somar(x,y):
        return x+y
    print(f"a soma é: {somar(var2,var3)}")
    
if var1 == "subi" :
    def sub(x,y):
        return x-y
    print(f"a subtraçao é: {sub(var2,var3)}")
    
if var1 == "mult" :
    def multi(x,y):
        return x*y
    print(f"a multiplicaçao é: {multi(var2,var3)}")

if var1 == "div" :
    def divi(x,y):
        return x/y
    print(f"a divisao é: {divi(var2,var3)}")