# digikey_scraper.py
import requests
from bs4 import BeautifulSoup
from typing import List, Dict
from dataclasses import dataclass, asdict
from pymongo import MongoClient
from config import Config

@dataclass
class Product:
    manufacturer: str
    model: str
    description: str
    price: float
    stock: int
    url: str

class DigiKeyScraper:
    def __init__(self, config: Config):
        self.config = config
        self.client = MongoClient(config.MONGODB_URI)
        self.db = self.client[config.DATABASE_NAME]
        self.collection = self.db['digikey_products']

    def scrape_manufacturer_products(self, manufacturer: str) -> List[Product]:
        """
        抓取特定制造商的产品信息
        """
        search_url = f"{self.config.DIGIKEY_URL}/products/{manufacturer}"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        try:
            response = requests.get(search_url, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            products = []
            for product_element in soup.select('.product-row'):
                product = Product(
                    manufacturer=manufacturer,
                    model=product_element.select_one('.product-number').text.strip(),
                    description=product_element.select_one('.product-description').text.strip(),
                    price=self._parse_price(product_element.select_one('.unit-price')),
                    stock=self._parse_stock(product_element.select_one('.quantity')),
                    url=product_element.select_one('a')['href']
                )
                products.append(product)
            
            return products
        
        except Exception as e:
            print(f"抓取 {manufacturer} 产品时发生错误: {e}")
            return []

    def _parse_price(self, price_element) -> float:
        """解析价格"""
        try:
            return float(price_element.text.replace('$', '').replace(',', ''))
        except:
            return 0.0

    def _parse_stock(self, stock_element) -> int:
        """解析库存"""
        try:
            return int(stock_element.text.replace(',', ''))
        except:
            return 0

    def save_products(self, products: List[Product]):
        """保存产品到 MongoDB"""
        if products:
            self.collection.insert_many([asdict(product) for product in products])

    def scrape_and_save_manufacturers(self, manufacturers: List[str]):
        """抓取并保存多个制造商的产品"""
        for manufacturer in manufacturers:
            products = self.scrape_manufacturer_products(manufacturer)
            self.save_products(products)
            print(f"抓取 {manufacturer} 完成，共 {len(products)} 个产品")

def main():
    config = Config()
    scraper = DigiKeyScraper(config)
    manufacturers = [
        'Texas Instruments', 
        'Analog Devices', 
        'STMicroelectronics', 
        'NXP Semiconductors'
    ]
    scraper.scrape_and_save_manufacturers(manufacturers)

if __name__ == "__main__":
    main()