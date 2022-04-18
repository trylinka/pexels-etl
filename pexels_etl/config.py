import logging
import os

from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Setup global logging config for ETL
logger = logging.getLogger("pexels_etl")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s: %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

logger.addHandler(console_handler)

# Get variables from .env file
API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")
PHOTOS_TOPIC = os.getenv("PHOTOS_TOPIC")

N_RECORDS = int(os.getenv("N_RECORDS"))
BATCH_SIZE = int(os.getenv("BATCH_SIZE"))

# Database and script configs
SQLITE_DB = os.getenv("SQLITE_DB")
DDL_TABLES = os.getenv("DDL_TABLES")
