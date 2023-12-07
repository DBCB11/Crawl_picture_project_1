from bs4 import BeautifulSoup
import os
import requests

# def download_person_image(save_path, race=None, age=None)
def download_person_image(save_path, race=None, age=None):
    # Tạo URL với các thông số sắc tộc và tuổi
    url = "https://this-person-does-not-exist.com/"
    """if race:
        url += f"?race={race}"
    if age:
        url += f"&age={age}"
        """

    response = requests.get(url)

    if response.status_code == 200:
        # Sử dụng BeautifulSoup để phân tích HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Tìm thẻ <img> chứa đường dẫn ảnh
        img_tag = soup.find('img', {'id': 'avatar'})
        if img_tag is not None:
            img_url = img_tag.get('src')

            # Tiếp tục với các bước khác nếu img_url không phải là None
            if img_url is not None:
                full_img_url = f"{url}/{img_url}"

                img_data = requests.get(full_img_url).content
                img_path = os.path.join(save_path, "test2.jpg")
                with open(img_path, 'wb') as img_file:
                    img_file.write(img_data)
                print(f"Ảnh đã được tải và lưu tại: {save_path}")
            else:
                print("Không tìm thấy thuộc tính 'src' trên thẻ <img>")
        else:
            print("Không tìm thấy thẻ <img> với id là 'avatar'")
    else:
        print(f"Không thể truy cập trang web. Mã trạng thái: {response.status_code}")

if __name__ == "__main__":
    # Tạo thư mục để lưu ảnh
    save_directory = "person_images1"
    os.makedirs(save_directory, exist_ok=True)

    # Thực hiện việc tải ảnh với các thông số mong muốn
    # download_person_image(save_directory, race="asian", age="12-18 years old")
    download_person_image(save_directory)  # Không có thông số cụ thể
