from playwright.sync_api import Page, expect

def test_pagination(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    has_next_page = page.locator('button[aria-label="Next"]').is_enabled()

    table = page.locator('table#example')
    # while page.locator('button[aria-label="Previous"]').is_disabled():
    row_count = 0

    while has_next_page:
        rows = table.locator('tbody tr')
        row_count += rows.count()
        # for row in rows.all():
        #     print(row.all_inner_texts())

        if page.locator('button[aria-label="Next"]').is_enabled():
            page.locator('button[aria-label="Next"]').click()
        else:
            has_next_page = False
    print(f"Total Row Count : {row_count}")


def test_pagination_filters(page:Page):
    page.goto("https://datatables.net/examples/core/basic_init/zero_configuration.html")

    table = page.locator('table#example')


    filter_rows = page.locator('select.dt-input')
    print()
    print(f"Default Filter Value = {filter_rows.input_value()}")

    filter_options = [25,50]

    for filter_val in filter_options:
        filter_rows.select_option(value=str(filter_val))
        print(f"Selected Filter : {filter_val}")

        rows = table.locator('tbody tr')
        expect(rows).to_have_count(filter_val)
        print(f"For given Filter Value of {filter_val}, Total Number of Rows present in Table is {rows.count()}")
