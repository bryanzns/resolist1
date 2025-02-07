import math
quantos_pintar = int(input("quantos metros vao ser pintados?"))
litros = quantos_pintar / 6
litros *= 1.1
print ("---------------------------------")
print (" GALAO DE 18 LITROS: 80R$")
print ("LATA DE 3,6 LITROS: 25R$")
print ("---------------------------------")
total_galoes = litros // 18
pggaloes = total_galoes * 80
print ("voce precisa comprar", total_galoes, "de 18 litros")
print (" voce tem que pagar:", pggaloes, "R$")  
total_latas = litros // 3.6
pglata = total_latas * 25
print ("voce precisa comprar ", total_latas, "de 3,6 litros")
print (" voce tem que pagar:",pglata, "R$") 
galoes_mistas = litros // 18 
resto = litros % 18
latas_mistas = math.ceil(resto / 3.6)
preço_misto = (latas_mistas * 25) + (galoes_mistas * 80)
print ("voce precisa comprar :", galoes_mistas, "galoes e ", latas_mistas, "latas")
print ("voce precisa pagar:", preço_misto)

