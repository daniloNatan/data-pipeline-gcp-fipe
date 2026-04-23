from typing import List, Dict
import pandas as pd

def data_transform(dados_brutos_json : List[Dict]) -> pd.DataFrame:

    """Recebe os dados que devem ser no formato de List[Dict] (json), valida se está vazio e informa o erro, realiza a transformação de json para DataFrame, renomeia as colunas 'codigo', 'nome' para 'codigo_marca', 'nome_marca', remove as linhas duplicadas e retorna o dataframe transformado.

    Returns:
        pd.DataFrame: DataFrame com as colunas 'codigo_marca' e 'nome_marca', sem linhas duplicadas.
    """
    if not dados_brutos_json:
        raise ValueError('Lista de dados vazia, processo de transformação interrompido.')

    print(f'Processo de transformação iniciado, {len(dados_brutos_json)} registros sendo processados.')

    df = pd.DataFrame(dados_brutos_json)

    df = df.rename(columns={'codigo' : 'codigo_marca', 'nome' : 'nome_marca'})

    df_transformado = df.drop_duplicates()

    return df_transformado
