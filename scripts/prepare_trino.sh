#!/bin/bash

# Definir o diretório de dados
DATA_DIR="./trino-data"

# Verificar se o diretório ./trino-data existe
if [ ! -d "$DATA_DIR" ]; then
  echo "Diretório $DATA_DIR não encontrado. Criando o diretório..."
  mkdir -p "$DATA_DIR"
fi

# Alterar a propriedade do diretório ./trino-data para o usuário 1000:1000
echo "Alterando a propriedade do diretório $DATA_DIR para 1000:1000..."
sudo chown -R 1000:1000 "$DATA_DIR"

# Gerar um UUID
NODE_ID=$(uuidgen)

# Criar o arquivo node.properties com o conteúdo necessário
cat > ./configs/trino/node.properties <<EOL
node.environment=production
node.id=$NODE_ID
node.data-dir=/data
EOL

# Exibir o conteúdo do arquivo gerado (opcional)
echo "Arquivo node.properties gerado com o seguinte conteúdo:"
cat ./configs/trino/node.properties
