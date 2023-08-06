# main.py

import os
import requests
from notion.client import NotionClient

# 获取Secrets
notion_token = os.getenv('NOTION_TOKEN')
notion_database_id = os.getenv('NOTION_DATABASE_ID') 

# 初始化客户端
notion = NotionClient(auth=notion_token)

# 获取biorxiv文章
response = requests.get("https://api.biorxiv.org/details/biorxiv/latest/10")
papers = response.json()

# 遍历导入Notion    
for paper in papers:
    data = {
        "标题": paper["title"],
        "作者": paper["authors_string"], 
        "摘要": paper["abstract"]
    }
    
    notion.pages.create(
        parent={"database_id": notion_database_id},
        properties=data
    )
