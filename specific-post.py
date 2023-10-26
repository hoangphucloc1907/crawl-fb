import requests
import json

POST_ID = ''
FIELDS = 'id,message,comments'
ACCESS_TOKEN = ''  # Thay thế bằng access token Facebook của bạn
COOKIE = '' # Thay thế bằng cookies Facebook của bạn

url = f'https://graph.facebook.com/{POST_ID}?fields={FIELDS}&access_token={ACCESS_TOKEN}'

sess = requests.Session()

def get_data(url):
    response = sess.get(url, headers={'cookie': COOKIE})
    response = json.loads(response.text)

    return response

# Gửi một yêu cầu để lấy dữ liệu từ bài viết cụ thể
post_data = get_data(url)

# In hoặc xử lý dữ liệu theo cách cần thiết
print(json.dumps(post_data, indent=4, ensure_ascii=False))
