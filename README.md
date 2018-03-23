# KOSS_TASK

This task is about making a web scraper which will scrap price about a specific product from the amazon site of whose url will be entered by the user and when it will be less than a base price given by a user ,then the user will get a mail that the given product's price is less than what he wants


##  for strating with this project 

 There is need to install "python scrapy" which can be installed by writing following command:
### 'pip instal scrapy' in the terminal

##  neccessary requirements
then to write this program ,we need a proxy free internet like mobile data since in the mailing part code, I used smtplib which needed proxy free internet.


##  for making a new project in python scrapy 
we need to type "scrapy startproject projectname" 	in the terminal
  
##  for running a program   
we need to type "sudo scrapy crawl spidername" in the terminal like
           for this program spidername is "amazon"
            "sudo" is used because sometimes it denies the permissinon or network access
  
##  for input data
  (1)   the first line it asks the user its base price and 
  (2)   the second line it asks the user Url of the product in the amazon for which price has to be extracted

##  for mailing part 
  (1)   sender's email and password can be changed from pipelines.py but only thing to be kept in mind that beofre sending the mail
    allow "less secure apps" function in your sender's email
  (2)   receiver's email can also be changed from pipelines.py 
