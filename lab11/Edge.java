import java.util.*;

public class Edge {
    private int from, to;
    private double wt;

    public Edge(int from, int to, double wt) {
	this.from = from;
	this.to = to;
	this.wt = wt;
    }

    public int from() {

	return from;

    }

    public int to() {

	return to;

    }

    public double weight() {

	return wt;

    }

    public String toString() {

	return ""+from+"->"+to+"\t"+wt+"\n";

    }

}
