quantos_kg = float(input("quantos kg de peixe voce pegou?"))
if quantos_kg > 50:
  excesso =   quantos_kg - 50
  multa = excesso * 4
  print ("voce tem que pagar de multa por ultrapassagem de peso:", multa)
else:
  print (" voce esta dentro da lei :)") 

 