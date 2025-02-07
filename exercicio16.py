quantos_pintar = float(input(" quantos metros vao ser pintados?"))
tinta_usada = quantos_pintar / 3
if tinta_usada == 0:
    print (" nao precisa de lata de tinta")
elif  tinta_usada > 0 and tinta_usada <= 18:
    print (" voce precisa comprar 1 lata")
    print (" preço a pagar: 80 R$")
else:
    varias = tinta_usada // 18
    print (" voce precisa comprar", varias, "latas")
    pagar = varias * 80
    print ("voce precisa pagar", pagar, "R$")
