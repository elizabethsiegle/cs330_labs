import java.util.*;

public class Vert implements Comparable<Vert>{
	private int vInd;
	private double vShortest;
	private Edge vPred;

	public Vert(int ind, int shortest) {
		vInd = ind;
		vShortest = shortest;
		vPred = null;
	}

	public int vInd() {
		return vInd;
	}

	public double shortest() {
		return vShortest;
	}

	public Edge vPred() {
		return vPred;
	}

	public void updateS(double newS) {
		vShortest = newS;
	}

	public void updateP(Edge newP) {
		vPred = newP;
	}

	public int compareTo(Vert other) {
		if (other.shortest() == vShortest){
			return 0;
		} else if (vShortest > other.shortest()){
			return 1;
		} else {
			return -1;
		} 
	}
}
