# GCP FIPE Data Pipeline

Este repositório contém a infraestrutura e os scripts para uma jornada de Engenharia de Dados que extrai dados da API FIPE (veículos).

## Estrutura do Projeto

Seguimos as práticas de DevOps e SRE voltadas à Engenharia de Dados:
- `dags/`: Orquestração de pipelines (Airflow).
- `scripts/`: Scripts principais de extração, processamento e carga de dados no BigQuery (`extract_fipe`, `data_transform`, `load_bigquery`).
- `tests/`: Testes de software garantindo qualidade da arquitetura.
- `config/`: Arquivos complementares de configuração.
- `terraform/`: Arquivos IaC (Infrastructure as Code) para Google Cloud Platform.

## Variáveis de Ambiente

Não há hardcoding no projeto. Duplique o arquivo `.env.example` e o renomeie para `.env`, preenchendo as chaves necessárias antes de rodar os scripts.

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
