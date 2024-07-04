valor = float(input("Informe o valor do Produto: "))
mPagamento = input("Informe o metodo de pagamento, debito, credito, pix , dinheiro: ")
total = 0
if mPagamento == 'pix' or mPagamento == 'dinheiro' :
    desconto = valor * 0.20
    total = valor - desconto
    print("Total compra : ",total,"Total de Desconto: ",desconto)
    print(" Volte sempre.")
elif mPagamento == 'debito':
    desconto = valor * 0.10 
    total = valor - desconto
    print("Total compra : ",total,"Total de Desconto: ",desconto)
    print(" Volte sempre.")
elif mPagamento == 'credito':
    credito = valor + (valor * 2.5)
    total = credito
    print("Modalidade credito existe um taixa de 2.5") 
    print("Total compra : ",total," Volte sempre.")
else:
     print("Modalidade de Pagamento incorreto.")     
