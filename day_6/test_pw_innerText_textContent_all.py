from playwright.sync_api import Page

# inner_text()        vs      text_content() 
# all_inner_texts()       vs      all_text_contents()
# all()
"""
text_content    (or)   all_text_contents            -> Captures the RAW TEXT from elements.
                                                    -> Spaces  ,  Special Character  ,  Hidden Characters  are Included & maybe Visible in captured Text
                                                    -> e.g. Expected text from element          --  "First Product" 
                                                            RAW Text captured from element      --  "\n \\s \n First Product \n \\s \n"
                                                    -> We might need    .strip()    method to remove unwanted chars , spaces

inner_text      (or)    all_inner_texts             -> Captures ONLY TEXT from elements.
                                                    -> Spaces  ,  Special Character  ,  Hidden Characters  are Excluded & are NOT Visible in captured Text
                                                    -> e.g. Text in element                     --  "\n \\s \n First Product \n \\s \n" 
                                                            Text captured from element          --  "First Product"

all                                                 -> Basically converts   'Locator Object'      into     "List of Locators"
                                                    -> A variable containing list of    Locators (or) Locator Objects Type   can be converted into      List Type containing list of Locators
                                                    -> When using   Locator Variable, we index using        .nth()
                                                        but with    List Type Locators, we index using      [0]

"""


def test_comparision_bw_funcs(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    products = page.locator("h2.product-title")

# ------------------ all_text_contents()  vs  all_inner_texts() ----------------- #
    print()
    print("All Text Content using all_text_contents()")
    print(products.all_text_contents())

    print()
    print("All Inner Text using all_inner_texts()")
    print(products.all_inner_texts())

# ------------------ text_content()  vs  inner_text() ----------------- #
    print()
    print("Text Content using text_content()")
    for product_num in range(products.count()):
        print(products.nth(product_num).text_content())

    print()
    print("Inner Text using inner_text()")
    for productNum in range(products.count()):
        print(products.nth(productNum).inner_text())

# ------------------ all() ------------------ #
    print()
    print('Type of Products Variable containing Locators Object : ',type(products))

    print()
    product_list = products.all()
    print('Type of Product Variable containing Locators List : ',type(product_list))

    for i in range(len(product_list)):
        print(product_list[i].inner_text())