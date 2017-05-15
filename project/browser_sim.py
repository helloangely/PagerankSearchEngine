import retrieve, pagerank, ast, sys

def results_giver(terms):
    # Returns tfidf with url
    retrieved = retrieve.Retriever(terms)
    retrieved_dict = retrieved.tf_idf_dict
    output_list = []
    with open("docs.dat", "r") as docs:
        docs_dat = ast.literal_eval(docs.read())
    page_graph = {}

    # Returns pagegraph with url and links
    try:
        page_graph = {i:docs_dat[retrieved_dict[i][1]] for i in retrieved_dict}
    except:
        pass

    # Returns pagerank with url
    try:
        page_ranks = pagerank.pagerank(page_graph)
    except:
        pass

    # Returns top 50 results [[score, url, title], ...]
    try:
        for page in retrieved_dict:
            output_list.append([((retrieved_dict[page][0]*page_ranks[page])*10000), page, retrieved_dict[page][2]])
        output_list = sorted(output_list, reverse=True)[:50]
        return output_list
    except:
        pass
