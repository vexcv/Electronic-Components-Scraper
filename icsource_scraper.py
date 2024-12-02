# icsource_scraper.py
import requests
from bs4 import BeautifulSoup
import pandas as pd
from dataclasses import dataclass
from typing import List, Dict
from pymongo import MongoClient
from config import Config
import datetime

@dataclass
class ProductInventory:
    product_id: str
    manufacturer: str
    quantity: int
    country: str
    company: str
    rating: float

class ICSourceScraper:
    def __init__(self, config: Config):
        self.config = config
        self.client = MongoClient(config.MONGODB_URI)
        self.db = self.client[config.DATABASE_NAME]
        self.collection = self.db['icsource_inventory']
        
    def login(self):
        """模拟登录 ICSource"""
        session = requests.Session()
        login_url = f"{self.config.ICSOURCE_URL}/login"
        
        payload = {
            'username': self.config.ICSOURCE_USERNAME,
            'password': self.config.ICSOURCE_PASSWORD
        }
        
        response = session.post(login_url, data=payload)
        return session if response.ok else None

    def get_product_inventory(self, product_ids: List[str]) -> List[ProductInventory]:
        """获取多个产品的库存信息"""
        session = self.login()
        if not session:
            print("登录失败")
            return []

        inventories = []
        for product_id in product_ids:
            url = f"{self.config.ICSOURCE_URL}/inventory/{product_id}"
            response = session.get(url)
            
            if response.ok:
                soup = BeautifulSoup(response.text, 'html.parser')
                inventory = self._parse_inventory(soup, product_id)
                inventories.extend(inventory)
        
        return inventories

    def _parse_inventory(self, soup: BeautifulSoup, product_id: str) -> List[ProductInventory]:
        """解析单个产品的库存信息"""
        rows = soup.select('table.inventory-table tr')
        inventories = []

        for row in rows[1:]:  # 跳过表头
            cols = row.find_all('td')
            if len(cols) >= 5:
                inventory = ProductInventory(
                    product_id=product_id,
                    manufacturer=cols[1].text.strip(),
                    quantity=int(cols[2].text.strip().replace(',', '')),
                    country=cols[3].text.strip(),
                    company=cols[4].text.strip(),
                    rating=self._calculate_rating(product_id)
                )
                inventories.append(inventory)
        
        return inventories

    def _calculate_rating(self, product_id: str) -> float:
        """计算产品评分"""
        # 这里可以根据实际需求实现复杂的评分逻辑
        url = f"{self.config.ICSOURCE_URL}/product_rating/{product_id}"
        # 模拟获取评分的逻辑
        return 0.0

    def save_inventories(self, inventories: List[ProductInventory]):
        """保存库存到数据库"""
        if inventories:
            self.collection.insert_many([vars(inv) for inv in inventories])

def main():
    config = Config()
    scraper = ICSourceScraper(config)
    
    # 从 DigiKey 抓取的产品中获取产品 ID
    client = MongoClient(config.MONGODB_URI)
    db = client[config.DATABASE_NAME]
    products = db['digikey_products'].find({}, {'model': 1})
    
    product_ids = [product['model'] for product in products]
    inventories = scraper.get_product_inventory(product_ids)
    scraper.save_inventories(inventories)

if __name__ == "__main__":
    main()