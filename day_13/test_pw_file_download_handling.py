from playwright.sync_api import Page, expect
import os

"""
- Download Files

To Download Files                       We need to Register an Event using  .on()   function
And the Event used here is              'download'
i.e.                                    page.on('download', lambda x:x.save_as("<FolderPath with File Name & Extension>"))

Registration of Event Msut be Done      Before Calling (or) Performing Click Action to Download

i.e.                                    page.on('download', lambda x:x.save_as("<FolderPath with File Name & Extension>"))
                                        page.locator("<elementToClickToDownload>").click()


Actions Inside Events:

0.  save_as()                   ->      Save the downloaded file to a specific path         ->      Requires Folder Path along with Suggested File Name and its extension
1.  url                         ->      Returns the Download URL                            ->      Returns link of the Downloading File
2.  cancel()                    ->      Cancels the downloading action                      ->      -------
3.  path()                      ->      Returns the PATH or Default PATH of Downloads       ->      Random GUID will be the file name Along with Path
4.  delete()                    ->      Deletes the Downloaded File                         ->      -------
5.  failure()                   ->      Returns download error                              ->      Returns Error message 
6.  suggested_filename          ->      Returns browser suggested File name                 ->      Returns the File Name decided by browser

"""


def test_file_downloads(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/p/download-files_25.html")

    page.get_by_label("Enter Text:").fill("Welsome //n This is Shakeel")

    page.get_by_role('button',name="Generate and Download Text File").click()

    download_link = page.locator('a#txtDownloadLink',has_text="Download Text File")
    expect(download_link).to_be_visible()

    # # ---------- SUGGESTED BY PLAYWRIGHT ---------- #
    # page.on('download',lambda download:download.save_as("downloads/sample_downloaded.txt"))
    # download_link.click()
    # page.wait_for_timeout(3000)
    # # ---------- ----------------------- ---------- #
        
    # ---------- SUGGESTED BY AI ---------- #
    with page.expect_download() as download_details:
        download_link.click()

    download_info = download_details.value
    print(f"URL of the Downloading File : {download_info.url}")
    print(f"Suggested File Name : {download_info.suggested_filename}")
    download_info.save_as("downloads/sample_downloaded.txt")
    # download_info.cancel()
    page.wait_for_timeout(3000)
    # # ---------- ----------------------- ---------- #

    # Validation for Downloaded File

    if os.path.exists("downloads/sample_downloaded.txt"): 
        print("File Exists")
    else:
        print("File Not Found")