from playwright.sync_api import Page, Playwright, expect
# Browser     Context     Page
"""
Browser vs Context vs Page

Browser                 ->          Browser is a instance of Physical Browser, where we can access websites/pages by sending request using URL
                                    e.g.    Chrome, Firefox, webkit

Context                 ->          BrowserContext is isolated, incognito like mode, where single browser instance can run 
                                    multiple pages without sharing their context data such as cookies, storage, cache

Page                    ->          Page is a Single Tab or a Popup window within a BrowserContext
                                    PopUp Windows    ,    Tabs     =>       are nothing but Pages


NOTE: 1 Browser         ->          can create Multiple Browser Context
      1 Browser Context ->          can create Multiple Pages
      Multiple Pages    ->          can work idependently, without using switch commands

            Browser     ---->     Context     ---->     Page

To Launch Browser       ->          Using "playwright Fixture", we can create browser instance for headless mode
                                    i.e.    def test_ABC(playwright:Playwright):                <----- Here 'playwright'     is    Fixture
                                    i.e.        browser = playwright.chromium.launch()

To Create New Context   ->          Using created Browser Instance, we can create single/multiple     ->     New Browser Context
                                    i.e.  context = browser.new_context()           (or)        context = playwright.chromium.launch().new_context()

To Create New Page      ->          Using created Context, we can create single/multiple     ->     New Pages
                                    i.e   page1 = context.new_page()    , page2 = context.new_page()
                                    (or)
                                    Using "page Fixture", we can directly create new Page, with default Browser Instance and Default Context
                                    i.e.    def test_ABC(page:Page):                <----- Here 'page'     is    Fixture
                                    i.e.        page1 = page.goto("https//:www.google.com")
"""

def test_browser_context_page(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False,)                      # Creating Browser Instance with headed mode

    context = browser.new_context()                                           # Creating New Browser Context

    page_1 = context.new_page()                                               # Creating New Page  i.e.  page1
    page_2 = context.new_page()                                               # Creating New Page  i.e.  page2

    page_1.goto("https://www.google.com")
    expect(page_1).to_have_title('Google')
    page_1.wait_for_timeout(3000)


    page_2.goto("https://testautomationpractice.blogspot.com/")
    expect(page_2).to_have_title('Automation Testing Practice')
    page_2.wait_for_timeout(3000)
    page_1.locator('textarea[aria-label="Search"]').focus()