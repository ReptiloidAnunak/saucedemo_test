# **Saucedemo test APP**
[saucedemo.com](https://www.saucedemo.com/)

### **Тестируемый функционал**

1. Авторизация с помощью тестового аккаунта
2. Выбор 1 товара и добавление в корзину
3. Оформление покупки
4. Проверка успешного завершения покупки

Логи всех ошибок фиксируются в файле `errors_logs/errors_logs.json`

## Запуск

1. Запустите команду установки виртуального окружения `python3 -m venv .venv`<br>
2. Актвируйте виртуальное окружение <br>
Linux/Mac: `source .venv/bin/activate`<br>
Windows (Command Prompt): `.venv\Scripts\activate`<br>
Windows (PowerShell): `.venv\Scripts\Activate.ps1`<br>
<br><br>
3. Установите необходимые библиотеки
`pip install -r requirements.txt`<br>
4. Запустите код `python main.py`