# Reto: Guardian del cine

edad = 18
tiene_boleto = True
amigo_del_gerente = False

if edad >= 18 and tiene_boleto:
    print('Puede entrar al cine, eres mayor de edad y tienes boleto')
elif not tiene_boleto and amigo_del_gerente:
    print('Puedes entrar al cine por que eres amigo del gerente')
else:
    print('No puedes entrar al cine')