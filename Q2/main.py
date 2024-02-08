from web_crawler import crawl_page
from excel_creator import create_excel_file

def main():
    """
    Main function to demonstrate the usage of web crawling and Excel file creation.
    Args:
        None
    Returns:
        None
    """
    # Example usage:
    url_to_crawl = 'https://unite.pokemon.com/en-us/'
    crawled_pages = crawl_page(url_to_crawl)
    create_excel_file(crawled_pages)


# This block ensures that the program is executed when the script is run as the main module.
if __name__ == "__main__":
    main()


# More Example Usages:
# 'https://seekingalpha.com/'
# 'https://unite.pokemon.com/en-us/'
# 'https://www.w3schools.com/python/python_intro.asp'
# 'https://www.nature.com/nbt/'
# 'https://www.mit.edu/'
