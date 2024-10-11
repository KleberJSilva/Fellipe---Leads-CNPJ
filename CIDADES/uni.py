import requests as res
import pandas as pd

# Lendo os CNPJs de uma planilha
cnpj_df = pd.read_excel('TODOS.xlsx')  # Supondo que a coluna com CNPJs se chame 'CNPJ'
cnpjs = cnpj_df['CNPJ'].astype(str).tolist()  # Convertendo a coluna de CNPJs para uma lista de strings

# Adicionando zero à frente de CNPJs com menos de 14 caracteres
cnpjs = [cnpj.zfill(14) for cnpj in cnpjs]

# Inicializando uma lista para armazenar os resultados
resultados = []

# Loop para buscar informações de cada CNPJ
for cnpj in cnpjs:
    url = f'http://ws.hubdodesenvolvedor.com.br/v2/cnpj/?cnpj={cnpj}&token=token'
    response = res.get(url)
    
    if response.status_code == 200:  # Verificando se a requisição foi bem-sucedida
        data = response.json()

        # Verificando se a chave 'result' está presente na resposta
        if 'result' in data:
            # Extraindo os dados necessários
            nome = data['result'].get('nome', 'Não informado')
            fantasia = data['result'].get('fantasia', 'Não informado')
            telefone = data['result'].get('telefone', 'Não informado')
            email = data['result'].get('email', 'Não informado')
            quadro_socios = data['result'].get('quadro_de_socios', [])

            # Armazenando os dados em um dicionário
            if isinstance(quadro_socios, list):  # Verificando se quadro_socios é uma lista
                for socio in quadro_socios:
                    socio_nome = socio.get('nome', 'Não informado') if isinstance(socio, dict) else socio
                    resultados.append({
                        'CNPJ': cnpj,
                        'Nome': nome,
                        'Fantasia': fantasia,
                        'Telefone': telefone,
                        'Email': email,
                        'Sócio': socio_nome
                    })
            else:
                # Se quadro_socios não for uma lista, armazenamos apenas um registro
                resultados.append({
                    'CNPJ': cnpj,
                    'Nome': nome,
                    'Fantasia': fantasia,
                    'Telefone': telefone,
                    'Email': email,
                    'Sócio': 'Não informado'
                })
        else:
            # Se 'result' não estiver na resposta, armazenamos um aviso
            resultados.append({
                'CNPJ': cnpj,
                'Nome': 'Não encontrado',
                'Fantasia': 'Não encontrado',
                'Telefone': 'Não encontrado',
                'Email': 'Não encontrado',
                'Sócio': 'Não encontrado'
            })
    else:
        print(f"Erro ao buscar CNPJ {cnpj}: {response.status_code}")

# Convertendo os resultados em um DataFrame
resultados_df = pd.DataFrame(resultados)

# Salvando os resultados em uma planilha Excel
resultados_df.to_excel('resultado.xlsx', index=False)

print("Dados salvos na planilha 'resultado.xlsx'.")
