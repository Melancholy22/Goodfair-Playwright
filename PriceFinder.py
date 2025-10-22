from playwright.sync_api import sync_playwright, TimeoutError, expect
import re

WEBSITE_URL = "https://goodfair.com/"
EMAIL = "BobBuilding@gmail.com"
PASSWORD = "BuildingCS"
SEARCH_QUERY = "Polo Ralph Lauren Polo Shirt Mens"
TARGET_VALUE = "Polo Ralph Lauren Polo Shirt Mens L Yellow Short Sleeve Classic Fit"

def login(page):
    # Navigate to Login page
    login_link = page.locator("header").get_by_role("link", name=re.compile(r"^\s*log\s*in\s*$", re.I))
    expect(login_link).to_be_visible()
    expect(login_link).to_have_count(1)
    login_link.first.click()

    # Locate all the login inputs
    form = page.locator("form[action='/account/login']")
    expect(form).to_be_visible()
    email_input = form.locator("#CustomerEmail, input[name='customer[email]']")
    password_input = form.locator("#CustomerPassword, input[name='customer[password]']")
    expect(email_input).to_be_visible()
    expect(password_input).to_be_visible()

    # Fill in the input to login 
    email_input.fill(EMAIL)
    password_input.fill(PASSWORD)

    print("Please solve the Captcha and then click Submit")
    page.wait_for_timeout(100 * 1000) # Give the user 100 seconds to fill out captcha and submit 

def search(page):
    search_btn = page.locator("header").get_by_role(
        "button",
        name=re.compile(r"^\s*search\s*$", re.I)
    )
    expect(search_btn).to_be_visible()
    expect(search_btn).to_have_count(1)
    search_btn.click()

    # Find where the shopify combobox is and input the query
    search_bar = page.get_by_role("combobox", name="Search")
    expect(search_bar).to_be_visible()
    search_bar.click()
    search_bar.fill(SEARCH_QUERY)
    search_bar.press("Enter")

    # Look for the products list find the targetted product
    rows = page.locator("main#MainContent ul.list-view-items > li.list-view-item")
    expect(rows.first).to_be_visible()

    row = rows.filter(has=page.get_by_role("link", name=re.compile(TARGET_VALUE, re.I)))
    expect(row).to_have_count(1)
    row = row.first
    expect(row).to_be_visible()
    print(f"Success product {TARGET_VALUE} was found!")

    # Look for sale price and then regular
    price = row.locator(".price__sale .price-item--sale, .price__regular .price-item--regular").first
    expect(price).to_be_visible()
    price_text = price.inner_text().strip()
    price_num  = float(re.sub(r"[^\d.]", "", price_text))

    print(f"Product costs: {price_text}")

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.set_default_timeout(10000)
    page.goto(WEBSITE_URL, wait_until="domcontentloaded")

    login(page)
    search(page)

    page.wait_for_timeout(10000)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
