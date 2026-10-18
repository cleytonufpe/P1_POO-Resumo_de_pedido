#dados

nome = "Felipe"
produto = "Hambúrguer"
quantidade = 3
preco_unitario = 25.0
cupom = "SIM"

#função lower

patterncupom = cupom.lower()

#função subtotal

def calcular_subtotal(quantidade,preco_unitario):
    subtotal = quantidade * preco_unitario
    return subtotal

#subtotal 

subtotal = calcular_subtotal(quantidade,preco_unitario)

#desconto 

desconto = 0

if patterncupom == "sim":
    desconto = subtotal/10
if patterncupom == "nao":
    desconto = 0

#total

total = subtotal - desconto

#classificação

pedido = subtotal
if pedido <= 30:
    tipo_de_pedido = "Pedido pequeno"
elif pedido <= 100:
    tipo_de_pedido = "Pedido médio" 
else:
    tipo_de_pedido = "Pedido grande"

#saida

print("--- INFORMAÇÕES DO PEDIDO ---","\n Cliente:",nome,"\n Produto:",produto,"\n Quantidade:",quantidade,"\n Preço unitário:", preco_unitario,"\n Subtotal:",subtotal,"\n Desconto:",desconto,"\n Total:",total,"\n Classificação:",tipo_de_pedido)
