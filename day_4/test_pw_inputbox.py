from playwright.sync_api import Page, expect


def test_inputbox(page:Page):
    page.goto('https://testautomationpractice.blogspot.com')
    inputBox = page.locator('input#name')

    expect(inputBox).to_be_visible()            # Check for the Visibility
    expect(inputBox).to_be_enabled()            # Check for the Enability

    placeholderValue = inputBox.get_attribute('placeholder')        # Get Value of an Attributeplaceholder
    print(f'Place Holder Value : {placeholderValue}')

    expect(inputBox).to_have_attribute('maxlength','15')            # Check/Validate the Attribute, by giving Value

    inputBox.fill("Shakeel Nawaz")          # Filling the text into textbox

    ValueOfInput = inputBox.input_value()           # Returns the value of input/text box. Helpful to check the pre-filled values
    print(f"Value of Input : {ValueOfInput}")

    page.wait_for_timeout(5000)