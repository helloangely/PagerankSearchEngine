# -*- coding: utf-8 -*-
from collections import deque
import scrapy

# for this project, I used stacks and queues to hold the urls given from the scrapy runs.
# I used lifo for stacks and the dfs algorithm, and fifo for the queues and bfs algorithm
# I complied with robots and the politeness requests of the assignment through changes in
# settings.py, and I was assisted in my project by use of the starter code given by the ais

#===========
# Exceptions
#===========
class AlgoNotProvidedException(Exception):
    pass

class AlgoNotSupportedException(Exception):
    pass

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

class Stack(Container):
    ''' Stack data structure implemented by deque '''
    def get_element(self):
        ''' Pop an element from the right '''
        return self.pop()


#=======
# Spider
#=======
class ExampleSpider(scrapy.Spider):
    name = "example"
    #allowed_domains = ["example.com"]
    start_urls = (
        'http://www.example.com/',
    )

    def __init__(self, algo=None, num=None, directory=None, urls=None,
            *args, **kwargs):
        ''' Cutomized constructor that takes command line arguements '''
        super(self.__class__, self).__init__(*args, **kwargs)

        # check manditory inputs
        if num is None:
            raise NumPageNotProvidedException
        self.num_page_to_fetch = num

        if directory is None:
            raise DestFolderNotProvidedException
        self.dest_folder = directory

        if urls is None:
            raise UrlNotProvidedException
        self.start_urls = urls.split(',')

        # check algorithm choice, and construct container accordingly
	if algo is None:
            raise AlgoNotProvidedException
        elif algo == 'dfs':
            self.container = Stack()
        elif algo == 'bfs':
            self.container = Queue()
        else:
			raise AlgoNotSupportedException
		
		# counter for filename
        self.count = 0
		
		#checks for duplicates
        self.old_urls = []
        
        return


    def parse(self, response):
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
            self.container.add_element(url)
			
		# make an absolute url and parse
        if (self.count < int(self.num_page_to_fetch)):
            current = self.container.get_element()
            next = response.urljoin(current)
            while current in self.old_urls:
                current = self.container.get_element()
            next = response.urljoin(current)
            self.old_urls.append(current)
            print next, self.count, self.num_page_to_fetch
            yield scrapy.Request(next, callback=self.parse)
