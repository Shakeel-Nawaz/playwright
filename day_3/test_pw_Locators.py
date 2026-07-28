from playwright.sync_api import Page, expect

# Locators
# CSS Path
# Selecting Specific Children / Indexing in CSS Path
# Pattern Matching
# Opertors in Path
# Immediate Sibling Locator / CSS Combinators

# LOCATORS      Methods used to find elements in webpage using different Path.
# PATH          A simple string, that points to a specific or group of elements in DOM. (Document Object Model)
# DOM           It is a structured map that is loaded from HTML and contains all the elements like a tree

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

# --------------------   Locators  ------------------- #
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

# --------------------   CSS Path   -------------------- #
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

# --------------------   Indexing in CSS Path   -------------------- #
'''
Using the Index Number we can identify or locate the exact child element.

star (*) can be used before semicolon, to search and count every single HTML tag type within that container/parent element. i.e  Explicitly forces the engine to evaluate any tag
Tag can be used before semicolon, to search and count for given tag within that container/parent element; ex. if p tag is mentioned (p:), browser search for only 'p' tags in its parent element 
                        
star(*)/tag :first-child            <- Returns the first child element within parent element

star(*)/tag :last-child             <- Returns the last child element within parent element

star(*)/tag :nth-child()            <- Returns the specific child element or returns given number child element within parent element

star(*)/tag :nth-last-child()       <- Returns the child element, traversing from last i.e  :nth-last-child(2) -> last 2nd element

star(*)/tag :first-of-type          <- Returns the all first indexed elements with in parent element and if specific tag is mentioned, return first indexed element of given tag that are avilable within parent element  i.e   "div>p:first-of-type"  returns all first indexed type 'p' tagged elements within 'div' 

star(*)/tag :last-of-type           <- Returns the all last indexed elements with in parent element and if specific tag is mentioned, return last indexed element of given tag that are avilable within parent element   i.e   "div>p:last-of-type"  returns all last indexed type 'p' tagged elements within 'div'

star(*)/tag :nth-of-type()          <- Returns all given numbered indexed elements with in parent element and if specific tag is mentioned, return given numbered indexed element of given tag that are avilable within parent element   i.e    if given number is 3, returns all 3rd indexed elements within parent element
                                        and if tag is used , then it returns all that tagged 3rd indexed element within parent

star(*)/tag :nth-last-of-type()     <- Returns all given numbered indexed elements with in parent element but in reversed manner or traversing from end/last. e.g. Consider parent element has 5 child elements and nth-last-of-type(2) is mentioned, it returns 4th element. 
                                        Specially helps in E-Commerce websites, accessing firstly loaded product elements/product elements that were present in landing page.
                                        As we click on load more button, newer products will be added at the top and ID might change... so to access last/end products we can use this.

'''

# --------------------   Pattern Matching   -------------------- #
'''
Elements can be identified with partial values/entries, using 3 methods.

^=      <- Caret Symbol     <- Starts With      e.g. p[id^=par]     or    p[class^=ma]              Finds 'p' tagged element with 'Id' Starts with 'par'

$=      <- Dollar Symbol    <- Ends With        e.g. a[href$='cs/']   or  a[id$='pagesbasics']      Finds 'a' tagged element with 'href' Ends with 'cs/' 

*=      <- Asterisk Symbol  <- Contains         e.g. a[aria-label*='ction']                         Finds 'a' tagged element with 'aria-label' containing 'ction'

'''

# --------------------   Opertors in Path   -------------------- #
'''
Specific Elements can be excluded using Negation Selector.
<tag>:not(<selector>)

i.e. Just like not operator, neglecting this show all.

e.g     button:not([type=submit])       <- Shows all 'button' elements that doesn't contain attribute 'type=submit' 

e.g     p:not(.main)                    <- Shows 'p' tagged elements that doesn't contain 'class' attribute 'main'
                                            Which means, it shows 'p[id=para2]' and 'p[id=pa1]' from above html codes

e.g     p:not([id=para2]):not(#man)     <- Shows 'p' tagged elements that doesn't contain 'id=para2' and 'class=man'
                                            which mean it just shows 'p[id=para1]' from above html codes
                                            NOTE: if,  id  or  class  or  any attribute is not mentioned, do NOT use SQUARE BRACKETS 
'''

# --------------------   CSS Combinators   -------------------- #
'''
Combinators allow you to locate elements based on their exact relationships with neighboring elements in the HTML tree

>       Child Selector                      e.g. html > body            Finds ONLY direct, immediate children of the parent, completely skips elements that are nested further down

space   Descendant Selector                 e.g. html body              No matter how deeply nested, Finds ALL matching elements anywhere INSIDE the parent container

+       Adjacent Sibling Selector           e.g. html > head+body       Finds the very next sibling element directly, provided it matches the tag. ONLY 1 LookUP

~       General Sibling Selector            e.g. html > head ~ body     Finds ALL matching sibling elements below it under the same parent, even if there are other different tags mixed in between.

'''