import pandas as pd

# Carregar as planilhas
planilha1 = pd.read_excel('SP.xlsx')
planilha2 = pd.read_excel('ABC.xlsx')
planilha3 = pd.read_excel('CAMPINAS.xlsx')
planilha4 = pd.read_excel('SOROPIRA.xlsx')
planilha5 = pd.read_excel('SAOJOSES.xlsx')
planilha6 = pd.read_excel('MAUADIADCARAJUNDITAINDA.xlsx')

# Lista de planilhas
planilhas = [planilha1, planilha2, planilha3, planilha4, planilha5, planilha6]

# Realizar a concatenação com base nas colunas comuns
resultado = pd.concat(planilhas, ignore_index=True, join='inner')  # Mantém apenas as colunas comuns entre todas

# Salvar o resultado em uma nova planilha
resultado.to_excel('todas.xlsx', index=False)

print("Planilhas unidas com sucesso!")
