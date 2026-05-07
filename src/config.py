import os

class Config:
    API_KEY = os.getenv("API_KEY", "your_default_api_key")
    MODEL_PATH = os.getenv("MODEL_PATH", "path/to/your/model")
    INPUT_DATA_PATH = os.path.join("data", "inputs")
    OUTPUT_DATA_PATH = os.path.join("data", "outputs")
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    MAX_RETRIES = 3
    TIMEOUT = 30  # seconds

    @staticmethod
    def get_database_uri():
        return os.getenv("DATABASE_URI", "sqlite:///default.db")