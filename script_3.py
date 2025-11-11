
# 4. Страница контактов - contact.html
contact_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Контакты</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Навигационное меню -->
    <nav>
        <ul>
            <li><a href="index.html">Главная</a></li>
            <li><a href="catalog.html">Каталог</a></li>
            <li><a href="about.html">О нас</a></li>
            <li><a href="contact.html" class="active">Контакты</a></li>
            <li><a href="order.html">Заказать</a></li>
            <li><a href="https://www.psychologies.ru" target="_blank">Как выбрать антистресс</a></li>
        </ul>
    </nav>

    <main>
        <h1>Свяжитесь с нами</h1>
        
        <section class="contact-section">
            <p>Если у вас есть вопросы или предложения, пожалуйста, заполните форму ниже, 
            и мы свяжемся с вами в ближайшее время.</p>

            <!-- Форма обратной связи -->
            <form action="https://httpbin.org/post" method="POST" class="contact-form">
                <label for="surname">Фамилия: *</label>
                <input type="text" id="surname" name="surname" required>

                <label for="name">Имя: *</label>
                <input type="text" id="name" name="name" required>

                <label for="group">Группа:</label>
                <input type="text" id="group" name="group" placeholder="Например, ИВТ-123">

                <label for="phone">Мобильный телефон: *</label>
                <input type="text" id="phone" name="phone" required placeholder="+7 (999) 123-45-67">

                <label for="email">Email: *</label>
                <input type="email" id="email" name="email" required placeholder="example@mail.ru">

                <label for="date">Дата отправки:</label>
                <input type="date" id="date" name="send_date">

                <button type="submit">Отправить</button>
            </form>

            <div class="contact-info">
                <h2>Наши контакты</h2>
                <p><strong>Телефон:</strong> +7 (999) 123-45-67</p>
                <p><strong>Email:</strong> info@antistress-toys.ru</p>
                <p><strong>Адрес:</strong> г. Москва, ул. Радости, д. 15</p>
            </div>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Антистресс-игрушки. Все права защищены.</p>
    </footer>
</body>
</html>"""

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(contact_html)

print("✓ contact.html создан")
