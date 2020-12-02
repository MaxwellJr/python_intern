# python_intern
---
## Docker-контейнеризация
В репозиторий добавлен Dockerfile, а также список зависимостей requirements.txt.
- Были установлены необходимые зависимости в виртуальной среде (python venv): requests, fastapi, uvicorn
- Экспорт зависимостей: pip freeze > requirements.txt
- Создание Dockerfile с ипользованием зависимостей из requirements.txt
- Создание контейнера (Docker image): docker build -t is_alive_host_image .
- Запуск приложения в Docker с ключом порта: docker run -p 8000:8000 is_alive_host_image

## requirements

- python 3.9
- В изначальном коде менять можно *всё*, вплоть до структуры файлов. 
- Использовать можно всё что угодно. 
- Таски со звёздочкой можно пропускать (или делать часть из них)
- Решение выложить через fork/копию/etc репозитория на github


## TODO

- реализовать функцию [is_alive_host](./app.py)

- покрыть функцию [тестами](./tests.py)

- развернуть вокруг функции веб сервис c помощью [fastapi](https://fastapi.tiangolo.com/)
```
>> curl your_service.loc:8001/healthz?hostname=semrush.com
{status: [up|down]}
```

- задача со *звёздочкой*: завернуть приложение в docker
- задача на *две звёздочки*: выложить куда-либо (heroku/DigitalOcean/etc) с помощью github-actions/gitlab/jenkins/etc
