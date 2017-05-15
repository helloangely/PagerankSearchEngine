# -*- coding: utf-8 -*-
from collections import deque
import scrapy


#===========
# Exceptions
#===========
class NumPageNotProvidedException(Exception):
    pass

class DestFolderNotProvidedException(Exception):
    pass

class UrlNotProvidedException(Exception):
    pass


#===========
# Containers
#===========
class Container(deque):
    ''' This is a class that serves as interface to the Spider '''
    def add_element(self, ele):
        ''' Add an element to the contain, always to the right '''
        return self.append(ele)

    def get_element(self):
        ''' This is an abstract method '''
        # One can also implement this using built-in module "abc",
        #   which stands for Abstract Base Class and produces a
        #   more meaningful error
        raise NotImplementedError

class Queue(Container):
    ''' Queue data structure implemented by deque '''
    def get_element(self):
        ''' Pop an element from the left '''
        return self.popleft()


#=======
# Spider
#=======
class ExampleSpider(scrapy.Spider):
    handle_httpstatus_list = [301, 401, 403, 404, 408, 429, 500, 503]
    name = "spider"

    def __init__(self, num=None, directory=None, urls=None,
            *args, **kwargs):
        ''' Cutomized constructor that takes command line arguements '''
        super(self.__class__, self).__init__(*args, **kwargs)

        # check mandatory inputs
        if num is None:
            raise NumPageNotProvidedException
        self.num_page_to_fetch = num

        if directory is None:
            raise DestFolderNotProvidedException
        self.dest_folder = directory

        if urls is None:
            raise UrlNotProvidedException
        self.start_urls = urls.split(',')

        self.container = Queue()

        # counter for filename
        self.count = 0
		
	#checks for duplicates
        self.old_urls = []

        return
    
    def parse(self, response):

        if response.status in self.handle_httpstatus_list:
            pass
        
        # build file name and add to count
        file_name = self.dest_folder + str(self.count) + '.html'
        self.count += 1
		
	# writing the html file
        with open(file_name, 'wb') as temp_html:
            temp_html.write(response.body)
		
	# writing the index columns
        with open((self.dest_folder + 'index.dat'), 'a') as temp_html:
            temp_html.write(file_name + '\t' + response.url + '\n')
		
        path_selector = response.xpath('//a/@href').extract()
        for url in path_selector:
            if response.urljoin(url) not in self.old_urls and ('http' in response.urljoin(url)):
                self.container.add_element(response.urljoin(url))
            else:
                pass
			
	# make an absolute url and parse
        if (self.count <= int(self.num_page_to_fetch)):
            try:
                current = self.container.get_element()
                while current in self.old_urls or ('facebook' in current):
                    current = self.container.get_element()
                self.old_urls.append(current)
                print current, self.count, self.num_page_to_fetch
                yield scrapy.Request(current, callback=self.parse)
            except:
                print "Out of useable links."
        else:
            pass
