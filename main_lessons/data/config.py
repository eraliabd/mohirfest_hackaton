from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()

# .env fayl ichidan quyidagilarni o'qiymiz
BOT_TOKEN = env.str("BOT_TOKEN")  # Bot toekn
ADMINS = env.list("ADMINS")  # adminlar ro'yxati
CHANNEL_ID = env.list("CHANNEL_ID")
IP = env.str("ip")  # Xosting ip manzili

DB_USER = env.str("DB_USER")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_NAME = env.str("DB_NAME")
DB_HOST = env.str("DB_HOST")
