# TreadTalk_api

### Промежуточная версия API для приложения TreadTalk.

Доступные функции:  
- Получать токен аутентификации, передав логин и пароль
- Получать список всех постов или создавать новый
- Получать конкретный пост, редактировать или удалять его по id
- Получать список всех групп
- Получить информацию о группе по id
- Получать список всех комментариев поста с id=post_id или создавать новый
- Получать, редактировать или удалять комментарий по id y поста с id=post_id

### Технологии
Python 3.9.10  
Django 2.2.16 обновлено до Django 4.2.16  
### Запуск проекта в режиме разработки
- Установите и активируйте виртуальную среду
- Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
- В папке с файлами manage.py запустите команду:
```bash
python manage.py runserver
```
### Автор
Sergey Khryashchev (Khryashoff)
