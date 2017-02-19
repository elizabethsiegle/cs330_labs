#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>

int main() {
	int i = 0;
	long n = 10000000000;
	float a, b, c, d, e, f;
	double duration, start;
	a = 0.0f;
	b = c = 1.0f;
	d = e = 2.0f;
	f = 3.0f;

	start = clock();
	while(i < n) {
		a = b * c - d / e + f;
		b = a * c - d / e + f;
		i++;
	} 
	duration = clock() - start;
	duration = duration/CLOCKS_PER_SEC;
	printf("Duration: %10f\n", duration);
	return 0;
}
