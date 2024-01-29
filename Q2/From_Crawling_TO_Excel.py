from Web_Crawl import web_crawler
from Creating_Excel_File import create_excel

# Example usage:
url_to_crawl = 'https://www.mit.edu/'
output_list = web_crawler(url_to_crawl)
create_excel(output_list)
# more Examples:
#'https://www.khanacademy.org/'
# 'https://www.youtube.com/'
# 'https://seekingalpha.com/'
# 'https://unite.pokemon.com/en-us/'
# 'https://www.w3schools.com/python/python_intro.asp'
# 'https://www.nature.com/nbt/'