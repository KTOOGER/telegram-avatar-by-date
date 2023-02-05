# Изменение аватара в Telegram на основе даты

## Описание

При запуске меняет аватар пользователя telegram на заранее подготовленную картинку на основе текущей даты (месяц, день).

**Важно:** В результате выполнения будут удалены все предыдущие изображения профиля.

## Установка и запуск

1. Скачайте [исходный код](https://github.com/KTOOGER/telegram-avatar-by-date/archive/master.zip "Скачать zip архив"):

    ```bash
    git clone https://github.com/KTOOGER/telegram-avatar-by-date.git
    ```

2. Установите [Python](https://python.org/downloads)
3. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

4. Получите telegram api hash и api id с сайта [my.telegram.org](https://my.telegram.org).
5. (Необязательно) Добавьте свои api реквизиты в файл `.env.local`:

    **Подробнее:**  Создайте копию `.env.template` с названием `.env.local` и запишите в него session name (произвольно), api hash и api id.

    ```env
    API_ID = "************"
    API_HASH = "************"
    SESSION_NAME = "something"
    IMAGES_PATH = "./images/"
    ```

6. Добавить в папку `images/` изображения в формате `<месяц>-<день>.png`

    Например, для 5 февраля, файл будет называться `2-5.png`

7. Запустить `main.py`

    Например, (если выполнен пункт номер 5):

    ```bath
    python main.py
    ```

    или

    ```bath
    python main.py --api_id ************ --api_hash ************
    ```

    При первом запуске сессии потребуется авторизация пользователя.

### Автоматический запуск в windows

В планировщике задач создать задачу, каждый день запускающую `main.py`. В результате изображение профиля будет меняться каждый день.
