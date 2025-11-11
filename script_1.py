
# 2. Страница каталога - catalog.html
catalog_html = """<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Каталог игрушек</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <!-- Навигационное меню -->
    <nav>
        <ul>
            <li><a href="index.html">Главная</a></li>
            <li><a href="catalog.html" class="active">Каталог</a></li>
            <li><a href="about.html">О нас</a></li>
            <li><a href="contact.html">Контакты</a></li>
            <li><a href="order.html">Заказать</a></li>
            <li><a href="https://www.psychologies.ru" target="_blank">Как выбрать антистресс</a></li>
        </ul>
    </nav>

    <main>
        <h1 id="top">Каталог игрушек</h1>
        
        <!-- Навигация по разделам страницы -->
        <div class="page-nav">
            <p><strong>Разделы каталога:</strong></p>
            <a href="#animals">Зверята</a> | 
            <a href="#insects">Насекомые</a> | 
            <a href="#top">К началу</a>
        </div>

        <!-- Раздел Зверята -->
        <section id="animals">
            <h2>Зверята</h2>
            
            <h3>Особенности наших зверят:</h3>
            <ol>
                <li>Мягкий плюш приятный на ощупь</li>
                <li>Встроенные антистресс-элементы (pop-it, кнопки, спиннеры)</li>
                <li>Коллекционные дизайны с уникальным характером</li>
                <li>Подходят для любого возраста</li>
            </ol>

            <h3>Виды антистресс-элементов:</h3>
            <!-- Вложенный список -->
            <ul>
                <li>Тактильные элементы
                    <ul>
                        <li>Pop-it</li>
                        <li>Simple dimple</li>
                        <li>Кнопки</li>
                    </ul>
                </li>
                <li>Кинетические элементы
                    <ul>
                        <li>Спиннеры</li>
                        <li>Вращающиеся диски</li>
                    </ul>
                </li>
            </ul>

            <!-- Таблица с игрушками -->
            <table class="toy-table">
                <tr>
                    <th>Изображение</th>
                    <th>Название</th>
                    <th>Описание</th>
                    <th>Цена</th>
                </tr>
                <tr>
                    <td>
                        <!-- Миниатюра-ссылка на полное изображение -->
                        <a href="image_chick_full.html" target="_blank">
                            <img src="image_chick.jpg" alt="Солнечный цыплёнок" width="100">
                        </a>
                    </td>
                    <td>Солнечный Цыплёнок</td>
                    <td>Милый жёлтый цыплёнок с красным гребешком и кнопочками на животике</td>
                    <td>1200 ₽</td>
                </tr>
                <tr>
                    <td>
                        <a href="image_bunny_full.html" target="_blank">
                            <img src="image_bunny.jpg" alt="Пушистый зайчик" width="100">
                        </a>
                    </td>
                    <td>Пушистый Зайчик</td>
                    <td>Нежный бежевый зайчик с фиолетовыми ушками и спиральным элементом</td>
                    <td>1500 ₽</td>
                </tr>
                <tr>
                    <td>
                        <a href="image_cat_full.html" target="_blank">
                            <img src="image_cat.jpg" alt="Котик счастья" width="100">
                        </a>
                    </td>
                    <td>Котик Счастья</td>
                    <td>Бежевый котик с пуговками-глазками и синей кнопкой-смайликом</td>
                    <td>1350 ₽</td>
                </tr>
                <tr>
                    <td>
                        <a href="pink_bear_full.html" target="_blank">
                            <img src="pink_bear.png" alt="Розовый мишка" width="100">
                        </a>
                    </td>
                    <td>Розовый Мишка</td>
                    <td>Розовый плюшевый мишка с антистресс-кнопкой</td>
                    <td>1400 ₽</td>
                </tr>
            </table>
        </section>

        <!-- Раздел Насекомые -->
        <section id="insects">
            <h2>Насекомые</h2>
            
            <h3>Особенности насекомых:</h3>
            <ul>
                <li>Уникальные дизайны насекомых</li>
                <li>Светящиеся элементы для вечернего использования</li>
                <li>Металлические детали высокого качества</li>
            </ul>

            <!-- Таблица с насекомыми -->
            <table class="toy-table">
                <tr>
                    <th>Изображение</th>
                    <th>Название</th>
                    <th>Описание</th>
                    <th>Цена</th>
                </tr>
                <tr>
                    <td>
                        <a href="image_ladybug_full.html" target="_blank">
                            <img src="image_ladybug.jpg" alt="Божья коровка удачи" width="100">
                        </a>
                    </td>
                    <td>Божья Коровка Удачи</td>
                    <td>Красная божья коровка с металлическими точками-кнопками</td>
                    <td>1100 ₽</td>
                </tr>
                <tr>
                    <td>
                        <a href="image_butterfly_full.html" target="_blank">
                            <img src="image_butterfly.jpg" alt="Волшебная бабочка" width="100">
                        </a>
                    </td>
                    <td>Волшебная Бабочка</td>
                    <td>Чёрная бабочка со светящимися фиолетовыми узорами</td>
                    <td>1600 ₽</td>
                </tr>
            </table>
        </section>

        <div class="page-nav">
            <a href="#top">Вернуться к началу</a>
        </div>
    </main>

    <footer>
        <p>&copy; 2025 Антистресс-игрушки. Все права защищены.</p>
    </footer>
</body>
</html>"""

with open('catalog.html', 'w', encoding='utf-8') as f:
    f.write(catalog_html)

print("✓ catalog.html создан")
