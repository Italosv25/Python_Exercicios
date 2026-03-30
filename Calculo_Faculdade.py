escola = {}
while True:
    print("\n--- Cadastro de Aluno ---")
    nome = input ("Digite o nome do aluno (ou 'sair' para encerrar): ")
    if nome.lower() == 'sair':
        break
turma = input("Digite a turma do aluno: ")

B1 = float(input("Digite a nota da B1: "))
B2 = float(input("Digite a nota da B2: "))
Media = (B1 + B2) / 2
if Media >= 6:
    situacao = "Aprovado"
elif Media >= 4:
    situacao = "Recuperação"
else:    situacao = "Reprovado"

Dados_alunos = {
    "Nome": nome,
    "Media": Media,
    "Situacao": situacao
}
if turma not in escola:
    escola[turma] = []
    escola[turma].append(Dados_alunos)


