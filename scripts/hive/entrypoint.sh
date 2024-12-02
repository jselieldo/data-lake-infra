#!/bin/bash

# Exit on any error
set -e

echo "Substituindo variáveis no arquivo hive-site.xml..."

sed -i "s|\${DB_HOST}|$DB_HOST|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${DB_PORT}|$DB_PORT|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${DB_NAME}|$DB_NAME|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${DB_USER}|$DB_USER|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${DB_PASSWORD}|$DB_PASSWORD|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${S3_ACCESS_KEY}|$S3_ACCESS_KEY|g" /opt/hive/conf/hive-site.xml
sed -i "s|\${S3_SECRET_KEY}|$S3_SECRET_KEY|g" /opt/hive/conf/hive-site.xml

echo "Substituindo variáveis no arquivo core-site.xml..."

sed -i "s|\${S3_ACCESS_KEY}|$S3_ACCESS_KEY|g" /opt/hive/conf/core-site.xml
sed -i "s|\${S3_SECRET_KEY}|$S3_SECRET_KEY|g" /opt/hive/conf/core-site.xml

echo "Initializing Hive schema..."
/opt/hive/bin/schematool -dbType mysql -initSchema || echo "Schema already initialized."

echo "Waiting for MySQL to be ready..."
while ! nc -z "$DB_HOST" 3306; do
  echo "MySQL not available yet, retrying..."
  sleep 5
done

echo "Starting Hive Metastore service..."
/opt/hive/bin/hive --service metastore &

echo "Starting HiveServer2 service..."
exec /opt/hive/bin/hive --service hiveserver2
