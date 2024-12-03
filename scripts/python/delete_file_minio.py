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

    # TODO: informar o Nome do arquivo a ser excluido
    file_name = '2024-12-03-377e96da-67b8-469b-acaa-056595ee6b29.json'

    # Criando instâncias das classes
    minio_client = MinIOClient(minio_endpoint, access_key, secret_key, bucket_name)

    # Excluindo o arquivo do MinIO
    minio_client.delete_object(file_name)

if __name__ == '__main__':
    main()