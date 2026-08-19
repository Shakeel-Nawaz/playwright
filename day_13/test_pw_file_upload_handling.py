from playwright.sync_api import Page, expect

"""
- Set Input Files

    .set_input_files()      ->      Accepts File Path  (or)  List of File Paths    available for upload
                                    It can only be used over locator,   i.e.    <Locator>.set_input_files("abc/abc.txt")
                            ->      For Multi File Uploads =>   <locator>.set_input_files(['abc/abc.txt','def/def.txt'])

"""


def test_single_file_upload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.focus("input#singleFileInput")
    page.wait_for_timeout(1000)
    page.locator("input#singleFileInput").set_input_files("uploads/sample.txt")
    page.wait_for_timeout(3000)

    page.get_by_role('button',name="Upload Single File").click()

    expect(page.locator("p#singleFileStatus")).to_contain_text("sample.txt")
    page.wait_for_timeout(3000)


def test_multi_file_upload(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.focus("input#multipleFilesInput")
    page.wait_for_timeout(1000)

    page.locator("input#multipleFilesInput").set_input_files(files=['uploads/sample.txt','uploads/sample_2.txt'])
    page.wait_for_timeout(3000)

    page.get_by_role('button',name="Upload Multiple Files").click()

    expect(page.locator('p#multipleFilesStatus')).to_contain_text('sample_2.txt')
    expect(page.locator('p#multipleFilesStatus')).to_contain_text('sample.txt')
    page.wait_for_timeout(3000)