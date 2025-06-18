from icrawler.builtin import BingImageCrawler

crawler = BingImageCrawler(storage={'root_dir': 'bike_images'})
crawler.crawl(keyword='car', max_num=20000)
