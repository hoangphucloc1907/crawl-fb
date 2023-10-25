import json

# Đọc dữ liệu từ tệp JSON gốc
with open('phuclongcoffeeandtea.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Tạo danh sách để lưu thông tin về tên và ID của người bình luận
commenters = []

# Lặp qua các bài viết và lấy thông tin người bình luận
for post in data:
    if 'comments' in post:
        for comment in post['comments']['data']:
            if 'from' in comment:
                commenter_info = comment['from']
                name = commenter_info['name']
                id = commenter_info['id']
                commenters.append({'name': name, 'id': id})

# Ghi danh sách người bình luận vào tệp JSON mới
with open('id_user.json', 'w', encoding='utf-8') as output_file:
    json.dump(commenters, output_file, ensure_ascii=False, indent=4)

print("Dữ liệu đã được ghi vào tệp id_user.json")