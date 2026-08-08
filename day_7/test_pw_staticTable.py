from playwright.sync_api import Page, expect

# Attaching Locator to the Exisitng Locator
"""
    e.g.    para = page.locator('p[class="para1"]')      -> Existing/Current Locator
            para.locator('h4[id="para4"]')               -> Attached to previous/existing locator
            
            It Becomes ->    page.locator('p[class="para1"] h4[id="para4"]')
"""


def test_static_table(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    table = page.locator("table[name='BookTable'] > tbody")

    # 1. Count total Rows in Table

    rows = table.locator('tr')
    expect(rows).to_have_count(7)

    print()
    print(f"Total Number of Rows in Table : {rows.count()}")

    # 2. Count total Columns/Headers in Table 
    # NOTE: Number of Headers Represent Number of Columns on Each Row

    columns = rows.locator('th')
    expect(columns).to_have_count(4)

    print(f"Total Number of Columns or Header in Table : {columns.count()}")

    # 3. Read columns data from 2nd row
    # --------------------------------  Method 1  

    all_row_data = rows.all()                  # NOTE: expect methods doesnt work here, as type of variable is List. So here we have used assert
    # first_row_data = all_row_data[1].locator("td").all_inner_texts()     # Since all_row_data[0] is header, all_row_data[1] is taken

    # assert first_row_data == ['Learn Selenium', 'Amit', 'Selenium', '300']
    # print(first_row_data)       

    # --------------------------------  Method 2

    first_row_data = rows.nth(1).locator("td")
    print(first_row_data.all_inner_texts())
    expect(first_row_data).to_have_text(['Learn Selenium', 'Amit', 'Selenium', '300'])

    # 4. Read All columns data except header

    print("All Columns Data : ")
    for col in all_row_data[1:]:                            # Since all_row_data[0]     has header data and No colums Data
        print(col.locator('td').all_inner_texts())          # Even if slicing was not done, we would have got an empty list for first row as no 'td' was present

    # 5. Read or Return Data based on Condition
        # Return    Book Name     written by    Mukesh

    print()
    for col in all_row_data[1:]:
        colum = col.locator('td').all_inner_texts()
        if colum[1] == "Mukesh":
            print(f"'{colum[0]}' is the Book Written by Mukesh")


    # 6. Calculate the total price of all the Books

    print()
    total_price = 0
    for col in all_row_data[1:]:
        book_price = col.locator('td').all_inner_texts()[3]
        print(int(book_price))
        total_price += int(book_price)

    print(f"Total Price of all Books : {total_price}")