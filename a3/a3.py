import re
import Queue

fname = "road-segments.txt"
content = open(fname).read()
new_content = []

content=re.split("\n",content)

visited = []
visited_cities = []
pathcities = []
graph = {}
dfs_dist = 0

for i in range(len(content)):
	row1=re.split(" +",content[i])
	row2=[row1[1], row1[0], row1[2], row1[3]]
	new_content.append(row1)
	new_content.append(row2)

def get_directions(start,end):
	# queue - BFS
	q = Queue.Queue()
	q = adding_to_q(q,start)

	while end not in visited_cities:
		visited_q(q,end)

def adding_to_q(q,item):
	len_visited_start = len(visited)
	for i in new_content:
		if i[0] == item:
			q.put(i)
			visited.append(i)
			update_v_cities()
	len_visited_end = len(visited)
	graph[item] = visited[len_visited_start:len_visited_end]
	return q

def visited_q(q,end,visited=visited): 
	''' finding out the cities where to go from the item in queue '''
	
	curr = q.get()
	if curr[1] not in visited_cities:
		adding_to_q(q,curr[1])
	if curr[1] == end:
		print("reached end")

def update_v_cities(visited_cities=visited_cities):
	for i in visited:
		if i[0] not in visited_cities:
			visited_cities.append(i[0])



def find_shortest_path_bfs(start, end, dist=0, path=[], graph=graph):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return None
	shortest = None
	for node in graph[start]:
		if node[1] not in path:
			dist = dist + int(node[2])
			newpath= find_shortest_path_bfs(node[1], end, dist, path, graph)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	return shortest


def find_paths_dfs_or_return_paths(start, end, return_paths=False, dfs_dist=dfs_dist, path=[], graph=graph):
	path = path + [start]
	if start == end:
		return path
	if not graph.has_key(start):
		return path
	paths = []
	shortest = None
	for node in graph[start]:
		if node[1] not in path:
			dfs_dist = dfs_dist + int(node[2])
			newpath= find_paths_dfs_or_return_paths(node[1], end, return_paths, dfs_dist, path, graph)
			paths.append(newpath)
			if newpath:
				if not shortest or len(newpath) < len(shortest):
					shortest = newpath
	if not return_paths:
		return shortest
	else:
		return paths

def find_paths_pq(start, end, path=[], graph=graph):
	pq = Queue.PriorityQueue()
	paths = find_paths_dfs_or_return_paths(start,end,return_paths=True)
	pq.put(paths, 0)

	shortest = pq.get()
	while not pq.empty():
		next = pq.get()
		if len(shortest) > len(next):
			shortest = next

	return shortest 

def main_bfs():
	get_directions("Bloomington,_Indiana", "Indianapolis,_Indiana")

	start = sys.argv[1]
	end = sys.argv[2]
	search = sys.argv[3]

	if search == "dfs":
		pa = find_paths_dfs_or_return_paths("Bloomington,_Indiana", "Indianapolis,_Indiana")
		road_segs = len(pa)
		print(road_segs)
		for i in pa:
			print("Go to ", i)
		print("Total segments ",road_segs)

	if search == "bfs":
		bfs = find_shortest_path_bfs("Bloomington,_Indiana", "Indianapolis,_Indiana")
		road_segs_bfs = len(bfs)

		print(road_segs)
		for i in bfs:
			print("Go to ", i)
		print("Total segments",road_segs_bfs)

	if search == "best":	
		pq = find_paths_pq("Bloomington,_Indiana", "Indianapolis,_Indiana")

		for i in pq:
			print("Go to ", i)
		print("Total segments",len(pq))




main_bfs()

