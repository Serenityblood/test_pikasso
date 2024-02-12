# test_pikasso
Приложение для загрузки файлов
## Стэк:
```
Django, DRF, PostgreSQL, Celery, Redis, Docker, Swagger
```

## Установка:

1. В корневой папке проекта:
```
Создать .env файл по примеру env-example
```
2. Запустить команду:
```
docker-compose up -d --build
```


## Эндпоинты:
### Всю документацию по реализованным эндпоинтам можно найти здесь: http://localhost:8000/swagger/

1. Загрузка файла: http://localhost:8000/api/v1/upload/
> Тело должно быть в формате form-data и иметь ключ file со значением в виде файла
> Пример ответа:
```bazaar
{
  "file": "txt",
  "uploaded_at": "2024-02-12T14:37:17.791Z",
  "processed": true
}
```
2. Выдача всех файлов: http://localhost:8000/api/v1/files/
> Пример ответа
```bazaar
{
  "count": 123,
  "next": "http://api.example.org/accounts/?page=4",
  "previous": "http://api.example.org/accounts/?page=2",
  "results": [
    {
      "file": "txt",
      "uploaded_at": "2024-02-12T14:39:57.208Z",
      "processed": true
    }
  ]
}
```
Автор проекта Бушланов Глеб