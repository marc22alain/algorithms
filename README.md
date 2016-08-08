# README #

### What is this repository for? ###

* Keep a PYTHON library of standard data structures and algorithms
	- to support learning in CS courses
	- to provide performant functionality for future projects


## Graph visualization ##




## Implementations of CLRS data structures and algorithms ##

- Disjoint Sets


## Architecture ##

### Type Categories ###

Data structures (DisjointSet)
- manipulate objects
- count operations

Objects (Node, Edge)
- have attributes
- DO NOT have countable operations


## Development ##

Architecture
- determine architecture of extensions for graphical display
	- (this might also include how to use the GUI to create graphs for later re-use)
- consider whether and how to convert the library to a proper package or library
- consider implementing as Python 3.x

Proliferation of algorithms and data structures
- underlying data structures with complexity tracking
- proper trees are so far ignored; would help with above

Testing and benchmarking classes
- more general testing
- focus on a set of canned graphs that have different testable properties/behaviour in different contexts


## TODOs ##
- Kruskal:
	- extend Kruskal to enable plotting... or extend the graph_maker to plot the steps
	- is the disjoint set the only option for the data structure? if so, compose it in the class
- CLRS data structures for sorting, such as BST
- graph
	- graph definition structures such as adjacency list and adjacency matrix
	- extend for trees
- Floyd-Warshall
- Ford-Fulkerson
- bipartite graphs
- Prim
- interface for graph visualiztion to:
	.load pre-defined graphs
	.run algorithms


## Library issues and questions ##
- assumptions of iterable structures are not consistent... A Java IDE would not allow these errors
- do I want a general graph generator function that can
	- generate random graphs
	- generate random graphs that give expected test results
- want to create nesting node structures for sorting algorithms... sortable nodes holding data nodes ?
