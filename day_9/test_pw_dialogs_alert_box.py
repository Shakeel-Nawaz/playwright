from playwright.sync_api import Page
import pytest

"""
There are 3 Types of Dialogs

1. Simple Alert             -> Simple Dialog Box containing a single button     -> 'OK'                 ->  Used to show Information/display a simple message 
2. Confirmation Alert       -> Dialog Box contains two buttons                  -> 'OK' & 'CANCEL'      ->  Used to Explicitly Show Message and get Explict Confirmation  
3. Prompt Alert             -> Interactive type dialog with Input Box           -> 'OK' & 'CANCEL'      ->  Used to allow user to enter the text/value inputs

In Playwright we need to        Register an Event       in order to handle Alerts/Dialogs

Dialogs                         ->  A small, built-in window that a browser displays over a webpage to interact with the user.

Event                           ->  It is a pre-defined system trigger provided by Playwright.
                                        Technically, Alerts are made of Dialogs.
                                        And to interact with this alert, we need LISTERNER FUNCTIONS.
                                    e.g. for events are => "dialog", "close", "crash", "download", "popup", "load", "filechooser" etc

Listerner Function              ->  Written by Tester, It is a normal function which WAITS for EVENT TO HAPPEN and PERFORM THAT ARE WRITTEN IN FUNCTION.
                                        REGISTERING OF LISTERNER FUNCTION/CUSTOM FUNCTION is NEEDED

What & Why to Register Event    ->  Playwright is way too fast and whenever Alert or Dialog Event Triggers, IT SIMPLY IGNORED AND PROCESS FURTHER.
                                    In Order to tell Playwright to perform some action when Dialog Event/ Alerts are triggered we need Registering it.

How to Register an Event        ->  By using .on() method,      i.e  .on(<EventType>, <ListenerFunction>),       e.g.  page.on("dialog",<ListenerFunction>)
                                    NOTE:       "dialog"     is MANDATORY ARGUMENT WE NEED TO PASS to Handle Alerts, followed by Custom/Listener Function
                                    We can make use of Python's lambda functions also.

"""


def test_simple_dialog(page:Page):
    """
    Using lambda x:x.accept()
    """

    page.goto('https://testautomationpractice.blogspot.com/')

# 1. Approach 1 (NOT RECOMMENDED)

    # def handle_dialog(dialog):
    #     dialog.accept()

    # page.on("dialog",handle_dialog)
    # page.wait_for_timeout(3000)
    # page.get_by_role('button',name='Simple Alert').click()

# 2. Approach 2 (RECOMMENDED & APPLICABLE TO ALL 3 Types OF ALERTS)

    page.on('dialog',lambda x:x.accept())
    page.wait_for_timeout(3000)
    page.get_by_role('button',name='Simple Alert').click()

    page.wait_for_timeout(3000)

def test_confirmation_alert(page:Page):
    """
    Using lambda x:x.accept()       to  Accept Confirmation Alert
    Using lambda x:x.dismiss()      to  Dismiss Confirmation Alert
    """
    page.goto('https://testautomationpractice.blogspot.com/')

    page.on('dialog',lambda x:x.accept())
    # page.on('dialog',lambda x:x.dismiss())
    page.wait_for_timeout(3000)
    page.get_by_role('button',name='Confirmation Alert').click()
    page.wait_for_timeout(3000)

def test_prompt_alert(page:Page):
    """
    Using lambda x:x.accept('<InputValue>')       to  Accept Confirmation Alert
        To pass text inside prompt, we need to add text(string) inside Round Brackets 
    Using lambda x:x.dismiss()      to  Dismiss Confirmation Alert
    """
    page.goto('https://testautomationpractice.blogspot.com/')

    page.on('dialog',lambda x:x.accept('100000000'))
    # page.on('dialog',lambda x:x.dismiss())
    page.wait_for_timeout(3000)
    page.get_by_role('button',name='Prompt Alert').click()
    page.wait_for_timeout(3000)