# Документация ГК Сибтехноцентр



___
Клонируем репозиторий на локальную машину:

```
https://github.com/zorgiy/STC_documentation.git
```
```
git clone git@github.com:zorgiy/STC_documentation.git
```
___
### Windows
<details><summary>Windows</summary>

Устанавливаем виртуальное окружение:

```
python -m venv env
```
Активируем виртуальное окружение:

```
source env/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver localhost:80
```
</details>

___
### MacOS, Linux
<details><summary>MacOS, Linux</summary>

Устанавливаем виртуальное окружение:

```
python3 -m venv env
```
Активируем виртуальное окружение:

```
source env/bin/activate
```



Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver localhost:80
```
</details>

___
#### Автор: [@zorgiy](https://github.com/zorgiy)