from starlette.config import Config

config = Config('.env')

PROJECT_NAME = 'Giggy'
API_VERSION = '1.0'
API_PREFIX = '/api'
DEBUG = config('DEBUG', cast=bool, default=True)

HOST = config('HOST', cast=str, default='0.0.0.0')
PORT = config('PORT', cast=int, default=8080)
GIGACHAT_CREDENTIAL = config('GIGACHAT_CREDENTIAL', cast=str, default=None)
PRIMING_MESSAGE = config('PRIMING_MESSAGE', cast=str, default="описание, одежда, личные качества, желания, образ жизни, факты их жизни, место жительства, возраст")
DATABASE_PATH="db/sqll.db"
