#include <time.h>
#include <stdlib.h>
#include <stdio.h>

#define NOT_FOUND -1
#define N 50000000
int A[N];

int linearSearch(int a[], int num, int x) {
  int ans = -1;
  for(int i = 0; i < num; i++) {
    if (a[i] == x) {
      ans = i;
    }
  }
  return ans;
}

int betterLinearSearch(int a[], int num, int x) {
  for(int i = 0; i < num; i++) {
    if (a[i] == x) {
      return i;
    }
  }
  return NOT_FOUND;
}

int sentinelLinearSearch(int a[], int n, int x) {
  int last = a[n-1];
  a[n-1] = x;
  int i = 0;
  while(a[i] != x) {
    i+=1;
  }
  a[n-1] = last;
  if(i < (n-1) || a[n-1] == x) {
    return i;
  }
  else {
    return NOT_FOUND;
  }
}

int recursiveLinearSearch(int a[], int n, int i, int x) {
  if(i >= n) {
    return NOT_FOUND;
  }
  else {
    if (a[i] == x) {
      return i;
    }
    else {
      return recursiveLinearSearch(a, n, i+1, x);
    }
  }
}

int main() {

  int n2 = N; //50,000,000
  for(int i = 0; i < n2; i++) {
    A[i] = rand();
  }
  int avgCaseEle = rand() % 10 + N + 100000;
  int bestCaseEle = A[0];
  int worstCaseEle = -10;

  printf("\n Best cases: \n");

  long start = clock();
  printf("linearSearch: %d \n", linearSearch(A, n2, bestCaseEle));
  double duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %.10f\n", duration);

  start = clock();
  printf("betterLinearSearch: %d \n", betterLinearSearch(A, n2, bestCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %.10f\n", duration);

  start = clock();
  printf("sentinelLinearSearch: %d \n", sentinelLinearSearch(A, n2, bestCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %.10f\n", duration);

  start = clock();
  printf("recursiveLinearSearch: %d \n", recursiveLinearSearch(A, n2, 0, bestCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %.10f\n", duration);


  printf("\n Average cases: \n");


  start = clock();
  printf("linearSearch: %d \n", linearSearch(A, n2, avgCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("betterLinearSearch: %d \n", betterLinearSearch(A, n2, avgCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("sentinelLinearSearch: %d \n", sentinelLinearSearch(A, n2, avgCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("recursiveLinearSearch: %d \n", recursiveLinearSearch(A, n2, 0, avgCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  printf("\n Worst cases: \n");


  start = clock();
  printf("linearSearch: %d \n", linearSearch(A, n2, worstCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("betterLinearSearch: %d \n", betterLinearSearch(A, n2, worstCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("sentinelLinearSearch: %d \n", sentinelLinearSearch(A, n2, worstCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %10f\n", duration);

  start = clock();
  printf("recursiveLinearSearch: %d \n", recursiveLinearSearch(A, n2, 0, worstCaseEle));
  duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("duration: %f\n", duration);

}
