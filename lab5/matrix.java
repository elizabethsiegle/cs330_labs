public class matrix{
    public static void main (String args[]) {
	int N = Integer.parseInt(args[0]);
	int[][] A = new int[N][N];
	identity(A);
	printMatrix(A);
    }

    public static void identity(int A[][]) {
	int N = A.length;
	for(int i = 0; i < N; i++) {
	    for(int j = 0; j < N; j++) {
		if (i == j) {
		    A[i][j] = 1;
		} else {
		    A[i][j] = 0;
		}
	    }
	}
    }

    public static void printMatrix(int A[][]) {
	int N = A.length;
	for (int i = 0; i < N; i++){
	    for (int j = 0; j < N; j++) {
		System.out.print(A[i][j]+" ");
	    }
	    System.out.println();
	}
    }
}
