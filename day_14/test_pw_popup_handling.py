from playwright.sync_api import Playwright, expect

"""
- POPUP

Popup is considered as Page in Playwright.

Multiple Popup Windows      ->      Considered as Tabs or Multiple Pages

To Handle Popup's       we need to use same     event handling method       and wait to complete Loading of Page/popup
i.e.    page.on('popup',lambda x:x.wait_for_load_state())


NOTE:   POPUP Windows/Pages will have same context, that are available for the page where POPUP is called.
        e.g.    page1     has     context1,
                Popup Window   is created from   Page1
                Popup Window   will have same   context1
"""


def test_popup_handling(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")

    page.on('popup', lambda popup:popup.wait_for_load_state())
    page.get_by_role('button',name="Popup Windows").click()

    page.wait_for_timeout(3000)
    # print(context.pages)
    print(f"Total Pages including Popup : {len(context.pages)}")

    for i in context.pages:
        print(f"Title of the Page : {i.title()}")
        print(f"Url of the Page : {i.url}")

    # To perform any action inside POPUP

    popup_1 = context.pages[1]              # Index 0 (zero) is of current page, so considering Index 1
    popup_2 = context.pages[2]

    popup_1.locator("a.getStarted_Sjon",has_text="Get started").click()
    # popup_1.wait_for_timeout(2000)

    popup_2.locator("button.navbar-toggler").click()
    # popup_2.wait_for_timeout(2000)

    expect(popup_1).to_have_title("Installation | Playwright")
    popup_1.locator("span.DocSearch-Button-Placeholder",has_text="Search").click()
    popup_1.focus("input.DocSearch-Input")
    popup_1.keyboard.insert_text("POPUP")
    popup_1.keyboard.press("Control+a")
    popup_1.keyboard.press("Control+c")
    popup_1.wait_for_timeout(3000)

    popup_2.locator("span.DocSearch-Button-Placeholder",has_text="Search").click()
    popup_2.focus("input.DocSearch-Input")
    popup_2.keyboard.press("Control+v")
    popup_2.wait_for_timeout(3000)


