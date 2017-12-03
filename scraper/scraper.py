import scrapy

class HealthSpider(scrapy.Spider):
    name = "healthSpider"
    start_urls = [
        'https://public.cdpehs.com/ILENVPBL/ESTABLISHMENT/ShowESTABLISHMENTTablePage.aspx?ESTTST_CTY=asgGk3ztR6c%3d'
    ]
    def parse(self, response):
        for item in response.css('td.tre > table > tbody > tr'):
            yield {
                "info": item.css('td::text').extract_first()
            }