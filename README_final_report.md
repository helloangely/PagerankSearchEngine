# anphilip_emkoby_final_project

Report

How to run the code locally and not on web browser: 

final results:
query_list = ["politics"]
browser_sim.results_giver(query_list)

pagerank:
x = {}
x = pagerank.pagerank(g)

indexer:
index.py from_dir index_data

retrieve:
retrieve.py words

crawler:
crawl.py start_urls num_page dest_dir
url MUST BE IN FORM OF http://... 

Link to URL:
http://cgi.soic.indiana.edu/~emkoby/project/search_engine.cgi

Code details and design decisions:
Mulitplied pagerank with tfidf because the final number would compute to a ratio. As far as code oragnization and recommendations, we consulted with the assignment directions posted on Canvas. 

Test subjects: 
Had each test subject try search engine twice on same query. 

Test subject 1: 
Anup Segu asegu@yipitdata.com 
Data Product Engineer at Yipit Data

Tried queries "Donald Trump" "Politics" "U.S."
Speed not an issue, seems fine to Segu. 
Segu searched Donald Trump and the first link was CNN politics, and second time searched was CNN money.
Segu searched Politics and the first first link was CNN politics, as he expected. 
Segu searched U.S. first link was U.S. News, but first time searched he got the CNN Video page as the first link.

Test subject 2:
Allwin Philip allwinphilip98@gmail.com
Sophomore Chemical Engineering Student at Purdue University

Philip also mentioned the search engine was slow compared to Google because he has to watch a screen load. 
Philip tested Donald Trump and got CNN Money as first result, and got CNN politics when he ran it the second time.
Philip ran query politics and got CNN Politics, as he expected by saying, "Yah, what else would I get"
Philip ran query us and got video news the first time, admitting he did not put the periods in between. The second time he got U.S. news, as he expected. 

Test subjects result:
Both test subjects tended to get similar results on the queries Donald Trump, Politics, and U.S.
As the software engineer thought the query time was as expected, the test subject without experience programming suggested that the search engine was really slow compared to the CNN website and Google and explained that he didn't enjoy staring at the screen while the results were loading. 

Enhancements:
We enhanced our webpage UI and also from our feedback went back and made our code faster. We also implemented two pagerank algorithms to see which one worked better and the one that worked better was put into our project file while the other one is one directory above.  

Sources:
We gathered material and assistance from both class lectures and materials in i427 and consulted online Python resouces to help with syntax and our search engine. 






