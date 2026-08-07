from playwright.sync_api import Page

# Different Kinds of Dropdown
"""
1) Select dropdown          - having 'select' tag               -> options are embedded in 'option' tags

2) Bootstrap dropdown       - having 'div' / 'button' tags      -> options are embedded inside the 'div' tags

3) Hidden dropdown          - options are hidden from the DOM"""

# Handling non <select> tag dropdowns
"""
Here   .select_option()  doesnt work, as dropdowns will be of different tags like input,button etc
Though we can capture Dropdown Element i.e. input/button etc. We might not be able to capture Options locations SOMETIMES/When Hidden
To capture that(options), we have different method called FREEZING SCREEN, by using/calling "setTimeout(() => { debugger; }, 4000);" code inside console
"""
# How to capture options/elements that are Hidden or Hide During Capturing Options/Elements
"""
Open Console
type =>     setTimeout(() => { debugger; }, 4000);
Hit Enter and Click on Dynamic/Options-Hidden Dropdown 
Wait for 4 seconds
Screen will freeze allowing us to capture/inspect Hidden Options/Elements
"""

def test_bootstrap_dpdw(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.get_by_placeholder('Username').fill('Admin')
    page.get_by_placeholder('Password').fill('admin123')

    page.get_by_role('button',name=' Login ').click()

    page.get_by_role('link',name='PIM').click()

    page.wait_for_timeout(1500)

#-------------------------------------------------- METHOD 1

    # page.locator('div.oxd-input-group > div:has-text("Job Title") + div').click()

    # # page.locator('form i').nth(2).click()

    # # page.locator("div[class='oxd-input-group oxd-input-field-bottom-space'] > div:has-text('Employment Status') + div").click()
    # # page.wait_for_timeout(1500)

    # # page.locator("div[class='oxd-input-group oxd-input-field-bottom-space'] > div:has-text('Include') + div").click()


    # page.wait_for_timeout(1500)
    # page.locator('div[role="listbox"] > div:has-text("Database Administrator")').click()

    # page.wait_for_timeout(1500)
    # page.locator('div.oxd-input-group >div:has-text("Job Title") + div').click()

    # page.wait_for_timeout(1500)
    # page.locator('div[role="listbox"] > div:has-text("VP - Sales & Marketing")').click()

    # page.wait_for_timeout(3500)

#----------------------------------- METHOD 2

    page.locator('form i').nth(0).click()

    page.wait_for_timeout(3000)

    options = page.locator('div[role="listbox"] span')
    option_names = options.all_text_contents()
    # print(option_names)

    for index,option in enumerate(option_names):
        if option == 'Full-Time Contract':
            # print((option,index))
            options.nth(index).click()
            break

    print(page.locator('form i').nth(0).text_content())
    page.wait_for_timeout(3500)
