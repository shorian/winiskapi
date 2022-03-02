import os
from winiskapi import create_app

app = create_app(os.getenv("FLASK_CONFIG") or "development")
