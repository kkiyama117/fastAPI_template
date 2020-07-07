import os

MODE = os.getenv("APP_MODE", default="DEVELOPMENT")
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
ALLOWED_ORIGINS = (
    ["https://portfolio.hinatan.jp"]
    if MODE == "PRODUCTION"
    else ["http://localhost", "http://localhost:3000", "https://postwoman.io"]
)
