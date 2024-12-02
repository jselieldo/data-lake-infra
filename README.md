
# Data Lake Setup with MinIO, Iceberg REST, and Trino

This repository provides a Docker Compose setup to configure a data lake environment using MinIO, Iceberg REST, and Trino. The stack is connected through a shared `data-lake` network, with MinIO serving as the object storage, Iceberg REST handling table catalogs, and Trino providing a SQL query engine.

---

## **Services Overview**

### **1. MinIO**
- Object storage compatible with AWS S3.
- Accessible via:
  - API: `http://localhost:9000`
  - Console: `http://localhost:9001`
- Credentials:
  - Default User: `admin`
  - Default Password: `password`
- Data is persisted in the `minio_data` volume.

### **2. Iceberg REST**
- REST API for managing Iceberg tables stored in MinIO.
- Accessible via: `http://localhost:8181`
- Configuration:
  - Warehouse directory: `s3://warehouse/`
  - Storage backend: MinIO

### **3. Trino**
- Distributed SQL query engine for large-scale analytics.
- Accessible via: `http://localhost:8090`
- Configuration:
  - Catalogs for Iceberg and MinIO are pre-configured.

### **4. MinIO Client (mc)**
- CLI tool for managing MinIO storage.
- Automatically creates and configures the `warehouse` bucket at startup.

---

## **Prerequisites**
1. Install [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/).
2. Clone this repository:
   ```bash
   git clone https://github.com/jselieldo/data-lake-infra.git
   cd data-lake-infra
   ```
3. Download necessary JARs:
  ```bash
   sh ./scripts/download_jars.sh
   ```
4. Generate the Hive configuration file:
  ```bash
   sh ./scripts/generate_hive_site.sh
   ```
5. Prepare Trino configuration:
  ```bash
   sh ./scripts/prepare_trino.sh
   ```
---

## **Setup Instructions**

### **1. Configure Environment Variables**
Create a `.env` file in the project root with the following content:

```env
# MinIO Credentials
MINIO_ROOT_USER=admin
MINIO_ROOT_PASSWORD=secure_password

# AWS Credentials for Iceberg REST
AWS_ACCESS_KEY_ID=admin
AWS_SECRET_ACCESS_KEY=secure_password
```

Ensure this file is not committed to version control by including `.env` in `.gitignore`.

### **2. Start the Services**
Run the following command to start the stack:
```bash
docker-compose up -d
```

This will spin up the following services:
- MinIO (`http://localhost:9000`, console: `http://localhost:9001`)
- Iceberg REST (`http://localhost:8181`)
- Trino (`http://localhost:8090`)

---

## **Usage**

### **1. Access MinIO**
1. Open the MinIO console at `http://localhost:9001`.
2. Log in using the credentials in the `.env` file.

### **2. Access Trino**
1. Navigate to `http://localhost:8090` for the Trino web interface.
2. Use Trino CLI or web UI to query data:
   - Example query:
     ```sql
     SELECT * FROM iceberg.default.nyc_taxis;
     ```

### **3. Manage Iceberg Tables**
Use the Iceberg REST API (`http://localhost:8181`) to manage table metadata.

---

## **Configuration Details**

### **1. MinIO**
- Configured with the `warehouse` bucket at startup.
- Data is stored in the `minio_data` Docker volume.

### **2. Iceberg REST**
- Backend storage: SQLite (default, for development).
- To use a production-ready database like PostgreSQL:
  1. Add a PostgreSQL service to the `docker-compose.yml`.
  2. Update the `rest` service configuration:
     ```yaml
     environment:
       - JDBC_CATALOG_URI=jdbc:postgresql://postgres:5432/iceberg_catalog
       - JDBC_CATALOG_USER=iceberg
       - JDBC_CATALOG_PASSWORD=secure_password
     ```

### **3. Trino**
- Configured with Iceberg and MinIO catalogs in `/etc/trino/catalog/`.

---

## **Future Improvements**
- **Security**:
  - Configure HTTPS for MinIO and Iceberg REST.
  - Implement authentication for Trino (e.g., basic auth or JWT).
- **Persistence**:
  - Migrate from SQLite to a production-ready database like PostgreSQL for Iceberg REST.
- **Monitoring**:
  - Add logging and monitoring tools, such as Prometheus and Grafana.

---

## **Contributing**
Feel free to contribute to this project by submitting issues or pull requests. Ensure your code follows best practices and is well-documented.

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.
