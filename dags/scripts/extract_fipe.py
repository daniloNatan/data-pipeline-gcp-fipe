import requests
import pandas as pd
from airflow.models import Variable

def extrair_dados() -> str:
    """Extrai dados em formato JSON da API FIPE e os salva em um arquivo parquet temporário.

    Returns:
        str: O caminho do arquivo salvo no disco local (/tmp/fipe_dados_brutos.parquet).

    Raises:
        requests.exceptions.ConnectionError: Quando o servidor não é encontrado.
        requests.exceptions.Timeout: Se a requisição expirar (timeout de 3.05 de conexão e 15s de leitura).
        requests.exceptions.HTTPError: Se o servidor retornar códigos HTTP de erro.
        requests.exceptions.JSONDecodeError: Se a resposta não puder ser convertida para JSON.
        requests.exceptions.RequestException: Qualquer outro erro inesperado na requisição.
    """
    try:
        url = Variable.get('FIPE_API_URL')

        timeout = 3.05, 15

        response = requests.get(url, timeout=timeout)
        
        response.raise_for_status()

        response_json = response.json()

        if isinstance(response_json, (dict, list)):

            df = pd.DataFrame(response_json)
            
            path_local = '/tmp/fipe_dados_brutos.parquet'
            
            df.to_parquet(path_local)
            
            return path_local

    except requests.exceptions.ConnectionError as err_c:

        print(f'Erro de Conexão: O servidor não foi encontrado. Detalhes: {err_c}')
        raise

    except requests.exceptions.Timeout as err_t:

        print(f'Erro de Timeout: A API demorou demais para responder. Detalhes: {err_t}')
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