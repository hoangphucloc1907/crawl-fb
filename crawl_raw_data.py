# https://developers.facebook.com/docs/graph-api/reference/post
import requests
import json
import time
import csv

PAGE = 'phuclongcoffeeandtea' # Page Id or Username
LIMIT = 100 # https://developers.facebook.com/docs/graph-api/overview/rate-limiting
FIELDS = 'id,message,comments' # https://developers.facebook.com/docs/graph-api/reference/post
SLEEP = 3 # Seconds
MAX_POSTS = 50


ACCESS_TOKEN = ''

''' For Cookie
1. Reload https://graph.facebook.com/me?access_token={YOUR_ACCESS_TOKEN_HERE} with F12
2. Go to the Network Panel and copy value of the cookie param in Request Headers
'''
COOKIE = ''

url = f'https://graph.facebook.com/{PAGE}/posts?limit={LIMIT}&fields={FIELDS}&access_token={ACCESS_TOKEN}'
fields_set = set(FIELDS.replace(' ', '').split(','))
sess = requests.Session()

def get_data_and_next_url(url):
    response = sess.get(url, headers={'cookie': COOKIE})
    response = json.loads(response.text)

    try: data = response['data']
    except:
        print(response['error']['message'])
        data = []

    try:
        next_url = response['paging']['next']
        time.sleep(SLEEP)
    except:
        print('Cannot find next URL')
        next_url = None
    return data, next_url

# # Mở tệp CSV để ghi
# with open(f'{PAGE}.csv', 'w', newline='', encoding='utf-8') as file:
#     # Tạo một đối tượng CSV writer
#     csv_writer = csv.writer(file)
# 
#     # Ghi tiêu đề (header) của các trường
#     header = list(fields_set)
#     csv_writer.writerow(header)
# 
#     while url is not None:
#         print(f'\nGetting {LIMIT} posts from {url}')
#         data, url = get_data_and_next_url(url)
# 
#         # Lặp qua các bài viết và ghi vào tệp CSV
#         for post in data:
#             # Tạo một danh sách chứa giá trị của các trường
#             row = [post.get(field, '') for field in header]
#             csv_writer.writerow(row)


# Mở tệp JSON để ghi
with open(f'{PAGE}.json', 'w', encoding='utf-8') as file:
    data_to_export = []  # Danh sách lưu trữ dữ liệu

    post_count = 0  # Số lượng bài viết đã thu thập

    while url is not None and post_count < MAX_POSTS:  # Thêm kiểm tra số lượng bài viết
        print(f'\nGetting {LIMIT} posts from {url}')
        data, url = get_data_and_next_url(url)

        for post in data:
            # Tạo một từ điển chứa giá trị của các trường
            post_data = {field: post.get(field, '') for field in fields_set}
            data_to_export.append(post_data)
            post_count += 1

        if post_count >= MAX_POSTS: #Giới hạn bài viết ko thôi nó lấy tất cả các ba viết từ trước đến giờ => rất lâu
            print(f'Đã thu thập đủ {MAX_POSTS} bài viết. Dừng thu thập.')
            break

    # Ghi dữ liệu JSON vào tệp
    json.dump(data_to_export, file, ensure_ascii=False, indent=4)
