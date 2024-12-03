import json
import logging
from urllib.parse import urlparse

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def ler_config_json(caminho_arquivo):
    """
    Lê um arquivo JSON e retorna as credenciais de acesso, incluindo o endpoint.
    """
    logger.info(f"Carregando Variáveis do arquivo {caminho_arquivo}!")
    try:
        with open(caminho_arquivo, 'r') as file:
            data = json.load(file)

        access_key = data.get('accessKey')
        secret_key = data.get('secretKey')
        url = data.get('url')

        # Usando urlparse para extrair a parte base da URL (domínio + porta)
        parsed_url = urlparse(url)
        host = f"{parsed_url.hostname}"

        return access_key, secret_key, host
    except Exception as e:
        logger.error(f"Erro ao ler o arquivo de configuração: {e}")
        return None, None, None
