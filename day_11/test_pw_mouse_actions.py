from playwright.sync_api import Page, expect

"""
- Different types of Mouse Actions

1.  MOUSE HOVER             ->      .hover()                ->      Mouse Cursor Hovers         over pointed/defined locator
2.  MOUSE CLICK             ->      .click()                ->      Mouse Cursor Click          on targeted locator
3.  MOUSE DOUBLE CLICK      ->      .dblclick()             ->      Mouse Cursor Double Click   on targeted locator  
4.  MOUSE RIGHT CLICK       ->      .click(button='right')  ->      Mouse Cursor Right Click    on target locator
                                                                    Need to provide Button Type  
                                                                    such as
                                                                            'left'  (default)
                                                                            'right'
                                                                            'middle'
NOTE: Mouse Functions can we called either      after defining locator      or      defining locator within function
5.  MOUSE DRAG TO           ->      .drag_to()              ->      Mouse Cursor Drags      from   source locator   to    target locator
                                                                    e.g.    <sourceLocator>.drag_to(<targetLocator>)
6.  MOUSE DOWN              ->      page.mouse.down()       ->      Mouse Button is Pressed     i.e. Click and Hold
                                                                    Can provide Button Type  
                                                                    such as
                                                                            'left'  (default)
                                                                            'right'
                                                                            'middle'
7.  MOUSE UP                ->      page.mouse.up()         ->      Mouse Button is Released     i.e. Held and Released 
                                                                    Can provide Button Type  
                                                                    such as
                                                                            'left'  (default)
                                                                            'right'
                                                                            'middle'
NOTE: It is Mandatory to use    '.mouse.up()'   when    '.mouse.down()'     been used before
NOTE: MOUSE DOWN & MOUSE UP     perform action      at the last locator, 
    so before using these two functions, make sure  -----  Mouse Cursor Hover  ----- function is used at locator

"""



def test_mouse_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.get_by_role("button",name="Point Me").hover()                                  # MOUSE HOVER
    # # or
    # page.hover('button[class="dropbtn"]')

    # page.get_by_role("button",name="Point Me").click()                                # MOUSE CLICK
    # or
    page.click('button[class="dropbtn"]')

    page.get_by_role('button',name="Copy Text").dblclick()                              # MOUSE DOUBLE CLICK

    page.wait_for_timeout(3000)

    source_locator = page.locator('#draggable')
    target_locator = page.locator('#droppable')
    source_locator.drag_to(target_locator)                                              # MOUSE DRAG TO ----- Approach 1 (RECOMMENDED)


    # page.locator('#draggable').drag_to(page.locator('#droppable'))                      # MOUSE DRAG TO ----- Approach 2


    # source_locator.hover()                                                              # MOUSE DRAG TO ----- Approach 3 (NOT RECOMMENDED)
    # page.mouse.down()                                                                   # MOUSE DOWN
    # page.wait_for_timeout(3000)
    # target_locator.hover()
    # page.wait_for_timeout(3000)
    # page.mouse.up()                                                                     # MOUSE UP
    

    page.wait_for_timeout(3000)


    page.goto("https://swisnl.github.io/jQuery-contextMenu/demo.html")

    page.locator('p > span',has_text='right click me').click(button='right')            # MOUSE RIGHT CLICK

    page.wait_for_timeout(3000)

