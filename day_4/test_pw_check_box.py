from playwright.sync_api import Page, expect

# Check Box #
'''

1. Select Specific Checkbox 
2. is_checked() Function to verify check box and Uncheck
3. Select Check Box using Labels or Other Attributes
4. Count Number of Check Boxes
5. Select All and Assert for each selected check box
6. Select Last 3 Check Boxes

Most IMP is at last : CSS or XPATH CAN BE USED TO CHECK/UNCHECK 
'''


def test_check_box(page:Page):
    page.goto('https://testautomationpractice.blogspot.com')

# 1. Select Specific Checkbox 
    check_box = page.get_by_label('Sunday')

    expect(check_box).to_be_visible()            # Check for the Visibility
    expect(check_box).to_be_enabled()            # Check for the Enability

    check_box.check()
    page.wait_for_timeout(2500)
    print()

# 2. is_checked() Function to verify check box
    if check_box.is_checked():
        print("Check Box : Sunday : is Checked")
        check_box.uncheck()
    page.wait_for_timeout(2500)

# 3. Select Check Box using Labels or Other Attributes

# 4. Count Number of Check Boxes        &          # 5. Select All and Assert for each selected check box
    
    checkBoxNames = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    checkBoxesList = []

    for name in checkBoxNames:
        checkName = page.get_by_label(name)
        checkBoxesList.append(checkName)
        checkName.check()
        expect(checkName).to_be_checked()

    print(f"Check Boxes Count : {len(checkBoxesList)}")
    page.wait_for_timeout(2500)

# 6. Select Last 3 Check Boxes

    for checkbox in checkBoxesList[-3:]:
        if checkbox.is_checked():
            checkbox.uncheck()
    page.wait_for_timeout(2500)


# Rough test by me

    for checkbox in checkBoxesList:
        if checkbox.is_checked():
            checkbox.uncheck()
        else:
            checkbox.check()
    page.wait_for_timeout(2500)


    specific_day = 'Thursday'

    for day in checkBoxNames:
        if specific_day == day:
            spc_day_check = page.get_by_label(specific_day)
            if spc_day_check.is_checked():
                spc_day_check.uncheck()
            else:
                spc_day_check.check()
    page.wait_for_timeout(2500)


# -----------------  MOST IMPORTANT ---------------- #

    checkBox2 = page.locator('input#wednesday')
    if checkBox2.is_checked():
        checkBox2.uncheck()
    else:
        checkBox2.check()

    expect(checkBox2).to_be_checked()
    page.wait_for_timeout(2500)
