arquivo = float(input(" quantos mb tem o arquivo?"))
link = float(input(" qual a velocidade em mbps do link?"))
mb = arquivo * 8 
instalaçao = mb / link
print ("sua instalaçao vai demorar:", instalaçao, "segundos")