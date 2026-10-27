# Exercício 2: Sistema de Notas UniFECAF

# 1. Entrada de Dados
nome_aluno = input("Digite o nome do estudante: ")
nota1 = float(input("Digite a nota do 1º Bimestre (0 a 10): "))
nota2 = float(input("Digite a nota do 2º Bimestre (0 a 10): "))

# 2. Processamento (Cálculo da Média)
media = (nota1 + nota2) / 2

# 3. Condicionais compostas (if, elif, else)
if media >= 7.0:
    situacao = "APROVADO"
elif media >= 5.0:
    situacao = "EM EXAME"
else:
    situacao = "REPROVADO"

# 4. Saída de Dados
print("\n=== BOLETIM ACADÊMICO ===")
print(f"Estudante: {nome_aluno}")
print(f"Média Final: {media:.1f}")
print(f"Status: {situacao}")
print("=========================")
