# api_yatube

[![CI](https://github.com/IlyaVasilevsky47/api_yatube/actions/workflows/main.yml/badge.svg?branch=master)](https://github.com/IlyaVasilevsky47/api_yatube/actions/workflows/main.yml)

API Yatube - это программный интерфейс, разработанный для блог-платформы [Yatube](https://github.com/IlyaVasilevsky47/yatube). Он предоставляет набор инструментов и протоколов для управления и доступа к контенту на платформе. С помощью API Yatube разработчики и пользователи могут создавать новые функции и приложения, улучшать взаимодействие с контентом и расширять возможности блог-платформы.

## Запуск проекта:
1. Клонируем проект.
```bash
git clone
```

2. Создаем и активируем виртуальное окружение.
```bash
python -m venv venv
source venv/scripts/activate
```

3. Обновляем менеджер пакетов pip и устанавливаем зависимости из файла requirements.txt.
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Создаем базу данных. 
```bash
python yatube_api/manage.py migrate 
```

5. Запускаем проект.
```bash
python yatube_api/manage.py runserver 
```

## Примеры запросов к API:
### url: http://127.0.0.1:8000/api/v1/posts/
#### GET запрос:
```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```
---
#### POST запрос:
Входные данные:
```json
{
  "text": "string",
  "image": "string",
  "group": 0
}
```
---
Полученные данные:
```json
{
  "id": 0,
  "author": "string",
  "text": "string",
  "pub_date": "2019-08-24T14:15:22Z",
  "image": "string",
  "group": 0
}
```

## Документация:
После запуска сервера, заходим в ReDoc по ссылке:
```url
http://127.0.0.1:8000/redoc/
```

## Автор:
- Василевский И.А.
- [GitHub](https://github.com/IlyaVasilevsky47)
- [Почта](vasilevskijila047@gmail.com)
- [Вконтакте](https://vk.com/ilya.vasilevskiy47)

## Технический стек
- Python 3.7.9
- Django 3.2.16
- Django REST Framework 3.12.4
  - Simple JWT 4.7.2
- PyJWT 2.1.0
- Djoser 2.2.2
