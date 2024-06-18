#Codiumate Option | Test this function
   def main() -> None :
    """
    Plan n logics
    1. insert url that contains lots of product and access it
    2. get the max page of plan 1
    3. for loop, do step 1 but with iteration of pages gathered by step 2
    4. scrape individual urls first into the max page
    5. after that, redo the for loop but for individual products
    6. before scraping, check if the url/product id has been scraped before, if it has been scraped then skip
    7. if has not been scraped then do the scraping, and the results goes into list of items
    8. insert the url that just being scraped into one big list of url
    9. after it's all succeed then do save xlsx
    10. then, use the number 8 to insert new data into database by for loop
    10a. db purpose is to check validation if a product has been scraped or not easily
    """

base_url = "https://sg.iherb.com/new-products"          #STEP 1
bs4soup, status_code = curl(base_url)
soup = Soup(bs4soup, base_url)
max_p = soup.get_max_page()                             #STEP 2
for p in range(1, 3 + 1): #max_p + 1):                  #STEP 3
    target_url = f"{base_url}?p={p}"
    logging.info(f"acccesing page" {target_url}")
    print(f"accessing page {target_url}")

    bs4soup, status_code = curl(target_url)             #STEP 4
    soup = Soup(bs4soup, target_url)
    urls = soup.scrape_urls()
    product_urls.extend(urls)
count = 0
req = 0
for url in product_urls:
    if check_product_notScraped(url):
    print(f"accessing page {url}")
    logging.info(f"accessing page {target_url}")