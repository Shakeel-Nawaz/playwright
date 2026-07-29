from playwright.sync_api import Page, expect

# XPATH Locators
# contains(<attribute>,<value>) , text()=<value> , last() , position() functions
# e.g.      a[contains(@href,'/home')]     or    a[contains(text(),'Home')]             Use     COMMA
# e.g.      a[text()='Home']                                                            Use     EQUALS
# e.g.      /ul/li[last()]
# e.g.      /ul/li[position()=3] 

# text_content() , all_text_contents()          <- Playwright
# NOTE: text_content()          returns         <- text in string type
#       all_text_contents()     returns         <- list of strings      

# count() , .first , .last , .nth()             <- Playwright


def test_XPath_locators(page:Page):
    page.goto('https://demowebshop.tricentis.com/')
    # page.goto('https://testpages.eviltester.com/pages/basics/basic-web-page/')
    page.locator("//ul[@class='top-menu']//a[@href='/books']").click()
    expect(page.locator("//div[@class='page-title']/h1")).to_have_text('Books')

    page.locator('//html/body/div[4]/div[1]/div[1]/div[1]/a/img').click()

    li_count = page.locator('//ul[@class="poll-options"]/li').count()
    print(f'li_count : {li_count}')

    expect(page.locator('//ul[@class="poll-options"]/li')).to_have_count(4)

    product_name = page.locator('//div[@class="item-box"]//h2[@class="product-title"]/a')

    print(f"First Product Name : {product_name.first.text_content()}")
    print(f"Last Product Name : {product_name.last.text_content()}")
    print(f"nth Product Name : {product_name.nth(2).text_content()}")

    options_title = page.locator('//ul[@class="poll-options"]/li/label').all_text_contents()
    for i in options_title:
        print(i)
    expect(page.locator('//ul[@class="poll-options"]/li[2]/label')).to_have_text(options_title[1])


    expect(page.locator("//li/a[contains(@href,'/awesome')]")).to_be_enabled()
    page.locator("//li/a[@href]")


    expect(page.locator("//li/a[starts-with(@href,'/comp')]").first).to_be_visible()

    print("Last Option in My Account Menu : ", page.locator("//div[@class='column my-account']/ul/li[last()]").text_content())
    print("Second Option in My Account Menu : ", page.locator("//div[@class='column my-account']/ul/li[position()=1]").text_content())
    page.wait_for_timeout(5000)