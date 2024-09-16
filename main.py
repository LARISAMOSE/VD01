import requests

# URL изображения
url = "https://static.wixstatic.com/media/bb86c6_a6bca7e257fb4e5bb92fe6ec29a8088f~mv2.png/v1/crop/x_32,y_0,w_959,h_1024/fill/w_620,h_662,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/marianeuro8_Macaron_cakes_of_different_colors_lay_beautifully_o_526fecce-15f2-4a43-b8fb-4c.png"

# Отправляем запрос на получение изображения
response = requests.get(url)

# Указываем имя файла и путь для сохранения
filename = "image5.jpg"

# Сохраняем изображение
with open(filename, "wb") as file:
    file.write(response.content)

print(f"Изображение сохранено как {filename}")
