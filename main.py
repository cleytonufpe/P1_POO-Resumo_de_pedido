#dados

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 3
preco_unitario = 25.0
cupom = "SIM"

#função lower

patterncupom = cupom.lower()

#subtotal

subtotal = quantidade * preco_unitario

#desconto 

desconto = 0

if patterncupom == "sim":
    desconto = subtotal/10
if patterncupom == "nao":
    desconto = 0
