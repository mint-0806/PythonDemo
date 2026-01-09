SECRET_KEY = 'your_secret_key_here'  # 生成：import secrets; secrets.token_hex(16)
SQLALCHEMY_DATABASE_URI = 'sqlite:///book_reading.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = 'uploads'  # 书籍存储路径