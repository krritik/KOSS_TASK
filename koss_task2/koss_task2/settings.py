

		# 	Scrapy settings for koss_task2 project
	
BOT_NAME = 'koss_task2'

SPIDER_MODULES = ['koss_task2.spiders']		#	defining the basic class spider of which all the user deifned spiders are subclass
NEWSPIDER_MODULE = 'koss_task2.spiders'


					# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0(X11; Linux x86_64; rv:7.0.1) Gecko/20100101 Firefox/7.7'

			#	 Obey robots.txt rules
ROBOTSTXT_OBEY = True

			#	 Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = .25


ITEM_PIPELINES = {	#	defining the pipelines class
    'koss_task2.pipelines.KossTask2Pipeline': 300,
}


