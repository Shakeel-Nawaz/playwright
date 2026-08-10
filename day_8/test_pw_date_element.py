from playwright.sync_api import Page, expect

# DATE Element Handling
"""
Different types of Date Elements are there in market.

Simple Date, Input that accepts Date, Bootstrap Date, Dynamic Date etc

We need to handle differently for each Date Elements.
"""
"""
We can create a utility function to click or select particular/given date
"""

def select_date(page, target_date:str, target_month:str, target_year:str, is_future:bool):
    while True:
        current_month = page.locator(".ui-datepicker-month").inner_text()
        current_year = page.locator(".ui-datepicker-year").inner_text()

        if current_month==target_month and current_year==target_year:
            break
        if is_future:
            page.locator('a[data-handler="next"]').click()
        else:
            page.locator('a[data-handler="prev"]').click()

    page.locator('.ui-state-default',has_text=target_date).click()
            

def test_date_element_handling(page:Page):

    page.goto("https://testautomationpractice.blogspot.com")
    date_loc = page.locator("input#datepicker")


# 1. Simple Date element that accepts text

    # date_loc.fill('10/15/2025')
    # page.locator("input#datepicker").press('Enter')
    # page.wait_for_timeout(3000)


# 2. By calling a Utility Function

    date_loc.click()
    page.wait_for_timeout(3000)


    is_future = True
    future_date = '20'
    future_month = 'December'
    future_year = '2027'

    select_date(page, future_date, future_month, future_year, is_future)
    inserted_value = date_loc.input_value()
    print(f"Value added using Date Dialog : {inserted_value}")
    page.wait_for_timeout(3000)
