from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Запуск браузера (Chrome)
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Открыть на весь экран
driver = webdriver.Chrome(options=options)

# Переход на сайт
url = "https://pruffme.com/webinar/"  # Замени на нужную ссылку
driver.get(url)

print("Бот запущен. Напишите сообщение и нажмите Enter.")

try:
    while True:
        message = input("Введите сообщение для чата: ")  # Ждет команду
        if message.lower() == "exit":
            break  # Выход из цикла

        # Найти поле ввода чата
        chat_input = driver.find_element(By.CSS_SELECTOR, "div.im-messages-input-text[contenteditable='true']")
        chat_input.click()  # Кликнуть, чтобы активировать поле
        chat_input.send_keys(message)  # Ввести текст
        chat_input.send_keys(Keys.RETURN)  # Отправить

        print(f"Отправлено: {message}")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    driver.quit()  # Закрытие браузера
    print("Бот завершил работу.")