from playwright.sync_api import Page, expect

# Handling Dynamic Elements
'''
To handle dynamic elements, we have multiple options
    1. .or_()   Playwright's Native OR Operator    e.g.  page.locator("<xpath or css path>").or_(page.locator("<xpath or css path>"))
    2. OR Operator with multiple attributes using Xpath
    3. contains()  in Xpath    or      *=    in CSS Path
    4. Starts-with (^=) in CSS Path     or     <tag>[starts-with( @ <attribute> , '<value>' )]   in XPATH

'''

def test_handling_dynamic_elements(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/playwrightpractice.html")

    for i in range(5):
        page.locator("//button[@class='start' or @class='stop']").click()
        page.wait_for_timeout(500)
        if page.locator("//button[@class='start' or @class='stop']").is_visible():
            print('Element Found')
        else:
            print('Not Found')

        print('ELEMENT FOUND' if page.locator("button.start").or_(page.locator("button.stop")).is_visible() else 'NOT FOUND')
        # print('ELEMENT FOUND' if page.locator("//button[@class='start']").or_(page.locator("//button[@class='stop']")).is_visible() else 'NOT FOUND')

    print()
    page.locator("//button[contains(@class,'st')]").click()
    #or 
    page.locator("button[class*='st']").click()

    page.locator("//button[starts-with(@class,'st')]").click()
    #or
    page.locator("button[class^='st']").click()