from os import getenv
from dotenv import load_dotenv
from pathlib import Path

dotenv_path = Path('.env.local')

load_dotenv(dotenv_path=dotenv_path)

api_id = getenv('API_ID')
api_hash = getenv('API_HASH')
session_name = getenv('SESSION_NAME') or "default"

system_version = getenv('SYSTEM_VERSION')

images_path = getenv('IMAGES_PATH') or "./images/"
sessions_path = getenv('SESSIONS_PATH') or "./sessions/"

images_name_template = getenv('IMAGES_NAME_TEMPLATE') or "%m-%d.png"

time_zone = getenv('TIME_ZONE') or "Europe/Moscow"

time_delta_hours = getenv('TIME_DELTA_HOURS') or 0