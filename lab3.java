public static void main(String[] args) {
    int i = 0;
    long n;
    float a, b, c, d, e, f;
    n = 100000000;
    a = 0.0f;
    b = c = 1.0f;
    d = e = 2.0f;
    f = 3.0f;

    long startTime = System.nanoTime();
    while(i < n) {
	a = b*c - d/e + f;
	b = a * c - d / e + f;
	i++;
    }
    long endTime = System.nanoTime();
    double duration = (endTime - startTime)/1000000;
    System.out.println("Duration: " + duration+ " milliseconds");
}
