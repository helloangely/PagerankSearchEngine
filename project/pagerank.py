def pagerank(graph):
        # Constants
        p = 0.2
        pn = p/len(graph)
        pp = 1.0-p
        nn = 1.0/len(graph)
        epsilon = 0.03
        before_dict = {}
        after_dict = {}
        
        # Initialize pagerank dicitonary with default score
        before_dict = {key:nn for key in graph.keys()}
        
        # Iterate to alter pagerank until within epsilon
        while True:
                for page in before_dict:
                        total = 0
                        for pagee in before_dict:
                                if page in graph[pagee]:
                                        total += (before_dict[pagee])/(len(graph[pagee]))
                        after_dict[page] = pn + (pp * total)

                epsilon_complete = True
                for page in before_dict:
                        if abs(after_dict[page]-before_dict[page]) > epsilon:
                                epsilon_complete = False
                                before_dict[page] = after_dict[page]
                if epsilon_complete:
                        return after_dict
