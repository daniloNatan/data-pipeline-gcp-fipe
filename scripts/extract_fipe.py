from typing import Dict, List
import requests
import os
from dotenv import load_dotenv

load_dotenv()

url = os.getenv('FIPE_API_URL')

def extrair_dados(url: str) -> List[Dict]:
    """Realiza uma requisição HTTP GET para a URL da API da FIPE e extrai os dados em formato JSON.

    Args:
        url (str): A URL da API ou endpoint para realizar a requisição.

    Returns:
        List[Dict]: Uma lista de dicionários contendo os dados retornados pela API.
    """
    try:

        timeout = 3.05, 15

        response = requests.get(url, timeout=timeout)
        
        response.raise_for_status()

        response_json = response.json()

        if isinstance(response_json, (dict, list)):

            return response_json

    except requests.exceptions.ConnectionError as err_c:

        print(f'Erro de Conexão: O servidor não foi encontrado. Detalhes: {err_c}')
        raise

    except requests.exceptions.Timeout as err_t:

        print(f'rro de Timeout: A API demorou demais para responder. Detalhes: {err_t}')
        raise

    except requests.exceptions.HTTPError as err_h:

        print(f'Erro HTTP: O servidor retornou um código de erro. Detalhes: {err_h}.')
        raise 

    except requests.exceptions.JSONDecodeError as err_j:

        print(f'Erro de JSON: A resposta recebida não é um JSON válido. Detalhes: {err_j}')
        raise

    except requests.exceptions.RequestException as erro_g:

        print(f'Erro Genérico: Um erro inesperado ocorreu durante a requisição. Detalhes: {erro_g}')
        raise