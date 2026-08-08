from playwright.sync_api import Page, expect

# Find Chrome CPU Usage and Compare it with Value in Yellow Label

def test_dynamic_table(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    print()
    cpu_from_loc = page.locator('p#chrome-cpu').inner_text().split(': ')[1]             # Specific to WEBSITE : NOT A CONCEPT
    expected_cpu = cpu_from_loc.split('%')[0] + '%'                                     # Specific to WEBSITE : NOT A CONCEPT
    print(f"Chrome CPU: {expected_cpu}")

    print()
    table = page.locator('table[class="table table-striped"]')

    table_head_row = table.locator('thead tr th')
    header_name_index = {}
    for index, colhead in enumerate(table_head_row.all_inner_texts()):
        # print(index,colhead)
        if colhead in ['Name', 'CPU']:
            header_name_index[colhead] = index

    print(f"Header Name With Index : {header_name_index}")

    table_body_row = table.locator('tbody tr')
    for row in table_body_row.all():
        row_data = row.locator('td').all_inner_texts()
        if row_data[header_name_index['Name']] == 'Chrome':
            print(f'CPU Usage of Application Name : {row_data[header_name_index['Name']]} is {row_data[header_name_index['CPU']]}')
            assert expected_cpu == row_data[header_name_index['CPU']]
        print(row_data)


    # --------------------------------   OR (OPTIMISED BY AI) -------------------- from line 25 ---------- #
    # chrome_row = page.locator("tbody tr", has_text="Chrome")
    # cpu_value = chrome_row.locator("td").nth(header_name_index['CPU']).inner_text()
    # assert expected_cpu == cpu_value
    # print()
    # print(cpu_value)

    
    page.wait_for_timeout(5000)