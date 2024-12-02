# config.py
from dataclasses import dataclass

@dataclass
class Config:
    MONGODB_URI: str = "mongodb://localhost:27017/"
    DATABASE_NAME: str = "electronic_components"
    DIGIKEY_URL: str = "https://www.digikey.com/"
    ICSOURCE_URL: str = "https://www.icsource.com/"
    
    # 认证信息，建议使用环境变量
    ICSOURCE_USERNAME: str = ""
    ICSOURCE_PASSWORD: str = ""