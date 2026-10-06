from playwright.sync_api import sync_playwright

ROUTER = "http://192.168.3.254"   # change if yours differs
PASSWORD = "PASSWORD"
TARGET = "20/40/80/160 MHz"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(ROUTER)

    # login
    page.fill("input[type=password]", PASSWORD)
    page.keyboard.press("Enter")

    # More Functions > Wi-Fi Settings > Advanced Wi-Fi Settings
    page.get_by_text("More Functions", exact=True).click()
    page.click("#wifisettingsparent_menuId")
    page.click("#wlanadvance_menuId")

    # open the 5 GHz bandwidth dropdown (second "Bandwidth" row on the page)
    page.get_by_text("Bandwidth", exact=True).nth(1).locator(
        "xpath=following::*[contains(text(),'MHz')][1]"
    ).click()

    # the selected value and the list entry share the same text,
    # so pick the last match, which is the entry in the opened list
    page.get_by_text(TARGET, exact=True).last.click()

    save = page.get_by_text("Save", exact=True)
    save.scroll_into_view_if_needed()
    save.click()
    page.wait_for_timeout(3000)
    browser.close()
