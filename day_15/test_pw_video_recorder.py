from playwright.sync_api import Playwright,expect

"""
- Video Recording of Test Execution

Playwright has provided with unique feature for Recording a Test Execution.

Complete execution video is recorded and saved at given path/location.

To provide destination/path/location, we need Context of Page, which is where Video Downloading/Saving Path can be defined
i.e.        playwright.chromium.launch().new_context(
                record_video_dir="<Path>"
                    )

"""

def test_video_recording_feature(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(
        record_video_dir="videos/"
    )
    page = context.new_page()

    page.goto("https://testautomationpractice.blogspot.com/")
    page.focus("input#input1")

    page.locator("input#input1").fill("Shakeel Nawaz")
    page.wait_for_timeout(3000)

    page.locator("button#btn1").click()
    page.wait_for_timeout(3000)

    context.close()
    browser.close()