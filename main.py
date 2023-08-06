import requests
from notion.client import NotionClient
import schedule
import time

# 初始化
biorxiv_api_key = '你的biorxiv API key'  
notion_token = '你的notionIntegration token'
notion_database_id = 'Notion数据库页面id'

# 获取biorxiv最新文章  
def get_new_papers():
    url = 'https://api.biorxiv.org/details/biorxiv/latest/10'
    res = requests.get(url)
import requests
from notion.client import NotionClient
import schedule
import time


# 初始化
biorxiv_api_key = '你的biorxiv API key'  
notion_token = '你的notionIntegration token'
notion_database_id = 'Notion数据库页面id'


# 获取biorxiv最新文章  
def get_new_papers():
    url = 'https:api.biorxiv.org/details/biorxiv/latest/10'
    res = requests.get(url)
    papers = res.json()


# 导入到Notion数据库
def import_to_notion(papers):
    notion = NotionClient(token_v2=notion_token)
    for paper in papers:
        data = {
            '标题': paper['title'], 
            '作者': paper['authors_string'],
            '摘要': paper['abstract'],
        }
        notion.pages.create(parent={'database_id': notion_database_id}, 
                            properties=data)


# 定时执行        
schedule.every().day.at("10:00").do(main)


def main():
    papers = get_new_papers()
    import_to_notion(papers)


while True:
    schedule.run_pending()
    time.sleep(1)import requests
from notion.client import NotionClient
import schedule
import time


# 初始化
biorxiv_api_key = '你的biorxiv API key'  
notion_token = '你的notionIntegration token'
notion_database_id = 'Notion数据库页面id'


# 获取biorxiv最新文章  
def get_new_papers():
    url = 'https:api.biorxiv.org/details/biorxiv/latest/10'
    res = requests.get(url)
   papers = res.json()


# 导入到Notion数据库
def import_to_notion(papers):
    notion = NotionClient(token_v2=notion_token)
    for paper in papers:
        data = {
            '标题': paper['title'], 
            '作者': paper['authors_string'],
            '摘要': paper['abstract'],
        }
        notion.pages.create(parent={'database_id': notion_database_id}, 
                            properties=data)


# 定时执行        
schedule.every().day.at("10:00").do(main)


def main():
    papers = get_new_papers()
    import_to_notion(papers)


while True:
    schedule.run_pending()
    time.sleep(1)json()

# 导入到Notion数据库
def import_to_notion(papers):
    notion = NotionClient(token_v2=notion_token)
    for paper in papers:
        data = {
            '标题': paper['title'], 
            '作者': paper['authors_string'],
            '摘要': paper['abstract'],
        }
        notion.pages.create(parent={'database_id': notion_database_id}, 
                            properties=data)

# 定时执行        
schedule.every().day.at("10:00").do(main)

def main():
    papers = get_new_papers()
    import_to_notion(papers)

while True:
    schedule.run_pending()
    time.sleep(1)
