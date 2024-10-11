import requests
import pandas as pd
from bs4 import BeautifulSoup

# Função para buscar o título e os telefones na página de um CNPJ
def buscar_dados(cnpj):
    # Garantir que o CNPJ tenha 14 dígitos, adicionando zeros à esquerda se necessário
    cnpj = str(cnpj).zfill(14)

    url = f"https://cnpja.com/office/{cnpj}"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Connection": "keep-alive"
    }

    # Faz a requisição HTTP
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Faz o parsing do HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Captura o valor da tag <title>
        title = soup.title.string if soup.title else "Título não encontrado"

        # Busca todos os números de telefone
        telefones = []
        for a_tag in soup.find_all('a', href=True):
            if "tel:" in a_tag['href']:
                telefone = a_tag['href'].replace("tel:", "")
                telefones.append(telefone)

        # Junta os telefones encontrados (caso haja mais de um)
        telefones_str = ", ".join(telefones) if telefones else "Telefone não encontrado"

        # Retorna uma tupla com o título e os telefones
        return title, telefones_str

    # Retorna None se algo der errado
    return "Erro ao acessar", "Telefone não encontrado"

# Carrega a planilha com os CNPJs
planilha = pd.read_excel('SP.xlsx')  # Supondo que a planilha tenha uma coluna chamada "CNPJ"

# Verifica se a coluna "CNPJ" está na planilha
if 'CNPJ' not in planilha.columns:
    print("A planilha deve conter uma coluna chamada 'CNPJ'.")
else:
    # Cria novas colunas "Título" e "Telefone" para salvar os resultados
    planilha[['Título', 'Telefone']] = planilha['CNPJ'].apply(lambda cnpj: pd.Series(buscar_dados(cnpj)))

    # Salva o resultado em uma nova planilha
    planilha.to_excel('cnpjs_com_titulo_telefones.xlsx', index=False)

    print("Título e telefones adicionados, e planilha salva com sucesso!")
