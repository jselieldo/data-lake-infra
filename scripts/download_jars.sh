#!/bin/bash

# Diretório onde os arquivos serão salvos
destino="./jars/"

# Criação do diretório (caso não exista)
mkdir -p "$destino"

# Baixando os arquivos com wget
wget -P "$destino" https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.6/hadoop-aws-3.3.6.jar
wget -P "$destino" https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.1026/aws-java-sdk-bundle-1.11.1026.jar
wget -P "$destino" https://repo1.maven.org/maven2/com/mysql/mysql-connector-j/8.3.0/mysql-connector-j-8.3.0.jar
wget -P "$destino" https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-hive-runtime/1.4.0/iceberg-hive-runtime-1.4.0.jar
wget -P "$destino" https://repo.maven.apache.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
wget -P "$destino" https://repo.maven.apache.org/maven2/org/apache/hadoop/hadoop-common/3.3.4/hadoop-common-3.3.4.jar

echo "Arquivos baixados com sucesso!"
