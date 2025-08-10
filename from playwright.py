from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
import time

# keywords = [
#     "inc", "incorporated", "LLC", "investment", "investments",
#     "partnership", "partner", "group", "realt"
# ]

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False, args=["--disable-blink-features=AutomationControlled"])
#     context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36")
#     page = context.new_page()

#     # Navigate to the property search page
#     page.goto("https://hcad.org/property-search/real-property-advanced-records/", timeout=120000)

#     # Wait for the form iframe and target it
#     page.wait_for_selector('iframe[src*="Advanced.asp"]', timeout=60000)
#     form_frame = page.frame(name="Advanced") or page.frame_locator('iframe[src*="Advanced.asp"]')

#     # Fill and submit the form
#     form_frame.locator('input[name="StateCategory"]').wait_for()
#     form_frame.locator('input[name="StateCategory"]').fill('A1')
#     form_frame.locator('input#Search').click()

#     # Wait for new results iframe or page update
#     page.wait_for_load_state("networkidle")

#     # Check all iframes for results (skip 1x1 Cloudflare)
#     target_frame = None
#     for frame in page.frames:
#         if frame.url and "AdvancedResults" in frame.url:
#             target_frame = frame
#             break

#     # Scroll through the iframe to load all rows
#     scroll_height = 0
#     previous_height = -1
#     while scroll_height != previous_height:
#         previous_height = scroll_height
#         target_frame.evaluate("window.scrollBy(0, window.innerHeight)")
#         time.sleep(1)  # Allow rows to load
#         scroll_height = target_frame.evaluate("document.body.scrollHeight")

#     # After scrolling, grab all table data
#     content_to_parse = target_frame.content() if target_frame else page.content()
#     soup = BeautifulSoup(content_to_parse, 'html.parser')
#     rows = soup.find_all('tr')

#     all_data = []
#     for row in rows:
#         cells = [cell.get_text(strip=True) for cell in row.find_all('td')]
#         if cells:
#             all_data.append(cells)

#     if all_data:
#         df = pd.DataFrame(all_data)
#         df.to_csv("hcad_full_table.csv", index=False)
#         print(f"Scraping completed. {len(df)} rows saved to hcad_full_table.csv")
#     else:
#         print("No table data found.")

#     browser.close()


with sync_playwright() as p:
    # Launch browser with anti-bot measures
    browser = p.chromium.launch(
        headless=False,
        args=["--disable-blink-features=AutomationControlled"]
    )
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0 Safari/537.36"
    )
    page = context.new_page()

    # Go to search page
    page.goto("https://hcad.org/property-search/real-property-advanced-records/", timeout=120000)

    # Target the iframe containing the search form
    page.wait_for_selector('iframe[src*="Advanced.asp"]', timeout=60000)
    form_frame = page.frame(name="Advanced") or page.frame_locator('iframe[src*="Advanced.asp"]')

    # Fill and submit the form
    form_frame.locator('input[name="StateCategory"]').wait_for()
    form_frame.locator('input[name="StateCategory"]').fill('A1')
    form_frame.locator('input#Search').click()

    # Wait for results page to load
    page.wait_for_load_state("networkidle")

    # Identify results iframe (skip Cloudflare 1x1 iframe)
    target_frame = None
    for frame in page.frames:
        if frame.url and "AdvancedResults" in frame.url:
            target_frame = frame
            break

    # Scroll until no more new rows load
    scroll_height = 0
    previous_height = -1
    while scroll_height != previous_height:
        previous_height = scroll_height
        target_frame.evaluate("window.scrollBy(0, window.innerHeight)")
        time.sleep(1)  # allow new rows to load
        scroll_height = target_frame.evaluate("document.body.scrollHeight")

        # Debug: print scroll progress
        print(f"Scrolled to height: {scroll_height}")

    # Extract table content after scrolling
    content_to_parse = target_frame.content() if target_frame else page.content()
    soup = BeautifulSoup(content_to_parse, 'html.parser')

    # Scope only to the main table
    table = soup.find('table', {'class': 'bgcolor_1'})
    rows = table.find_all('tr') if table else []

    all_data = []
    for row in rows:
        cells = [cell.get_text(strip=True) for cell in row.find_all('td')]
        if cells:  # Skip empty rows
            all_data.append(cells)

    # Export results
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv("/Users/bobbybruno/Documents/take5.csv", index=False)
        print(f"Scraping completed. {len(df)} rows saved to take5.csv")
    else:
        print("No table data found.")

    browser.close()