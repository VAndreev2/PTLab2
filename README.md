[![Build Status](https://app.travis-ci.com/kpdvstu/PTLab2.svg?branch=master)](https://app.travis-ci.com/kpdvstu/PTLab2)
# Лабораторная 2 по дисциплине "Технологии программирования"

Цели работы: 
1. Познакомиться c моделью MVC, ее сущностью и основными фреймворками на ее основе. 
2. Разобраться с сущностями «модель», «контроллер», «представление», их функциональным 
назначением. 
3. Получить навыки разработки веб-приложений с использованием MVC-фреймворков, написания 
модульных тестов к ним и интеграции приложений в конвейер CI / CD; 
4. Получить навыки управления автоматизированным тестированием и разворачиванием 
программного обеспечения, расположенного в системе Git, с помощью инструмента Travis CI.

Индивидуальное задание 
1. Выберите для Вашего проекта тип лицензии и добавьте файл с лицензией в проект. 
2. Доработайте проект магазина, добавив в него новую функциональность и информацию в базу 
данных в соответствии с типом магазина (согласно индивидуальному варианту: магазин мягкой мебели. Функционал: покупатель может положить товары в корзину, общая стоимость 
которой показывается пользователю. Корзина может содержать 
только один экземпляр одного товара.). Составьте 
модульные тесты к проекту, постарайтесь покрыть тестами максимально возможный объем кода. Для 
работы с этим заданием создайте новую ветку кода на основе главной и фиксируйте в нее весь 
программный код в процессе разработки. Добейтесь выполнения всех тестов проекта, после чего 
объедините текущую ветку кода с главной. 
3. Проанализируйте полученные результаты и сделайте выводы.

Выполнение работы заключалось в том, чтобы развернуть проект Django у себя на компьюетер и осуществить переработку магазина под свою тематику, а также добавить дополнительный функционал. В соответствие с изучаемой тематикой MVC / MTV, был реализован функционал магазина с использованием принципа MTV, потому что проекты Django придерживаются именно ему. В результате проектирования была добавлена новая таблица (CartItem), стилистически оформлены страницы, добавлена новая страница (success.html), информирующая пользователя об успешной покупке и деталей заказа. Добавлены unittest's, проверяющие работоспособность проекта.
