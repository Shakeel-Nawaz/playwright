from playwright.sync_api import Page, expect
import re

def test_excercise_02(page:Page):
    page.goto('https://practice-automation.com/form-fields/')

    page.locator('label[for="name-input"]').fill("Shakeel")     # Could have used label but has 2 elements, so used locator
    page.get_by_label("Password ").fill('Nawaz')

    drinks = ['Water', 'Milk', 'Coffee', 'Wine', 'Ctrl-Alt-Delight']
    for drink in drinks:
        checkbox = page.get_by_label(drink)
        if drink in ['Coffee', 'Milk']:
            checkbox.check()

    colors = ['Red','Blue','Yellow','Green','#FFC0CB']
    page.locator('input[value="Red"]').check()
    for color in colors:
        radio = page.locator(f'input[value="{color}"]')
        if color == 'Red': pass
        else:
            expect(radio).not_to_be_checked()
            print(f'{color} : Radio Button is Unchecked')

    page.wait_for_timeout(5000)