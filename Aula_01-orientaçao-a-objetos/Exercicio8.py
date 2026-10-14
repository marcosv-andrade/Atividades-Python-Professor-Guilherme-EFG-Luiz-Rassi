temperatura = float(input("Qual temperatura: "))

if temperatura >= 30: # lembrar sempre de colocar " : " #
    print(f"Temperatura de risco(alerta vermelho)")
elif temperatura >=15 and temperatura < 30:
    print(f"Temperatura média(alerta amarelo)")
else: # lembrar sempre de colocar " : " depois do else #
    print(f"Temperatura ideal(alerta verde)")


"""Exercicio 8) Voce esta desenvolvendo um pequeno programaque atraves de um sensor de temperatura mede a temperatura de um freezer de vacina, usando um input receba essa temperatura e classifique mandando um alerta na tela
leia a temperatura e informe se: Temperatura de risco(alerta veremelho)(acima de 30)
                                 Temperatura  média(alerta amarelo)(entre 15 e 30)
                                 Temperatura ideal(alerta verde(menor que 15)"""