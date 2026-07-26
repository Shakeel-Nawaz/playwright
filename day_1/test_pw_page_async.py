from playwright.async_api import Page, expect


def test_verifyTitle(page:Page):
    page.goto('https://www.google.com')
    expect(page).to_have_title('Google')