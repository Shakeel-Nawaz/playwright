from playwright.sync_api import Page

# List all product names in a list
# List all prices in a list
# print all product names with price
# sort/filter from UI from 'low to high cost'
# print lowest and highest products name & price

def test_exercise_03(page:Page):
    page.goto("https://bstackdemo.com/")

    product_titles = page.locator("p[class$='_title']").all_text_contents()

    ele_prod_price_dollars = page.locator("div[class$='_price'] > div.val > b")
    ele_prod_price_decimal = page.locator("div[class$='_price'] > div.val > span")
    
    product_price = [float(integer+decimal) for integer,decimal in zip(ele_prod_price_dollars.all_text_contents(), ele_prod_price_decimal.all_text_contents())]

    # Below line is the code to reduce the space complexity from (O(N)) to (O(1))
    # product_price = list(float(integer+decimal) for integer,decimal in zip(ele_prod_price_dollars.all_text_contents(), ele_prod_price_decimal.all_text_contents()))
    
    # Below line using all_text_contents() directly
    # product_price = [float(integer+decimal) for integer,decimal in zip(page.locator("div[class$='_price'] > div.val > b").all_text_contents(), page.locator("div[class$='_price'] > div.val > span").all_text_contents())]

    # print("All Product with their Prices")
    all_product_list = list((name,price) for name,price in zip(product_titles,product_price))
    # print(all_product_list)

    page.locator("div.sort > select").select_option(value='lowestprice')            # Clicking on Dropdown and selecting 'Lowest to Highest' option
    page.wait_for_timeout(2500)

    filtered_product_price = [float(integer+decimal) for integer,decimal in zip(ele_prod_price_dollars.all_text_contents(), ele_prod_price_decimal.all_text_contents())]
    filtered_all_product_list = list((name,price) for name,price in zip(page.locator("p[class$='_title']").all_text_contents(),filtered_product_price))

    sorted_all_prod = sorted(all_product_list,key=lambda x:x[1])

    assert sorted_all_prod == filtered_all_product_list 

    print(f'Lowest Priced Product : {filtered_all_product_list[0]}')
    print(f'Highest Priced Product : {filtered_all_product_list[-1]}')