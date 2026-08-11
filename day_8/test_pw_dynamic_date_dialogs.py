from playwright.sync_api import Page

def select_checkin_date(page,target_date,target_month,target_year):
    while True:
        checkin_month_year = page.locator('.d7bd90e008 > h3').first.inner_text()
        print(checkin_month_year)
        if checkin_month_year == f'{target_month} {target_year}':
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    page.locator('.b8fcb0c66a tbody tr td > span', has_text=target_date).first.click()

def select_checkout_date(page,target_date,target_month,target_year):
    while True:
        checkin_month_year = page.locator('.d7bd90e008 > h3').last.inner_text()
        print(checkin_month_year)
        if checkin_month_year == f'{target_month} {target_year}':
            break
        else:
            page.locator('button[aria-label="Next month"]').click()

    page.locator('.b8fcb0c66a tbody tr td > span', has_text=target_date).last.click()      


def test_dynamic_date_dialog(page:Page):

    page.goto('https://www.booking.com/')

    #------Below check and click is for Unneccessory dialog----#
    page.locator('button[aria-label="Dismiss sign-in info."]').click()
    #----------------------------------------------------------#
    
    page.get_by_test_id('date-display-field-start').click()             # Here data-testid attribute is present in element, 
                                                                        # and CSS might not work properly when this attribute is present
    
    
    select_checkin_date(page,'12','May','2027')
    select_checkin_date(page,'29','October','2027')

    page.wait_for_timeout(3000)