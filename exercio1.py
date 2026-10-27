nome_cliente = input("Digite o nome do cliente: ")
valor_compra = float(input("Digite o valor total da compra (R$): "))

if valor_compra > 100.0:
	desconto = valor_compra * 0.10
	valor_final = valor_compra - desconto
	ganhou_desconto = True
else:
	desconto = 0.0
	valor_final = valor_compra
	ganhou_desconto = False

print("\n--- RESUMO DO PEDIDO ---")
print(f"Cliente: {nome_cliente}")
print(f"Valor original: R$ {valor_compra:.2f}")

if ganhou_desconto:
	print(f"Parabéns! Você ganhou R$ {desconto:.2f} de desconto (10%).")
else:
	print("Compras até R$ 100.00 não possuem desconto desta vez.")

print(f"Valor total a pagar: R$ {valor_final:.2f}")
print("------------------------")
