import pandas as pd
import os

def data_transform(caminho_bruto: str) -> str:
    """Recebe o caminho do arquivo parquet bruto, realiza a transformação no Pandas, renomeia colunas, remove duplicatas e salva em um novo arquivo parquet limpo.

    Args:
        caminho_bruto (str): Caminho local do arquivo parquet proveniente da extração via XCom.

    Returns:
        str: Caminho local do arquivo parquet transformado.
    """
    if not caminho_bruto or not os.path.exists(caminho_bruto):
        raise ValueError('Caminho do arquivo bruto inválido ou inexistente. Processo abortado.')

    df = pd.read_parquet(caminho_bruto)
    print(f'Processo de transformação iniciado, {len(df)} registros sendo processados.')

    df = df.rename(columns={'codigo' : 'codigo_marca', 'nome' : 'nome_marca'})

    df_transformado = df.drop_duplicates()

    path_local_limpo = '/tmp/fipe_dados_limpos.parquet'
    
    df_transformado.to_parquet(path_local_limpo)

    return path_local_limpo
