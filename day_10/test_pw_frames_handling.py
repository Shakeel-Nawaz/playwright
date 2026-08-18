from playwright.sync_api import Page, expect

#   Frame Handling in Playwright
#   Child Frames (or) Nested Frames (or) iframes Handling


#   M-IMP   =>      TO ACCESS LOCATORS INSIDE FRAME, WE NEED TO OPEN THAT FRAME'S URL IN NEW TAB 

# NOTE: Difference Between      FRAME       and         iFrame
#   Frame       -> Old or OBSOLATED Technology, DIVIDES entire browser window into DISTINCT SECTIONS
#               -> MAIN HTML's ---- BODY ---- is replaced with ----- frameset -----

#   iframe      -> Current or Modern Tech, DOES NOT DIVIDE browser window, but EMBEDDS into a specific spot
#               -> HTML BODY Remains and External Document/Webpage/Website can SIT anywhere on the page
#               -> Distinct to Parent Page, e.g. YouTube Video can be Embedded into Personal Website

"""
1.  Frame Handling in Playwright

Frames      ==>       A Page containing or embedded with another entire HTML page and those embedded pages are called as Frames

We cannot directly access elements present inside embedded pages/frame. 

To access those elements,    we need to navigate/ GET ACCESS into particular frame.

In Playwright   Frames can be ACCESSED using    4 METHODS   i.e.
1.      page.frames                         ->  Listing All Frames                          -->     returns list containing ALL FRAMES

2.      page.frame_locator()                ->  Using CSS, ID, CLASS (HIGHLY RECOMMENDED)   -->     Focus on to selected Frame using Locator
                                                Highly Stable & Supports Automatic Waiting
                                                NOTE: CAN BE USED TO LOCATE  ----- iframes -----

3.      page.frame(name="<frameName>")      ->  Using Name of Frame                         -->     Focus on to selected Frame containing given Name
                                                (Usage of attribute 'name=' is OPTIONAL)

4.      page.frame(url="<frameURL>")        ->  Using URL of Frame (USED CATIOUSLY)        -->     Focus on to selected Frame containing given URL
                                                Because URL might contain keys e.g. sessionKeys   
                                                or
                                                Because different Environment like Dev/QA/Stage has different urls
                                                (Usage of attribute 'url=' is RECOMMENDED)

EXAMPLE ->      
        HTML Tag    =>    <iframe id="email-sub" name="email-subscribe" src="https://example.com"></iframe>
        2 =>    page.frame_locator("iframe#email-sub")
        3 =>    page.frame(name="email-subscribe")
        4 =>    page.frame(url="https://example.com")
"""


def test_frames_handling(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    for frame in page.frames:
        print(frame)
    print(f"Total Number of Frames in a Page : {len(page.frames)}")

    # page.goto('https://practice.expandtesting.com/iframe')
    # print(page.frame(url="https://practice.expandtesting.com/iframe-email-subscribe").is_visible)         # By Using URL to search, we can have access to some functions/validations
    # page.frame_locator("#iframe-youtube")                                                                 # We might not find any function/validation funcs, when using page.frame_locator()

    target_frame = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")

    target_frame.locator('input[name="mytext3"]').fill("SHAKEEL NAWAZ")

    expect(target_frame.locator('input[name="mytext3"]')).to_have_value("SHAKEEL NAWAZ")
    page.wait_for_timeout(3000)


# ------------------------------------------------------------------------------------------------------------------------ #

"""
2.  Child Frames (or) Nested Frames (or) iframes Handling

Child Frames        -        Frames that are nested inside Parent Frame. 

To handle child frames,      we have a function called ------>  child_frames <------

NOTE:   child_frames        func can only be accessed, if FRAME IS ACCESSED USING ---> URL <---
                            i.e.    targetFrame = page.frame(url="<URL>")
                                    child_in_targetFrame = targetFrame.child_frames
"""

def test_child_frames_handling(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    tar_frame = page.frame(url="https://ui.vision/demo/webtest/frames/frame_3")

    childs_tar_frame = tar_frame.child_frames           #Returns List containing Child Frames

    childs_tar_frame[0].get_by_label("Web Testing").check()

    page.wait_for_timeout(3000)