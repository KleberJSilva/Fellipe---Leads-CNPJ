import requests as res
import pandas as pd
import time

# Função para consultar CNPJ e retornar dados
def consulta_cnpj(cnpj):
    url = f'https://open.cnpja.com/office/{cnpj}'
    try:
        response = res.get(url)
        response.raise_for_status()  # Levanta um erro se a requisição falhar
        data = response.json()

        # Extrair as informações
        name = data['company']['name']
        alias = data['alias']
        phones = [f"({phone['area']}) {phone['number']}" for phone in data['phones']]
        emails = [email['address'] for email in data['emails']]
        member_names = [member['person']['name'] for member in data['company']['members']]

        return {
            "Razao Social": name,
            "Fantasia": alias,
            "Telefone": phones,
            "Emails": emails,
            "Socios": member_names
        }
    except res.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao consultar CNPJ {cnpj}: {http_err}")
    except res.exceptions.RequestException as req_err:
        print(f"Erro de requisição ao consultar CNPJ {cnpj}: {req_err}")
    except Exception as e:
        print(f"Erro inesperado ao consultar CNPJ {cnpj}: {e}")
    return None

# Lê a planilha com os CNPJs
cnpj_df = pd.read_excel('todas.xlsx')  # Substitua pelo caminho da sua planilha
cnpj_list = cnpj_df['CNPJ'].tolist()  # Assumindo que a coluna se chama 'CNPJ'

# Lista para armazenar resultados
results = []

# Loop pelos CNPJs
for cnpj in cnpj_list:
    result = consulta_cnpj(cnpj)
    if result:
        results.append(result)
    time.sleep(20)  # Aguardar 20 segundos entre requisições

# Cria um DataFrame com os resultados
results_df = pd.DataFrame(results)

# Salva os resultados em uma nova planilha
results_df.to_excel('resultados_cnpj.xlsx', index=False)
print("Resultados salvos na planilha 'resultados_cnpj.xlsx'")
