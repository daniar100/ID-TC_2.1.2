#Проверка
# «Создание заказа на доставку с оплатой
# через Kaspi для неавторизированного пользователя с выбором ранее добавленного адреса»

from playwright.sync_api import sync_playwright
import allure
import os
import json
import time

@allure.step("test_begin_kid")
def test_begin():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page1 = context.new_page()
        page1.goto("https://dev.daribar.kz/")
        page1.locator("input").click()
        page1.wait_for_timeout(2000)
        page1.locator("input").fill("Фен")
        page1.wait_for_timeout(2000)
        page1.get_by_text("Нью капли 20 мл").click()
        local_storage = page1.evaluate('''() => {
                        let data = {};
                        for (let i = 0; i < localStorage.length; i++) {
                            let key = localStorage.key(i);
                            data[key] = localStorage.getItem(key);
                        }
                        return data;
                    }''')
        with open("storage_load.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()
time.sleep(2)
@allure.step("fen")
def test_fen():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page2 = context.new_page()
        page2.goto(
            "https://dev.daribar.kz/products/aspirin-s-400mg-240mg-10-shipuchie--ba5e98ee-12e0-4dac-9730-d15f67d51942")
        with open("storage_load.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page2.evaluate('''(data) => {
                    for (const key in data) {
                        localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        sel = page2.locator(".mobile_cartPrice__2iIyF").first
        sel.click()
        local_storage = page2.evaluate('''() => {
                                let data = {};
                                for (let i = 0; i < localStorage.length; i++) {
                                    let key = localStorage.key(i);
                                    data[key] = localStorage.getItem(key);
                                }
                                return data;
                            }''')
        with open("storage_load2.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
time.sleep(2)
@allure.step("h_korzina")
def test_mou_korzina():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page3 = context.new_page()
        page3.goto(
            "https://dev.daribar.kz/products/aspirin-s-400mg-240mg-10-shipuchie--ba5e98ee-12e0-4dac-9730-d15f67d51942")
        with open("storage_load2.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page3.evaluate('''(data) => {
               for (const key in data) {
                   localStorage.setItem(key, data[key]);
               }
           }''', local_storage_data)
        page3.reload()
        page3.locator(".mobile_myCart__IJxPF").click()
        local_storage = page3.evaluate('''() => {
            let data = {};
            for (let i = 0; i < localStorage.length; i++) {
            let key = localStorage.key(i);
            data[key] = localStorage.getItem(key);
        }
            return data;
        }''')
        with open("storage_load3.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
time.sleep(2)
@allure.step("naiti_apteka")
def test_naiti_apteka():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/cart")
        with open("storage_load3.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
            for (const key in data) {
                localStorage.setItem(key, data[key]);
            }
        }''', local_storage_data)
        page.reload()
        sel = page.get_by_text("Найти в аптеках")
        if sel:
            sel.click()
        else:
            print("ERROR: test_naiti_apteka")

        local_storage = page.evaluate('''() => {
                                        let data = {};
                                        for (let i = 0; i < localStorage.length; i++) {
                                            let key = localStorage.key(i);
                                            data[key] = localStorage.getItem(key);
                                        }
                                        return data;
                                    }''')
        with open("storage_load4.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)
time.sleep(2)
@allure.step("ofo_form")
def test_ofo_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/pharmacies")
        with open("storage_load4.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        sel = page.get_by_role("button", name="Перейти к оформлению 1780₸").first
        sel.click()
        local_storage = page.evaluate('''() => {
                                                let data = {};
                                                for (let i = 0; i < localStorage.length; i++) {
                                                    let key = localStorage.key(i);
                                                    data[key] = localStorage.getItem(key);
                                                }
                                                return data;
                                            }''')
        with open("storage_load5.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)
time.sleep(2)
@allure.step("dostahka")
def test_dos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/checkout")
        with open("storage_load5.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        sel = page.get_by_role("button", name="Доставка")
        if sel:
            sel.click()
        else:
            print("ERROR:test_dos")
        local_storage = page.evaluate('''() => {
                                                        let data = {};
                                                        for (let i = 0; i < localStorage.length; i++) {
                                                            let key = localStorage.key(i);
                                                            data[key] = localStorage.getItem(key);
                                                        }
                                                        return data;
                                                    }''')
        with open("storage_load6.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)
time.sleep(2)
@allure.step("number_phone")
def test_number_phone():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/checkout")
        with open("storage_load6.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)
        page.evaluate('''(data) => {
                for (const key in data) {
                    localStorage.setItem(key, data[key]);
                    }
                }''', local_storage_data)
        page.reload()
        sel = page.get_by_role("button", name="Доставка")
        if sel:
            sel.click()
        else:
            print("ERROR:test_dos")
        full_xpath = "/html/body/div/div[2]/div/div/div[2]/div[2]/form/div[1]/input"
        page.wait_for_selector(f'xpath={full_xpath}')
        input_element = page.locator(f'xpath={full_xpath}')
        input_element.clear()
        input_element.type("77075999527")
        local_storage = page.evaluate('''() => {
            let data = {};
                 for (let i = 0; i < localStorage.length; i++) {
                      let key = localStorage.key(i);
                      data[key] = localStorage.getItem(key);
                                                               }
                return data;
            }''')
        with open("storage_load7.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)
time.sleep(2)
@allure.step("get_cod")
def test_click_get_cod():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page = context.new_page()
        page.goto("https://dev.daribar.kz/checkout")
        with open("storage_load7.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)
        page.evaluate('''(data) => {
                        for (const key in data) {
                            localStorage.setItem(key, data[key]);
                            }
                        }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(3000)
        sel = page.get_by_role("button", name="Доставка")
        if sel:
            sel.click()
        else:
            print("ERROR:test_dos")
        full_xpath = "/html/body/div/div[2]/div/div/div[2]/div[2]/form/div[1]/input"
        page.wait_for_selector(f'xpath={full_xpath}')
        input_element = page.locator(f'xpath={full_xpath}')
        input_element.clear()
        input_element.type("77075999527")
        sel = page.locator(".AuthorizationModal_submitButton__MIgUD")
        sel.click()
        page.wait_for_timeout(5000)
        arr = ["1","2","8","9"]

        d1 = page.query_selector('[data-id="0"]')
        d1.click()
        d1.fill(arr[0])
        d2 = page.query_selector('[data-id="1"]')
        d2.click()
        d2.fill(arr[1])
        d3 = page.query_selector('[data-id="2"]')
        d3.click()
        d3.fill(arr[2])
        d4 = page.query_selector('[data-id="3"]')
        d4.click()
        d4.fill(arr[3])
        page.wait_for_timeout(2000)
        page.get_by_text("Подтвердить").click()
        local_storage = page.evaluate('''() => {
                    let data = {};
                         for (let i = 0; i < localStorage.length; i++) {
                              let key = localStorage.key(i);
                              data[key] = localStorage.getItem(key);
                                                                       }
                        return data;
                    }''')
        sel=page.get_by_text("Алматы улица Гоголя,20").first
        sel.click()
        page.wait_for_timeout(3000)
        sel=page.get_by_text("Оформить заказ").first
        sel.click()
        with open("storage_load8.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        page.wait_for_timeout(2000)
