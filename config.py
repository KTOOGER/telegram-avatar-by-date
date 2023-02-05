from os import getenv
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('/.env.local')

load_dotenv(dotenv_path=dotenv_path)

api_id = getenv('API_ID')
api_hash = getenv('API_HASH')
session_name = getenv('SESSION_NAME') or "default"

images_path = getenv('IMAGES_PATH') or "./images/"
sessions_path = getenv('SESSIONS_PATH') or "./sessions/"

time_zone = getenv('IMAGES_PATH') or "Europe/Moscow"
