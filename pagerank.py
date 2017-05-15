# pagerank file example to use for final project. acutal pagerank used is in project/pagerank.

def pagerank(graph, epsilion = 0.02, p = 0.8):
	inbounds = {}
	keep_going_flag = True
	n = len(graph)

	# initialize each of the values to a set number
	for key, value in graph.iteritems():
		inbounds[key] = 0.25

	# keep going until epsilon converges 
	while keep_going_flag:
		for k, v in inbounds.iteritems():
			inbounds[k] = (1-p)*(inbounds[k]/len(graph[k]))
			if calculate_inbounds_epsilon(inbounds,epsilion,inbounds[k]):
				print inbounds[k]*p/n
				keep_going_flag = False
				print "results converged"
				return inbounds[k]*p/n

def calculate_inbounds_epsilon(inbounds,epsilion,pr):
	# get difference of the sum of inbound values 
	# and the length of inbound values mult by pagerank
	# to determine if new pagerank is in epsilion range

	s = sum(inbounds.values())
	b = len(inbounds.values())*pr

	if (s-b)<=epsilion:
		return True
	else:
		return False


