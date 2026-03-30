escola = {}

while True:
    print("\n--- Cadastro de Aluno ---")
    nome = input("Digite o nome do aluno (ou 'sair' para encerrar): ")
    
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
    else:
        situacao = "Reprovado"

    Dados_alunos = {
        "Nome": nome,
        "Media": Media,
        "Situacao": situacao
    }
    
    if turma not in escola:
        escola[turma] = []
    
    # Esta linha deve ficar fora do 'if turma not in' para adicionar o aluno sempre
    escola[turma].append(Dados_alunos)

# O RELATÓRIO FICA FORA DO WHILE (DEPOIS QUE O USUÁRIO DIGITA 'SAIR')
print("\n" + "="*30)
print("RELATÓRIO FINAL POR TURMA")
print("="*30)

for nome_turma, alunos in escola.items():
    print(f"\nTurma: {nome_turma}")
    for aluno in alunos:
        print(f"Nome: {aluno['Nome']}, Média: {aluno['Media']:.2f}, Situação: {aluno['Situacao']}")