sexo = str(input('qual seu sexo? [m/f]'))
altura = float(input("qual sua altura"))
if sexo == "m": 
    peso_ideal = (72.7 * altura) - 58
elif sexo == "f":
    peso_ideal = (62.1 * altura)- 44.7    
print ("seu peso ideal e:", peso_ideal)