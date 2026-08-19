from playwright.sync_api import Page, expect

"""
- Keyboard Actions

Keyboard Actions can be achieved using "page.keyboard.<actions>"

1.  keyboard.insert_text()      ->  Unlike fill() method which clears the existing value/text before filling,
                                    insert_text()   Appends text from the last/current cursor point
2.  keyboard.type()             ->  .type() function is used to enter the value allowing delay between each entry/press
                                    e.g.    keyboard.type("CHECK",delay=500)    time is in millisec

3.  keyboard.press              ->  .press()    used to press the keys, and conbination of keys
                                    e.g.    keyboard.press("Control+F")
                                    NOTE: NO SPACE should be present before/after Plus (+) & Minus/Hypen (-)
4.  keyboard.down               ->  .down()     used when we need to press or hold pressing continuously
                                # #     e.g.    keyboard.down("Shift")
                                # #             keyboard.type("eMerGenCY")
                                #     NOTE: From example: Shift button is pressed but not released and waiting for keyup event
                                #           i.e.  keyboard.up("Shift"). Causing result to change lower case to upper.
                                #           i.e   "EmERgENcy"
5.  keyboard.up                 ->  .up()     used when we need to unpress or release pressing
                                    """
"""
- Types of Keys

1.  Function Keys               ->  F1 to F12
2.  AlphaNumeric Keys           ->  A to Z,
                                    0 to 9,
                                    comma,semicolon,quote keys,period
3.  Modifier Keys               ->  Shift, Control, Alt,
4.  Navigation Keys             ->  Arrow Keys (up, down, left, right)
                                    Enter / Return Key
                                    Backspace / Delete
                                    Page Down / Page Up
                                    Home / End key
5.  System Keys                 ->  Escape (Esc)
                                    Caps Lock / Num Lock
                                    Print Screen (PrtScn)

"""

def test_keyboard_actions(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.focus("input#input1")
    page.keyboard.insert_text('SHaKEeL')

    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    page.keyboard.type("SHaKEeL",delay=300)

    page.keyboard.press("Tab")
    page.keyboard.press("Tab")

    page.keyboard.press("S+H+a+K+e+e+L+Minus",delay=500)
    page.wait_for_timeout(3000)

    page.keyboard.down("Control")
    page.keyboard.down("A")
    page.keyboard.press("Control+X")
    page.wait_for_timeout(5000)
    page.keyboard.press("Control+V")
    page.keyboard.up("A")
    page.keyboard.up("Control")

    page.keyboard.down("Shift")
    page.wait_for_timeout(1000)
    page.keyboard.press('ArrowLeft')
    page.keyboard.press('ArrowLeft')
    page.wait_for_timeout(1000)
    page.keyboard.up("Shift")
#     page.keyboard.type("###")
    page.click('input#input3',button='right')
    
    page.wait_for_timeout(5000)