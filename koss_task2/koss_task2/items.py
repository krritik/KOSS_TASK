
import scrapy


class KossTask2Item(scrapy.Item):	#defining the class which will be called after the data is extracted by spider and will be stored in these classes and furhter used by pipelines.pys
    					# defining  the fields for your item for containg different datas.
    product_sale_price = scrapy.Field()
    my_price=scrapy.Field()
