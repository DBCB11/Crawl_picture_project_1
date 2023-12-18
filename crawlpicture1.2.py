from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import os
import requests
import time

# def download_person_image(save_path, race=None, age=None)
def download_person_image(save_path, etnic = None, age = None, gender = None):

    if age is not None and isinstance(age, int):
        if age < 12:
            age = "all"
        elif 12 <= age <= 18:
            age = "12-18"
        elif 19 <= age <= 25:
            age = "19-25"
        elif 26 <= age <= 35:
            age = "26-35"
        elif 36 <= age <= 50:
            age = "35-50"
        elif age > 50:
            age = "50"
    else: 
        age = "all"
    if etnic is None:
        etnic = "all"
    if gender is None:
        gender = "all"

    # Khởi tạo trình duyệt Chrome với Selenium
    driver = webdriver.Chrome()

    # Tạo URL với các thông số sắc tộc và tuổi
    url = "https://this-person-does-not-exist.com/"
    
    # Mở trang web
    driver.get(url)

    # Xác định phần tử select bằng name
    my_select_gender = Select(driver.find_element(By.NAME, "gender"))
    my_select_age = Select(driver.find_element(By.NAME, "age"))
    my_select_ethnicity = Select(driver.find_element(By.NAME, "etnic"))
    # Xác định nút bấm refresh
    my_button_refresh = driver.find_element(By.ID, "reload-button")

    # Chọn option cụ thể
    my_select_gender.select_by_value(gender)
    my_select_age.select_by_value(age)
    my_select_ethnicity.select_by_value(etnic)
    # Sau khi chọn xong thì click nút refresh 
    my_button_refresh.click()

    # Vì thời gian để refresh ảnh là 3s nên để 5s cho thoải mái 
    time.sleep(5)

    # Tìm phần tử img có id = "avater" bằng cách sử dụng biểu thức XPath 
    img = driver.find_element(By.XPATH, "//img[@id='avatar']")
    # Lấy src của img sau khi đã thực hiện các click 
    img_url = img.get_attribute("src")
    response = requests.get(img_url)
    img_path = os.path.join(save_path, "test3.jpg")

    if response.status_code == 200:
        img_data = response.content
        with open(img_path, 'wb') as img_file:
            img_file.write(img_data)
        print(f"Ảnh đã được tải và lưu tại: {save_path}")
    else:
        print(f"Không thể truy cập ảnh. Mã trạng thái: {response.status_code}")

if __name__ == "__main__":
    # Tạo thư mục để lưu ảnh
    save_directory = "person_images1"
    os.makedirs(save_directory, exist_ok=True)

    # Thực hiện việc tải ảnh với các thông số mong muốn
    download_person_image(save_directory)
