# Electronic Components Scraper

## 项目描述
聚合电子元器件数据，从 DigiKey 和 ICSource 网站抓取产品信息、库存和热度数据。

## 环境准备
1. Python 3.8+
2. MongoDB
3. 安装依赖: `pip install -r requirements.txt`

## 配置
1. 修改 `config.py`
   - 设置 MongoDB 连接
   - 添加 ICSource 登录凭据

## 运行
```bash
python main.py
