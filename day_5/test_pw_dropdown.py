from playwright.sync_api import Page, expect

# -------------- Types of Dropdown -------------- #
'''
1. Single Select Dropdown

- select_option by Value
- select_option by Label
- select_option by Index

2. Multiselect Dropdown

- select_option by Value
- select_option by Label
- select_option by Index

'''

def test_dropdown(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # -----------------  Single Select Dropdown ----------------- #

    page.locator('#country').select_option(value='canada')          # Defining parameter name (value=) is not Mandatory

    page.wait_for_timeout(2500)
    page.locator('#country').select_option(label='Germany')         # Defining parameter name (label=) is not Mandatory

    page.wait_for_timeout(2500)
    page.locator('#country').select_option(index=9)             # Index starts from Zero (0)  
                                                                # Defining parameter name is MANDATORY
    page.wait_for_timeout(2500)

    # --------------------- Multi Select Dropdown ------------------ #

    page.get_by_label('Sorted List:').select_option(value=['Dog','Zebra','Fox'])            # Defining parameter name (value=) is MANDATORY
    
    page.wait_for_timeout(2500)
    
    page.get_by_label('Sorted List:').select_option(label=['Cat','Deer','Dog'])             # Defining parameter name (label=) is MANDATORY

    page.wait_for_timeout(2500)

    page.locator("label+select[name='animals']").select_option(index=[2,4,6,8])             # Index starts from Zero (0)
                                                                                            # Defining parameter name is MANDATORY
    page.wait_for_timeout(2500)

    dropdown = page.locator("label+select[name='animals']>option")
    opt_list = dropdown.all_text_contents()
    backupp = opt_list.copy()
    option = [i.strip() for i in opt_list]
    print(f"Options from DOM : [{option}]")
    sorted_option = sorted(backupp)
    print(f"Sorted Option : [{[i.strip() for i in sorted_option]}]")                # For 'Sorted Dropdowns' we can assert/expect SortedDropdown equals OptionsFromDOM
    page.wait_for_timeout(2500)
