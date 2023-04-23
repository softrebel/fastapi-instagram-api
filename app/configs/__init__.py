from dotenv import load_dotenv
from pathlib import Path
dotenv_path = Path('.env.local')
load_dotenv(dotenv_path=dotenv_path)
from .database import *
from .authentication import *
