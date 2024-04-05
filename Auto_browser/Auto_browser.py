from playwright.sync_api import Playwright, sync_playwright
from twocaptcha import TwoCaptcha
import time
from config import data_sitekey_main, url_main, WHOCAPTCHA_API_KEY


def captcha_code():
    print("Solving Captcha")
    solver = TwoCaptcha(WHOCAPTCHA_API_KEY)
    print("Ожидание ответа с решением капчи...")
    response = solver.recaptcha(sitekey=data_sitekey_main, url=url_main)
    code = response['code']
    print(f"Капча решена!")
    return code

playwright = sync_playwright()
url = "ru.stripchat.global"

def main_auto_browser(playwright: Playwright, url: str, username: str, password: str) -> None:

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto(url)
    page.get_by_role("button", name="Мне больше 18 лет").click()
    page.get_by_role("link", name="Войти").click()
    page.get_by_placeholder("Никнейм или имейл").fill(username)
    page.get_by_placeholder("Пароль").fill(password)

    """Отправляем решеную капчу и входим на сайт"""
    page.evaluate(f'document.getElementById("g-recaptcha-response").innerHTML = "{captcha_code()}";')
    page.get_by_role("button", name="Войти").click()

    """В поисковой строке сайта вводится значение, которое было прописано в форме,
    когда мы нажимали кнопку "Начать" и перейти по данному значению."""
    page.get_by_placeholder("Модели, категории, страны, меню чаевых").fill(username)
    page.get_by_placeholder("Модели, категории, страны, меню чаевых").press("Enter")

    print('Готово!')
    time.sleep(30)
    # ---------------------
    context.close()
    browser.close()


def run_main(url: str, username: str, password: str):
    with sync_playwright() as playwright:
        main_auto_browser(playwright, url=url, username=username, password=password)

