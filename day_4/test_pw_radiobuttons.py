from playwright.sync_api import Page, expect


def test_radio_button(page:Page):
    page.goto('https://testautomationpractice.blogspot.com')
    radio_button = page.locator("#male")

    expect(radio_button).to_be_visible()            # Check for the Visibility
    expect(radio_button).to_be_enabled()            # Check for the Enability

    expect(radio_button).not_to_be_checked()            # Validate for Radio Button to Not Checked

    radio_button.check()            # Select Radio Button using .check() function

    expect(radio_button).to_be_checked()            # Validate for Radio Button is now Checked

    page.wait_for_timeout(5000)