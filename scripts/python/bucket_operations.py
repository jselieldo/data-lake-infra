import boto3
import json
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MinIOClient:
    def __init__(self, endpoint, access_key, secret_key, bucket_name, region='us-east-1', use_ssl=False):
        self.endpoint = endpoint
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.region = region
        self.use_ssl = use_ssl

        self.s3 = boto3.client(
            's3',
            endpoint_url=f'http://{self.endpoint}',
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key,
            region_name=self.region,
            use_ssl=self.use_ssl
        )

    def list_objects(self):
        try:
            logger.info(f"Listando objetos do bucket {self.bucket_name}:")
            response = self.s3.list_objects_v2(Bucket=self.bucket_name)
            if 'Contents' in response:
                for obj in response['Contents']:
                    logger.info(f"Objeto: {obj['Key']}")
            else:
                logger.info("Nenhum objeto encontrado no bucket.")
        except (NoCredentialsError, PartialCredentialsError) as e:
            logger.error(f"Erro de credenciais: {e}")
        except Exception as e:
            logger.error(f"Erro ao listar objetos: {e}")
        finally:
            logger.info("Listagem de objetos concluída.")
            

    def save_object(self, file_name, data):
        try:
            data_json = json.dumps(data, indent=4)
            self.s3.put_object(Bucket=self.bucket_name, Key=file_name, Body=data_json)
            logger.info(f"Cadastro salvo com sucesso em {self.bucket_name}/{file_name}!")
        except Exception as e:
            logger.error(f"Erro ao salvar o arquivo: {e}")

    def download_object(self, file_name):
        try:
            logger.info(f"Baixando o arquivo {file_name} do bucket {self.bucket_name}...")
            self.s3.download_file(self.bucket_name, file_name, file_name)
            logger.info(f"Arquivo {file_name} baixado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao baixar o arquivo: {e}")

    def delete_object(self, file_name):
        try:
            logger.info(f"Deletando o arquivo {file_name} do bucket {self.bucket_name}...")
            self.s3.delete_object(Bucket=self.bucket_name, Key=file_name)
            logger.info(f"Arquivo {file_name} deletado com sucesso!")
        except Exception as e:
            logger.error(f"Erro ao deletar o arquivo: {e}")
