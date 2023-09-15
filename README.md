# О проекте
![Static Badge](https://img.shields.io/badge/python%20-%20black?logo=python&logoColor=%23FFDE56)
![Static Badge](https://img.shields.io/badge/flask%20-%20black?logo=Flask&logoColor=%#000000)
![Static Badge](https://img.shields.io/badge/docker%20-%20black?logo=Docker&logoColor=%#2496ED)
![Static Badge](https://img.shields.io/badge/javascript%20-%20black?logo=javascript)
![Static Badge](https://img.shields.io/badge/html5%20-%20%23000000?logo=HTML5)
![Static Badge](https://img.shields.io/badge/css3%20-%20%23000000?logo=CSS3&logoColor=%231572B6)


Простой API сервис "Конвертер валют".

Источник курсов валют: https://www.cbr-xml-daily.ru/

Бэкенд: python 3.10 + flask 2.3.3. Фронтенд: html, css, js.
## API
`GET http://127.0.0.1:5000/api/rates?from=<currency1>&to=<currency2>&value=<value>`

- `<currency1>` - базовая валюта,
- `<currency2>` - валюта, в которую конвертируем,
- `<value>` - количество.

При успешной операции возвращает ответ статус `200` и ответ:
```
{
    "result": 96.6338
}
```
В случае отсутствия валюты в базе возвращает статус `404` и ответ:
```
{
    "error": "unknown currency"
}
```
Ошибка доступа к источнику данных в приложении не обрабатывается.

## Docker
Создаем образ
```
docker build -t flask_app_docker .
```
Запускаем контейнер
```
docker run -p 5000:5000 -d flask_app_docker
```

## WEB - интерфейс

Главная страница `http://127.0.0.1:5000/` с простым интерфейсом.

Для отправки запроса на сервер используется скрипт на языке JavaScript.

![web](/img/web.png)