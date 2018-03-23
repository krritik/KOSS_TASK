import scrapy				
from koss_task2.items import KossTask2Item			#	I am calling a class "KossTask@Item" which has been defined in the file "items.py"

n=input("enter the base price for the product :")		#	asking the user for the base price for the product

class koss_task(scrapy.Spider):				#	Here I defined my spider which will extract the data from the website 
	name = "amazon"					# 	Here I defined the name of my spider which can be used for calling it in the terminal
	
	allowed_domains = ["amazon.com"]		# 	here Url is entered for which data has to be extracted and it will not extract data beyond this  site if  "Offsite middleware" is active"


	x=raw_input("enter the url : ")			#	asking the user to enter the URL of the product from the amazon site of whose price has to be extraced and compared

	
	start_urls=[]					#	this contains the urls of the web sites whose data has to be extracted and for which crawler has to start extracting data 
	start_urls.append(str(x))	
	



	def parse(self, response):			#	function which will act on the response returned by the spider and extract the specific data which I needed (in this it is price)
		items=KossTask2Item()			
		sale_price = response.xpath('//span[contains(@id,"ourprice") or contains(@id,"saleprice")]/text()').extract()

							#	here the price is extracted using xpath which uses the id of the tag which contains the price and and then extract function is used to extract it and assign it to sale_price
		items['product_sale_price'] = ''.join(sale_price).strip()	#this is done to remove the extra spaces in the first and the last of the price and just extract the price 
		items['my_price']=str(n)		# this is to pass the base price entered by the user
		yield items				#	sending the scraped data by spiders to "pipelines.py" where the other functions on scraped data will take place 


