class UnionFind():

	def __init__(self, nodes):
		self.nodes = nodes
		self.num_of_nodes = 0
		self.num_of_components = len(nodes)

		# Create Bijection and Store Node -> 0 .. num_of_nodes - 1
		self.bijection = {}
		for node in nodes:
			self.add_node(node)

		# componets[i] = j ith component parent is j
		# initially every node points to itself
		self.components_parent = [i for i in range(len(self.nodes))]

		# Initially every node points to itself thus each node create 
		# components themselves and size = 1
		self.component_size  = [1 for _ in range(len(self.nodes))]

	def add_node(self, node):
		self.bijection[node] = self.num_of_nodes
		self.num_of_nodes += 1

	# Returns the index the node root which is root of the group in which node resides
	def find(self, node):
		node_index = self.bijection[node]
		temp = node_index

		# Find the root index in temp
		while self.components_parent[temp] != temp:
			temp = self.components_parent[temp]

		root_index = temp

		# Path compresssion
		# All nodes in chain to group root node will point directly to root node
		temp = node_index
		while self.components_parent[temp] != temp:
			parent_index = self.components_parent[temp]
			self.components_parent[temp] = root_index
			temp = parent_index

		return root_index

	def connected(self, node_a, node_b):
		return self.find(node_a) == self.find(node_b)

	def component_size(self, node):
		self.component_size[self.find(node)]

	def __len__(self):
		return self.num_of_components

	def union(self, node_a, node_b):
		root_a = self.find(node_a)
		root_b = self.find(node_b)

		if root_a == root_b:
			return 

		if self.component_size[root_a] > self.component_size[root_b]:
			self.component_size[root_a] += self.component_size[root_b]
			self.components_parent[root_b] = root_a
		else:
			self.component_size[root_b] += self.component_size[root_a]
			self.components_parent[root_a] = root_b

		self.num_of_components -= 1

def main():
	uf = UnionFind(['1','2','3','4','5','6'])

	uf.union('2','3')
	uf.union('3','6')
	uf.union('4','5')
	uf.union('6','5')
	print(uf.connected('2', '5'))
	print(uf.find('5'))



if __name__ == '__main__':
	main()




