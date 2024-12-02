# main.py
from config import Config
from digikey_scraper import DigiKeyScraper
from icsource_scraper import ICSourceScraper

def main():
    config = Config()
    
    # DigiKey 抓取
    digikey_scraper = DigiKeyScraper(config)
    manufacturers = [
        'Texas Instruments', 
        'Analog Devices', 
        'STMicroelectronics', 
        'NXP Semiconductors'
    ]
    digikey_scraper.scrape_and_save_manufacturers(manufacturers)
    
    # ICSource 抓取
    icsource_scraper = ICSourceScraper(config)
    # 从 DigiKey 抓取的产品中获取产品 ID 并抓取库存
    client = config.MongoClient(config.MONGODB_URI)
    db = client[config.DATABASE_NAME]
    products = db['digikey_products'].find({}, {'model': 1})
    product_ids = [product['model'] for product in products]
    
    inventories = icsource_scraper.get_product_inventory(product_ids)
    icsource_scraper.save_inventories(inventories)

if __name__ == "__main__":
    main()