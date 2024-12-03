from config_loader import ler_config_json
from bucket_operations import MinIOClient
from datetime import date
import uuid
from faker import Faker
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PessoaFicticia:
    def __init__(self):
        self.fake = Faker('pt_BR')

    def gerar_cadastro(self):
        return {
            "nome": self.fake.name(),
            "email": self.fake.email(),
            "endereco": self.fake.address(),
            "telefone": self.fake.phone_number(),
            "cpf": self.fake.cpf(),
            "data_nascimento": self.fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=80).isoformat(),
            "data_cadastro": self.fake.date_this_decade().isoformat()
        }

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
    arquivo_nome = f'{date.today()}-{uuid.uuid4()}.json'

    # Dados a serem salvos no MinIO
    cadastro_ficticio = PessoaFicticia().gerar_cadastro()

    logger.info(f"Cadastro ficticio gerado: {cadastro_ficticio}")

    # Salvando o cadastro no MinIO
    minio_client.save_object(arquivo_nome, cadastro_ficticio)

if __name__ == "__main__":
    main()   