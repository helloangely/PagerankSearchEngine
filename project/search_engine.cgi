#!/usr/bin/python
import cgi, browser_sim


# Base of the html content
CONTENT = """
<html>
<title>Interactive Page</title>
<body>
    <h1>Simple CNN Search Engine by EMKOBY and ANPHILIP</h1>
    <form method=POST action="search_engine.cgi">
        <P><img src="search_icon.jpg" style="width:50px;height:50px;"><B>Your last query is "%s"; enter your new query</B>
        <P><input type=text name=query>
        <P><input type=submit>
    </form>
    <h2>Results</h2>
    %s
</body></html>
"""


def format_results(results):
	links_html = ""
	for i in results:
		links_html+= "<a href='" + i[1] + "'>" + i[2] + "</a><br/>"
	return links_html

def main():
    print "Content-Type: text/html\n\n"
    # parse form data
    form = cgi.FieldStorage()

    # get the query, if any, from the form
    if 'query' in form:
        query_str = cgi.escape(form['query'].value)
    else:
        query_str = '"empty query"'

    query_list = query_str.split(' ')

    # format URL strings in results into hyperlinks
    results = browser_sim.results_giver(query_list)
    if results is None or len(results) == 0:
        result_str = '<h3>Empty result: No Hit</h3>'
    else:
        result_str = format_results(results)
	
    # format your final html page
    print CONTENT % (query_str, result_str)


if __name__ == '__main__': main()
