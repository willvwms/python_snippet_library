import csv
with open('content.csv', 'w', newline='\r\n', encoding='utf-8') as csvfile:
    # fieldnames = ["url", "scrape_date", "html_unicode_string"]
    fieldnames = list(item.keys())
    writer = csv.DictWriter(csvfile, delimiter='|', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(item_page_list)
