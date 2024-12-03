from config_loader import ler_config_json
from bucket_operations import MinIOClient


def main():
    # Caminho para o arquivo JSON
    caminho_arquivo = './credentials.json'
    # Lendo as credenciais do arquivo JSON
    access_key, secret_key, host = ler_config_json(caminho_arquivo)
    # TODO: informar a porta do serviço do Minio IO. Exemplo: '9000'
    port = '9000'
    # TODO: Utilizar minio_endpoint=localhost:9000 se se o script for executado no mesmo ambiente que o minio
    minio_endpoint = f'{host}:{port}'
    # TODO: informar o nome do bucket onde está os arquivos. Exemplo: 'prd-data-raw'
    bucket_name = 'prd-data-raw'

    # Criando instâncias das classes
    minio_client = MinIOClient(minio_endpoint, access_key, secret_key, bucket_name)

    # Nome do arquivo a ser salvo
    arquivo_nome = "2024-12-03-74cc729f-b49f-44de-bf5e-b2d24eb26035.json"

    # Baixando o arquivo do MinIO
    minio_client.download_object(arquivo_nome)

if __name__ == "__main__":
    main()