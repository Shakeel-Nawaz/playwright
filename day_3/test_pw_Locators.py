from playwright.sync_api import Page, expect
# FOR EXAMPLES, NAVIGATE TO BOTTOM OF THIS MODULE #

def test_locators(page:Page):
    page.goto('https://demowebshop.tricentis.com/')

    page.wait_for_timeout(5000)
    page.locator("input.newsletter-subscribe-button[type=button]").click()
    expect(page.locator("label[for=pollanswers-1]")).to_be_visible()
    page.locator("input#pollanswers-1[name=pollanswers-1]").click()
    page.locator("a[href='/register'][class=ico-register]").click()
    page.goto('https://testpages.eviltester.com/pages/basics/basic-web-page/')
    page.locator('a[aria-label="Twitter"]').click()

def test_CSSLocators(page:Page):
    # Below locator uses CSS path (Absolute & Relative)
    page.goto('https://testpages.eviltester.com/pages/basics/basic-web-page/')
    expect(page.locator('html > body > div > div > div > main > div > div > p#para1.main')).to_be_visible()

    page.locator('div button#button1').click()
    expect(page.locator('div p#click-message')).to_have_text('You clicked the button!')
    page.wait_for_timeout(5000)

# --------------------   Locator Paths  ------------------- #
'''
<html>
    <head> </head>
    <body>
        <div class="page-body">
            <div class="navigation">...< /div>
            <h1>Basic Web Page Example</h1>
            <div class="explanation">
                <p id="pa1" class="man" style >text</p>
            </div>
            <div class="centered"> == $0
                <p id="para1" class="main" style >A paragraph of text</p>
                <p id="para2" class="sub" aria-label="Toggle section navigation">Another paragraph of text</p>
                <a href="/pages/basics/" class="align-left ps-0  td-sidebar-link td-sidebar-link__section" id="m-pagesbasics"><span class="">Basics</span></a>
            </div>
            <div class="page-footer">...< /div>
        </div>
    </body>
</html>

NOTE: ABOVE HTML IS DIFFERENT FROM TESTCASES
    CODES ARE FROM 'https://testpages.eviltester.com/pages/basics/basic-web-page/'
    TESTCASES ARE FROM 'https://demowebshop.tricentis.com' and 'https://testpages.eviltester.com/pages/basics/basic-web-page/'

tag class               ex:  p.main    or    .main
tag id                  ex:  p#para1   or    #para1
tag attribute           ex:  p[aria-label="Toggle section navigation"]
tag class attribute     ex:  a[href="/pages/basics/"][id=m-pagesbasics]
'''


# --------------------   CSS Locators   -------------------- #
'''
Absolute CSS Path : 
                    Starts from ROOT Node or Tag : We need to have navigating/greater-than (>) symbol 

Considering above DOM :: to find "A paragraph of text" paragraph element

html > body > div > div > p[id=para1]
or
html > body > div > div > p[class=main]
or
html > body > div > div > p[id=para1][class=main]           <- Any number of attributes, of that element, can be used to locate, make sure its under square brackets []
or
html > body > div > div > p[id=para1][class=main]           <- NOTE: First 'div' inside 'body' have many 'div's; and some contain 'p' tag init. But we need 3rd 'div's 'p' element.
or                                                                   Here we are NOT us index method, instead we need to add attributes of that element to identify uniquely. 
html > body > div > div > p#para1                           <- # (hash) is used for ID
or
html > body > div > div > p.main                            <- . (dot) is used for Class
or
html > body > div > div > p#para1.main                      


Relative CSS Path : 
                    Starts from Relative Node or Tags : We need to have space between paths

Considering above DOM :: to find "A paragraph of text" paragraph element

div p[id=para1]
or
div p[class=main]
or
div p[id=para1][class=main]
or
div p#para1
or
div p.main
or
div p#para1.main

'''