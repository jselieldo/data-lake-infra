#!/bin/bash

# Carrega as variáveis do arquivo .env
echo "Carrega as variáveis do arquivo .env..."
set -a
. ./.env  # Use ponto (.) em vez de source
set +a
#C:\Users\josee\Downloads\data-lake-infra\configs\hive\template-core-site.xml
# Caminho do template XML
HIVE_TEMPLATE_FILE="./configs/hive/template-hive-site.xml"
HIVE_OUTPUT_FILE="./configs/hive/hive-site.xml"

CORE_TEMPLATE_FILE="./configs/hive/template-core-site.xml"
CORE_OUTPUT_FILE="./configs/hive/core-site.xml"
TRINO_OUTPUT_FILE="./configs/trino/core-site.xml"

# Substitui as variáveis no arquivo template
echo "Substituindo variáveis de ambiente no template..."
sed -e "s|\${DB_HOST}|$DB_HOST|g" \
    -e "s|\${DB_PORT}|$DB_PORT|g" \
    -e "s|\${DB_NAME}|$DB_NAME|g" \
    -e "s|\${DB_USER}|$DB_USER|g" \
    -e "s|\${DB_PASSWORD}|$DB_PASSWORD|g" \
    -e "s|\${S3_ACCESS_KEY}|$AWS_ACCESS_KEY_ID|g" \
    -e "s|\${S3_SECRET_KEY}|$AWS_SECRET_ACCESS_KEY|g" \
    $HIVE_TEMPLATE_FILE > $HIVE_OUTPUT_FILE

echo "Arquivo hive-site.xml gerado com sucesso em $HIVE_OUTPUT_FILE"


# Substitui as variáveis no arquivo template
echo "Substituindo variáveis de ambiente no template..."
sed -e "s|\${DB_HOST}|$DB_HOST|g" \
    -e "s|\${DB_PORT}|$DB_PORT|g" \
    -e "s|\${DB_NAME}|$DB_NAME|g" \
    -e "s|\${DB_USER}|$DB_USER|g" \
    -e "s|\${DB_PASSWORD}|$DB_PASSWORD|g" \
    -e "s|\${S3_ACCESS_KEY}|$AWS_ACCESS_KEY_ID|g" \
    -e "s|\${S3_SECRET_KEY}|$AWS_SECRET_ACCESS_KEY|g" \
    $CORE_TEMPLATE_FILE > $CORE_OUTPUT_FILE
echo "Arquivo core-site.xml gerado com sucesso em $CORE_OUTPUT_FILE"

cp $CORE_OUTPUT_FILE $TRINO_OUTPUT_FILE
echo "Arquivo core-site.xml gerado com sucesso em $TRINO_OUTPUT_FILE"