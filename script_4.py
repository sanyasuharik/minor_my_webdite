
# 5. Страница заказа - order.html
order_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Оформить заказ</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Навигационное меню -->
    <nav>
        <ul>
            <li><a href="index.html">Главная</a></li>
            <li><a href="catalog.html">Каталог</a></li>
            <li><a href="about.html">О нас</a></li>
            <li><a href="contact.html">Контакты</a></li>
            <li><a href="order.html" class="active">Заказать</a></li>
            <li><a href="https://www.psychologies.ru" target="_blank">Как выбрать антистресс</a></li>
        </ul>
    </nav>

    <main>
        <h1>Оформить заказ</h1>
        
        <section class="order-section">
            <p>Заполните форму ниже, чтобы оформить заказ. Мы свяжемся с вами для подтверждения.</p>

            <!-- Форма заказа -->
            <form action="https://httpbin.org/post" method="POST" class="order-form">
                
                <h2>Информация о товаре</h2>
                
                <label for="toy_name">Название игрушки:</label>
                <input type="text" id="toy_name" name="toy_name" placeholder="Например, Солнечный Цыплёнок">

                <label for="quantity">Количество:</label>
                <input type="number" id="quantity" name="quantity" min="1" max="10" value="1">

                <h2>Способ доставки</h2>
                
                <div class="radio-group">
                    <label>
                        <input type="radio" name="delivery_type" value="pickup" checked>
                        Самовывоз
                    </label>
                    <label>
                        <input type="radio" name="delivery_type" value="courier">
                        Курьер
                    </label>
                    <label>
                        <input type="radio" name="delivery_type" value="post">
                        Почта России
                    </label>
                </div>

                <h2>Дополнительные опции</h2>
                
                <div class="checkbox-group">
                    <label>
                        <input type="checkbox" name="gift_wrapping" value="yes">
                        Подарочная упаковка (+200 ₽)
                    </label>
                    <label>
                        <input type="checkbox" name="accessories" value="yes">
                        Дополнительные аксессуары (+300 ₽)
                    </label>
                </div>

                <label for="delivery_date">Желаемая дата доставки:</label>
                <input type="date" id="delivery_date" name="delivery_date">

                <h2>Ваши данные</h2>
                
                <label for="customer_name">Имя покупателя: *</label>
                <input type="text" id="customer_name" name="customer_name" required>

                <label for="customer_password">Пароль для входа: *</label>
                <input type="password" id="customer_password" name="customer_password" required>

                <label for="promo_code">Промокод:</label>
                <input type="text" id="promo_code" name="promo_code" value="WELCOME10">

                <!-- Скрытое поле -->
                <input type="hidden" name="user_id" value="guest123">

                <button type="submit">Оформить заказ</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2025 Антистресс-игрушки. Все права защищены.</p>
    </footer>
</body>
</html>"""

with open('order.html', 'w', encoding='utf-8') as f:
    f.write(order_html)

print("✓ order.html создан")
