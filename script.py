
# Создам HTML файлы для простого сайта магазина игрушек

# 1. Главная страница - index.html
index_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Антистресс-игрушки - Главная</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Навигационное меню -->
    <nav>
        <ul>
            <li><a href="index.html" class="active">Главная</a></li>
            <li><a href="catalog.html">Каталог</a></li>
            <li><a href="about.html">О нас</a></li>
            <li><a href="contact.html">Контакты</a></li>
            <li><a href="order.html">Заказать</a></li>
            <li><a href="https://www.psychologies.ru" target="_blank">Как выбрать антистресс</a></li>
        </ul>
    </nav>

    <!-- Основной контент -->
    <main>
        <h1>Добро пожаловать в магазин дизайнерских антистресс-игрушек!</h1>
        
        <section class="intro">
            <p>Наши игрушки — это милые персонажи, которые дарят радость и помогают расслабиться. 
            Каждая игрушка сочетает визуально привлекательный дизайн и тактильные антистресс-элементы.</p>
            <p>Теребите, щёлкайте, крутите — создавайте хорошее настроение каждый день!</p>
        </section>

        <!-- Примеры игрушек -->
        <section class="examples">
            <h2>Наши игрушки</h2>
            <div class="toy-grid">
                <div class="toy-item">
                    <img src="image_chick.jpg" alt="Солнечный цыплёнок" width="200">
                    <p>Солнечный Цыплёнок</p>
                </div>
                <div class="toy-item">
                    <img src="image_bunny.jpg" alt="Пушистый зайчик" width="200">
                    <p>Пушистый Зайчик</p>
                </div>
                <div class="toy-item">
                    <img src="image_cat.jpg" alt="Котик счастья" width="200">
                    <p>Котик Счастья</p>
                </div>
            </div>
        </section>

        <div class="button-container">
            <a href="catalog.html" class="button">Перейти в каталог</a>
        </div>
    </main>

    <!-- Подвал -->
    <footer>
        <p>&copy; 2025 Антистресс-игрушки. Все права защищены.</p>
    </footer>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("✓ index.html создан")
