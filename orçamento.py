
servico = []
qnt_Servico = []
preco_Servico = []
subtotal = 0
total = []
pagamento = 0

nome = input("Qual o nome do cliente: ")
enderenco = input("Qual o enderenço do cliente: ")
fone = input("Qual o telefone do cliente: ")
email = input("Qual o e-mail do cliente ")
resposta = "S"
while resposta == "S":
    servico.append(input("Qual foi o serviço: "))
    qnt_Servico.append(int(input("Quantas quantidades: ")))
    preco_Servico.append(float(input("Qual o valor unitario do serviço: ")))

    resposta = input("Digite \"S\" para cadastrar outro serviço:").upper()


arquivo = open("Orçamento02.xtx", "w")

pagamento = input("Qual a forma de pagamento :")
print("RUA ILHEUS, 890-BLOCO 5 APT 204- PIEDADE - JABOATÃO DOS GUARARAPES - CEP:54420-150 ")
arquivo.write("AVENIDA JESE BUHA TEM, 113-A- VILA NAZARE- PAÇO DO LUMIAR - MAR - CEP:65.130-00 \n")
print('-'*90)
print('{:^90}'.format('Dados do Cliente'))
arquivo.write('{:^90}'.format('Dados do Cliente'))
print('-'*90)
print("NOME: "+ nome)
arquivo.write("\nNOME: "+ nome)
print("END: "+enderenco)
arquivo.write("\nEND: "+enderenco)
print("FONE: "+ fone + "    E-MAIL: " + email)
arquivo.write("\nFONE: "+ fone + "    \nE-MAIL: " + email + "\n")


print('-'*90)
print('{:^90}'.format('Dados dos serviços'))
arquivo.write('{:^90}'.format('Dados dos serviços'))
print('-'*90)


print("COG   QNT             SERVIÇOS                  VALOR UNI           SUBTOTAL" )
arquivo.write("\nCOG   QNT             SERVIÇOS                  VALOR UNI           SUBTOTAL\n" )
for s in range(0,len(servico)):
    subtotal = (qnt_Servico[s] * preco_Servico[s])
    total.append(subtotal)
    print(s+1,"   ", qnt_Servico[s], "              ", servico[s], "                    ", preco_Servico[s], "              ",
          subtotal)
    #arquivo.write['{},"   ", {}, "              ", {}, "                    ", {}, "              ",{}'.format(str(s+1), str(qnt_Servico[s]), str(preco_Servico[s]), str(subtotal))]
print('-'*90)
print("TOTAL: R$ ", sum(total))
#arquivo.write("TOTAL: R$ ", sum(total))
print('-'*90)
print("FORMA de PAGAMENTO:", pagamento)
#arquivo.write("\nFORMA de PAGAMENTO:", pagamento)
arquivo.close()