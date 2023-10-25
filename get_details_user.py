import json
import requests
import csv


ACCESS_TOKEN = 'EAABwzLixnjYBO6djXsif24jocnWjNge2lrdjU3DDUDRc37stvPAS5sDK4sqo80Szv6xh1tgojNc3Gai59akWFRwxtpRoKrPJiEFfnOGFWZCFsDaJSgE9DYdxwFLWYjsSc3RsYk1ZB6CqAqqDsfieGYq9lg0H1VS0ju0racK9PbJ3VBrxZCC7awRTYV2mwwaClwqXpAS188ZD'
FIELDS = 'id,name,gender,location,hometown,birthday'

# Đọc danh sách người dùng từ tệp JSON
input_json_file = 'id_user.json'  # Thay đổi thành tên tệp JSON của bạn
with open(input_json_file, 'r', encoding='utf-8') as json_file:
    user_data = json.load(json_file)

# Mở tệp CSV để ghi
output_csv_file = 'user_data.csv'
with open(output_csv_file, 'w', newline='', encoding='utf-8') as csv_file:
    # Tạo một đối tượng CSV writer
    csv_writer = csv.writer(csv_file)

    # Ghi tiêu đề (header) của các trường
    header = FIELDS.split(',')
    csv_writer.writerow(header)

    # Lặp qua danh sách người dùng và lấy thông tin từ Facebook Graph API
    for user in user_data:
        user_id = user['id']
        url = f'https://graph.facebook.com/{user_id}?fields={FIELDS}&access_token={ACCESS_TOKEN}'
        response = requests.get(url)
        user_info = response.json()

        # Tạo một danh sách chứa giá trị của các trường
        row = [user_info.get(field, '') for field in header]
        csv_writer.writerow(row)
        print(f"Đã lấy dữ liệu cho {user_info.get('name')}")

print("Hoàn thành việc lấy dữ liệu và lưu vào tệp CSV.")
