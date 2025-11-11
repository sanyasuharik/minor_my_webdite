
# Создаём страницы с полноразмерными изображениями для открытия в новом окне
# Эти страницы будут открываться при клике на миниатюры в каталоге

# Страница с полным изображением цыплёнка
chick_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Солнечный Цыплёнок - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="image_chick.jpg" alt="Солнечный Цыплёнок">
</body>
</html>"""

with open('image_chick_full.html', 'w', encoding='utf-8') as f:
    f.write(chick_full)

# Страница с полным изображением зайчика
bunny_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Пушистый Зайчик - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="image_bunny.jpg" alt="Пушистый Зайчик">
</body>
</html>"""

with open('image_bunny_full.html', 'w', encoding='utf-8') as f:
    f.write(bunny_full)

# Страница с полным изображением котика
cat_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Котик Счастья - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="image_cat.jpg" alt="Котик Счастья">
</body>
</html>"""

with open('image_cat_full.html', 'w', encoding='utf-8') as f:
    f.write(cat_full)

# Страница с полным изображением мишки
bear_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Розовый Мишка - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="pink_bear.png" alt="Розовый Мишка">
</body>
</html>"""

with open('pink_bear_full.html', 'w', encoding='utf-8') as f:
    f.write(bear_full)

# Страница с полным изображением божьей коровки
ladybug_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Божья Коровка Удачи - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="image_ladybug.jpg" alt="Божья Коровка Удачи">
</body>
</html>"""

with open('image_ladybug_full.html', 'w', encoding='utf-8') as f:
    f.write(ladybug_full)

# Страница с полным изображением бабочки
butterfly_full = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Волшебная Бабочка - Полное изображение</title>
    <style>
        body {
            margin: 0;
            padding: 20px;
            background-color: #fff5f8;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        img {
            max-width: 600px;
            max-height: 400px;
            border-radius: 10px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <img src="image_butterfly.jpg" alt="Волшебная Бабочка">
</body>
</html>"""

with open('image_butterfly_full.html', 'w', encoding='utf-8') as f:
    f.write(butterfly_full)

print("✓ Страницы с полноразмерными изображениями созданы")
print("\nВсе файлы HTML и CSS успешно созданы!")
