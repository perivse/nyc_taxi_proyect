NYC Taxi Data Pipeline 🚕
Este proyecto procesa grandes volúmenes de datos de los taxis de Nueva York utilizando PySpark. El pipeline realiza tareas de extracción, limpieza y transformación de datos en formato Parquet.

🚀 Instrucciones de Ejecución
Para reproducir este proyecto, sigue estos pasos detallados:

1. Requisitos Previos
Asegúrate de tener instalado:

Python 3.9+

Java 8 o 11 (Necesario para Spark)

Apache Spark 3.x

2. Configuración del Entorno
Es recomendable usar un entorno virtual para evitar conflictos de dependencias:

Bash
# Crear el entorno virtual
python -m venv spark_env

# Activar el entorno
# En Windows:
.\spark_env\Scripts\activate
# En Linux/Mac:
source spark_env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
3. Preparación de los Datos
Debido al tamaño de los archivos, la carpeta data/ no se incluye en el repositorio. Debes seguir estos pasos:

Crea la estructura de carpetas:

Bash
mkdir -p data/raw data/processed
Descarga los datasets necesarios (formato Parquet) desde el sitio oficial de NYC TLC Trip Record Data.

Coloca los archivos descargados en la carpeta data/raw/.

4. Ejecución del Pipeline
Para procesar los datos, ejecuta el script principal:

Bash
python main.py
(O el nombre de tu script principal, por ejemplo: spark-submit src/transform.py)

🛠️ Estructura del Proyecto
data/: Carpeta (ignorada por Git) para almacenar archivos .parquet.

notebooks/: Análisis exploratorio de datos (EDA).

src/: Scripts de procesamiento y lógica del pipeline.

.gitignore: Configuración para evitar subir archivos pesados y entornos virtuales.

📊 Pipeline de Datos
El flujo de trabajo consiste en:

Ingesta: Lectura de archivos Parquet crudos.

Limpieza: Filtrado de valores nulos y eliminación de outliers en las tarifas.

Transformación: Creación de nuevas métricas (tiempo de viaje, velocidad promedio).

Almacenamiento: Escritura de los resultados en data/processed/ para su posterior análisis.

Linea de uso:
    Correr notebooks del 01 al 04, despues dashboard.py!