from playwright.sync_api import Page

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
    page.goto('https://testautomationpractice.blogspot.com/')

    def handle_dialog(dialog):
        dialog.accept()
        # dialog.dismiss()

    page.on("dialog",handle_dialog)
    page.wait_for_timeout(3000)
    page.get_by_role('button',name='Confirmation Alert').click()

    page.wait_for_timeout(10000)