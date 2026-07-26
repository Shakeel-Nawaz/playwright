from playwright.sync_api import Page, expect

def test_verifyPageURL(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")

def test_verifyTitle(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_verifyPageURL2(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")

def test_verifyTitle2(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_verifyPageURL3(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")

def test_verifyTitle3(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")

def test_verifyPageURL4(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_url("https://www.google.com/")

def test_verifyTitle4(page:Page):
    page.goto("https://www.google.com")
    expect(page).to_have_title("Google")