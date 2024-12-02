#!/bin/bash

# Exit on any error
set -e

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
