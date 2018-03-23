
import smtplib			# library used for mailing


server = smtplib.SMTP("smtp.gmail.com",587,timeout=120)			#	assigning the host and port for sending the mails
server.starttls()							#	this is used for protecting the password for unauthorised usages.	
server.login("dreamer.nikku@gmail.com","ndee vqmt plao oqtj")		#	giving the email and password from which email is sent


class KossTask2Pipeline(object):				
	def open_spider(self, spider):				#	this function is called when the spider starts crawling
		self.file =open('items.txt', 'w')		#	this code is used to open a file which is used to keep a eye on working of code and gets updated  with every scraping

	def close_spider(self, spider):				#	this function is called when the spider stops extracting the data from the webpage.
		self.file.close()
		
	def process_item(self, item, spider):			#	this is called for every object item
		line = item['product_sale_price']		#	here the price extracted is assigned to a variable

		# basically there is a problem if the price is more than 1000 rupees,them it contains commas which has to be removed
			#	like eg.: price for a product extracted is "123,200"	,this comma has to be reomved

		line2=""			#	defining a string for string the price without commas 

		x=line.split(',')	#spliting the string into lists between commas and removing commas

		for i in range(len(x)):
			line2= line2+ str(x[i])	#then again adiding the lists to sring to get the extraced price
	
		if float(line2)<float(item['my_price']):		#comparing the prices 

			self.file.write("oh yes Price is less than what I required")	#	if it less than the price ,it sends the mail and update the textfile"items.txt"
			
			msg ="Oh Yeah Price went down.    The price of stuff is" +line2
			server.sendmail("dreamer.nikku@gmail.com","ritikburnwal@gmail.com",msg)	#information about sebdibg the mail ( sender-email , reciever-email, message to be sent) 
			server.quit()		
		else:
			self.file.write("Price is greater than what I want")		#updating the text_file"items.txt"
		return item

