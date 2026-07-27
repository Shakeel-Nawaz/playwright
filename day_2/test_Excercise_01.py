from playwright.sync_api import Page, expect
import time

URL = 'https://opensource-demo.orangehrmlive.com/'
USERNAME = 'Admin'
PASSWORD = 'admin123'
TITLE_OF_PAGE = 'OrangeHRM'
EXP_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
DASHBOARD_URL = 'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'

def test_LandingPage(page:Page):
    page.goto(url=URL)
    expect(page).to_have_title(TITLE_OF_PAGE)
    expect(page).to_have_url(EXP_URL)
    expect(page.get_by_role('heading',name='Login')).to_be_visible()

def test_LoginProcess(page:Page):
    page.goto(url=URL)
    page.get_by_placeholder('Username').fill(USERNAME)
    page.get_by_placeholder('Password').fill(PASSWORD)

    page.get_by_role('button',name=' Login ').click()

    expect(page).to_have_url(DASHBOARD_URL)
    expect(page.get_by_role('heading',level=6,name='Dashboard')).to_be_visible()