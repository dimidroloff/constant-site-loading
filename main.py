from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Настройки браузера (скрытый режим)
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")  # Без открытия окна
options.add_argument("--disable-gpu")  # Отключение GPU (ускоряет работу)
options.add_argument("--no-sandbox")  # Безопасный режим (для серверов)
options.add_argument("--disable-blink-features=AutomationControlled")  # Убирает детектирование Selenium
options.add_argument("--window-size=1920,1080")  # Эмуляция обычного экрана

# Запуск браузера
driver = webdriver.Chrome(options=options)

# Открываем сайт
url = "https://pruffme.com/webinar/?id="  # Замени на нужную ссылку
driver.get(url)

# Делаем страницу "активной"
driver.execute_script("document.hasFocus = function() { return true; }")

print("Бот запущен в скрытом режиме. Напишите сообщение и нажмите Enter.")

try:
    while True:
        message = input("Введите сообщение для чата: ")  # Ждет команды
        if message.lower() == "exit":
            break  # Выход

        # Найти поле ввода
        chat_input = driver.find_element(By.CSS_SELECTOR, "div.im-messages-input-text[contenteditable='true']")
        chat_input.click()  # Активируем поле
        chat_input.send_keys(message)  # Вводим текст
        chat_input.send_keys(Keys.RETURN)  # Отправляем

        print(f"Отправлено: {message}")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()  # Закрытие браузера
    print("Бот завершил работу.")