
from datetime import datetime, timezone
import requests
from config import NOTION_TOKEN, DATABASE_ID, headers


print(headers)
def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"

    payload = {"parent": {"database_id": DATABASE_ID}, "properties": data}
    print(requests.post(create_url, headers=headers, json=payload))
    res = requests.post(create_url, headers=headers, json=payload)
    print(res)
    print(res.status_code)
    return res

title = "Test Title"
description = "Test Description"
published_date = datetime.now().astimezone(timezone.utc).isoformat()
data = {
    "URL": {"title": [{"text": {"content": description}}]},
    "Title": {"rich_text": [{"text": {"content": title}}]},
    "Published": {"date": {"start": published_date, "end": None}}
}

create_page(data)