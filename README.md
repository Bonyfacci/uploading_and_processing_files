## Загрузка и обработка файлов Django REST API

### Стек технологий:

 - ![alt text](https://img.shields.io/badge/Python-3.11.5-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-4.2.9-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/PostgreSQL-15.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=%234169E1)

### Описание проекта
Разработан Django REST API, который позволяет загружать файлы на сервер, а затем асинхронно обрабатывать их с использованием Celery.

Реализован механизм для обработки различных типов файлов (изображений, текстовых файлов и т.д.).

Реализован фронтенд для взаимодействия с пользователем.

<details>
<summary>Для запуска через консоль необходимо:</summary>

 - Клонировать проект на собственный диск в новом каталоге
 - Создать виртуальное окружение
 - Установить зависимости командой:
```python
    pip install -r requirements.txt
```
 <details>
   <summary>Прописать переменные окружения в файле `.env.sample`</summary>
   
    ```dotenv
    SECRET_KEY='Секретный ключ Django'
    DEBUG='True/False', например: True
    
    POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'file_db'
    POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
    POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
    POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' (для Docker)
    POSTGRES_DB_PORT='Порт базы данных', например: '5432'
    ```
 </details>

 <details>
   <summary>Создать базу данных (в данной работе используется PostgreSQL)</summary>

 ```python
     psql -U postgres
     create database file_db;
     \q
 ```
   </details>

 - Применить миграции командой:
   ```python
       python manage.py migrate
   ```

 <details>
   <summary>Для создания тестового пользователя - администратор:</summary>

   - login: admin
   - password: admin 
   ```python
        python manage.py csu
   ```
 </details>
 
 <details>
 <summary>Для запуска сервера через терминал:</summary>

   - Запустить Redis (в окне терминала под Ubuntu)
      ```python
          python manage.py runserver
      ```
   - Запустить celery (в другом окне терминала)
      ```python
          celery -A config worker -l INFO -P eventlet
      ```
   - Запустить tasks (в другом окне терминала)
      ```python
          celery -A config beat -l info -S django
      ```
   - Запустить сервер
      ```python
          python manage.py runserver
      ```
 </details>

</details>


<details>
<summary>Для запуска через Docker необходимо:</summary>

```python
    docker-compose up --build
```
 - Происходит сборка образа контейнера согласно инструкции в файле Dockerfile и последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml

</details>

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в окне терминала




### Как изменится архитектура, если мы ожидаем большую нагрузку
Большая нагрузка может быть вызвана: масштабированием приложения для пользователей, 
нагрузкой количества подключений, хранением большого количества информации (файлов) и потерей информации.

В приложении уже используется асинхронная обработка файлов с помощью Celery, а также используется СУБД PostgreSQL.
Примерные решения:
1. Размещение приложения на нескольких серверах.
2. Оптимизировать запросы к базе данных.
3. Резервное копирование данных.
4. Кэширование информации.


### Какую нагрузку в RPS сможет выдержать ваш сервис
RPS - количество запросов в секунду.

Для такого анализа и тестирования в реальных условиях можно воспользоваться инструментами для нагрузочного тестирования,
(например Apache) чтобы оценить, как приложение справляется с нагрузкой.

Данное приложение не имеет узких мест и достаточно оптимизировано. 
Соответственно на локальной машине может выдержать от нескольких сотен до нескольких тысяч запросов в секунду.

<details>
<summary><b>Connect with me:</b></summary>
   <p align="left">
       <a href="mailto:platonovpochta@gmail.com"><img img src="https://img.shields.io/badge/gmail-%23EA4335.svg?style=plastic&logo=gmail&logoColor=white" alt="Gmail"/></a>
       <a href="https://wa.me/79217853835"><img src="https://img.shields.io/badge/whatsapp-%2325D366.svg?style=plastic&logo=whatsapp&logoColor=white" alt="Whatsapp"/></a>
       <a href="https://t.me/platonov_sm"><img src="https://img.shields.io/badge/telegram-blue?style=plastic&logo=telegram&logoColor=white" alt="Telegram"/></a>
   </p>
</details>
