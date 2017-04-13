import java.util.*;

public class Graph {

    private int numVert;

    private int numEdges;

    private ArrayList<Edge>[] edges;

    public Graph(int v) {

	numVert = v;

	edges = (ArrayList<Edge>[]) new ArrayList[v];

	for (int i = 0; i < v; i++) {

	    edges[i] = new ArrayList<Edge>();

	}

    }

    public int V() {

	return numVert;

    }

    public int E() {

	return numEdges;

    }

    public void addEdge(Edge e) {

	int from = e.from();

	edges[from].add(e);

	numEdges++;

    }

    public ArrayList<Edge> getAdj(int v) {

	return edges[v];

    }

    public String toString() {

	StringBuilder graph = new StringBuilder();

	graph.append("edge-weighted digraph\n");

	for (int i = 0; i < numVert; i++) {

	    for (int j = 0; j < edges[i].size(); j++) {

		graph.append(edges[i].get(j).toString());

	    }

	}

	return graph.toString();

    }

}
