from playwright.sync_api import Page, expect

"""Below are the Playwright Built-In Locators
    1. page.get_by_text()
    2. page.get_by_role()
    3. page.get_by_alt_text()
    4. page.get_by_label()
    5. page.get_by_placeholder()
    6. page.get_by_title()
    7. page.get_by_test_id()
"""

def test_getbyText(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    text = page.get_by_text('Sign up for our newsletter:')
    expect(text).to_be_visible()

def test_getbyRole(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    expect(page.get_by_role('heading', name='Build your own expensive computer')).to_be_enabled()

def test_getbyAltText(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    expect(page.get_by_alt_text('Tricentis Demo Web Shop')).to_be_visible()

def test_getbyLabel(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    expect(page.get_by_label('Excellent')).to_be_visible()

def test_getbyPlaceHolder(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    page.get_by_placeholder('Enter your full name').fill('Shakeel Nawaz')

def test_getbyTitle(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    expect(page.get_by_title('Tooltip text')).to_have_text("This text has a tooltip")

def test_getbyTestId(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/playwrightpractice.html')
    expect(page.get_by_test_id('profile-email')).to_have_text("john.doe@example.com")