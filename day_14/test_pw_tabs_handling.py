from playwright.sync_api import Page, Playwright, expect

"""
- TABS

Tabs in Playwright are nothing but Pages.

To handle Tabs, we need to Register an Event the same way we do for 'dialog', 'download', 'popup'.

Similarly to handle tabs    we use event    'page'      used in   .on()   method from ----- * CONTEXT * -------

NOTE:   Since Pages are created after context creation, either manually(using 'playright' fixture) or automatically(using 'page' fixture)
        We need to capture/handle   the page creation event       (or)        the tab creation event    using   .on() method of Context

i.e.        context.on('page',lambda page:page.wait_for_load_state())
            page.click("<locator that created new tab>")


After Registering and Handling an event     we can perform actions      on new tab/page     using index from context.pages
i.e.        all_pages = context.pages
            parentpage = all_pages[0]
            tabpage = all_pages[1] 

"""

def test_page_tabs(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    page = context.new_page()
    page.goto("https://testautomationpractice.blogspot.com/")

    context.on('page', lambda page:page.wait_for_load_state())
    page.get_by_role('button',name='New Tab').click()

    page.wait_for_timeout(3000)

    all_pages = context.pages
    parentpage = all_pages[0]
    tabpage = all_pages[1]

    tabpage.locator("input.gsc-input").fill("Online Training")
    tabpage.locator("input.gsc-search-button").click()
    expect(tabpage).to_have_title("SDET-QA Blog: Search results for Online Training")


