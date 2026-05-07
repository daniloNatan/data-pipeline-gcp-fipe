# GCP FIPE Data Pipeline

Este repositório contém a infraestrutura e os scripts para uma jornada de Engenharia de Dados que extrai dados da API FIPE (veículos).

## Estrutura do Projeto

Seguimos as práticas de DevOps e SRE voltadas à Engenharia de Dados:
- `dags/`: Orquestração de pipelines (Airflow).
- `scripts/`: Scripts principais de extração, processamento e carga de dados no BigQuery (`extract_fipe`, `data_transform`, `load_bigquery`).
- `tests/`: Testes de software garantindo qualidade da arquitetura.
- `config/`: Arquivos complementares de configuração.
- `terraform/`: Arquivos IaC (Infrastructure as Code) para Google Cloud Platform.

## Variáveis de Ambiente e Airflow Variables

Não há hardcoding no projeto. Duplique o arquivo `.env.example` e o renomeie para `.env` se for rodar os scripts localmente sem Airflow.

**Para a execução das DAGs do Airflow:**
A arquitetura foi otimizada para evitar leitura de disco e sobrecarga do Scheduler. Você **deve** cadastrar as seguintes chaves na interface web do Airflow em **Admin > Variables**:
- `FIPE_API_URL`
- `GCP_PROJECT_ID`
- `GCP_TABLE_ID`

## Arquitetura de Pipeline Sênior
Para evitar o estrangulamento do banco de dados de metadados do Airflow (limites do XCom), o tráfego de dados volumosos entre as `tasks` não é feito em memória. 
Utilizamos a gravação de arquivos intermediários eficientes (`.parquet`) na pasta `/tmp/`, e trafegamos apenas a *string* do caminho do arquivo via XCom entre a Extração, Transformação e Carga.

## Dicionário de Dados

**Tabela: Marcas (Veículos FIPE)**

| Coluna | Tipo | Descrição |
|--------|------|-----------|
| `codigo_marca` | INT / STRING | Identificador único da marca na FIPE |
| `nome_marca` | STRING | Nome oficial da marca fabricante |

*(A estrutura final será consolidadada após a carga no Data Warehouse do Google BigQuery).*

## Execução Local (Poetry/UV)

Este projeto usa **Poetry** (ou UV) para gerenciamento de dependências.
Para inicializar o ambiente:
```bash
poetry install
poetry run python scripts/extract_fipe.py
```
