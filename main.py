import requests

# URL изображения
url = "https://e3.edimdoma.ru/data/recipes/0010/9596/109596-ed4_wide.jpg?1628781622"

# Отправляем запрос на получение изображения
response = requests.get(url)

# Указываем имя файла и путь для сохранения
filename = "image4.jpg"

# Сохраняем изображение
with open(filename, "wb") as file:
    file.write(response.content)

print(f"Изображение сохранено как {filename}")
