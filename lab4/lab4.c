#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>

int arr[N];
int arr2[N];
int random_int(int a, int b);
void fisher_yates(int arr[]);
int comp(const void* a, const void* b);
void print_array(int arr[], int len);
void quicksort(int arr[], int left, int right);
void insertionSort(int A[]);
void quicksort2(int arr[], int left, int right);
void hybridSort(int arr[], int left, int right);
#define arraysize(array) (sizeof(array)/sizeof(*array))
int main(){
  srand(time(NULL));
  for(int i = 0; i < N; i++) {
    arr[i] = i;
  }
  fisher_yates(arr);
  for(int i = 0; i < N; i++) {
    arr2[i] = arr[i];
  }
  //print_array(arr, N);

  /* long start = clock(); */
  /* quicksort(arr, 0, N-1); */
  /* double duration = (clock() - start + 0.0)/CLOCKS_PER_SEC; */
  /* //printf("bentley's quicksort duration: %.10f\n", duration); */
  /* printf("%.10f\t", duration); */

  /* for(int i = 0; i < N; i++) { */
  /*   arr[i] = arr2[i]; */
  /* } */

  /* start = clock(); */
  /* hybridSort(arr, 0, N-1); */
  /* duration = (clock() - start + 0.0)/CLOCKS_PER_SEC; */
  /* //printf("hybrid duration: %.10f\n", duration); */
  /* printf("%.10f\t", duration); */

  for(int i = 0; i < N; i++) {
    arr[i] = arr2[i];
  }

  /* start = clock(); */
  /* qsort(&arr, N, sizeof(int), comp); */
  /* duration = (clock() - start + 0.0)/CLOCKS_PER_SEC; */
  /* //printf("library qsort duration: %.10f\n", duration); */
  /* printf("%.10f\n", duration); */

  long start = clock();
  dualPivotQuicksort(&arr, 0, arraysize(arr), 3, 27);
  double duration = (clock() - start + 0.0)/CLOCKS_PER_SEC;
  printf("%.10f\n", duration);
  //printf("%.10f\n", duration);
  return 0;
}

int random_int(int a, int b){
    return (rand()%(b-a)+a);
}

void fisher_yates(int arr[]) {
  for(int i = 0; i < N-1; i++) {
    int j = random_int(i, N);
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  } //for
}

int comp(const void* a, const void* b){
  int one = *(const int*) a;
  int two = *(const int*) b;

  if(one < two) return -1;
  if(two < one) return 1;
  return 0;
}

void print_array(int arr[], int len){
    for(int i = 0; i < len; i++){
      printf("%d; ", arr[i]);
    }
    printf("\n");
}

//Bentley's quicksort
void quicksort(int arr[], int left, int right){
    if(left >= right) return;

    int pivot = random_int(left, right+1); //inclusive right?
    int temp = arr[left];
    arr[left] = arr[pivot];
    arr[pivot] = temp;

    int m = left;

    for(int i = left+1; i<=right; i++){
      if(arr[i] < arr[left]){
        m++;
        int temp2 = arr[m];
        arr[m] = arr[i];
        arr[i] = temp2;
      }
    }
    int temp3 = arr[left];
    arr[left] = arr[m];
    arr[m] = temp3;

    quicksort(arr, left, m-1);
    quicksort(arr, m+1, right);
}

void insertionSort(int A[]){
  for (int i = 1; i < N; i++){
    int key = A[i];
    int j = i - 1;
    while (j >= 0 && A[j] > key){
      A[j+1] = A[j];
      j--;
    }
    A[j+1] = key;
  }
}

//Hybrid's quicksort
void quicksort2(int arr[], int left, int right){
    if(right - left < 25) return;

    int pivot = random_int(left, right+1); //inclusive right?
    int temp = arr[left];
    arr[left] = arr[pivot];
    arr[pivot] = temp;

    int m = left;

    for(int i = left+1; i<=right; i++){
      if(arr[i] < arr[left]){
        m++;
        int temp2 = arr[m];
        arr[m] = arr[i];
        arr[i] = temp2;
      }
    }
    int temp3 = arr[left];
    arr[left] = arr[m];
    arr[m] = temp3;

    quicksort(arr, left, m-1);
    quicksort(arr, m+1, right);
}

void hybridSort(int arr[], int left, int right){
  quicksort2(arr, left, right);
  insertionSort(arr);
}
//dual-pivot
void swap(int *a, const int i, const int j) {
  int tmp = a[i];
  a[i] = a[j];
  a[j] = tmp;
}
void dualPivotQuicksort(int *a, const int left, const int right, int div, const int limit) {
  int length = right - left;
  //use insertion sort for small arrays length < 27
  if(length < limit) {
    for(int i = left + 1; i <= right; i++){
      for(int j = i; j > left && a[j] < a[j - 1]; j--) {
	swap(a, j, j - 1);
      } //small for
    } //big 4
    return;
  } //if
  int third = length / div;
  //middle
  int m1 = left + third;
  int m2 = right - third;
  if(m1 <= left) {
    m1 = left + 1;
  }
  if(m2 >= right) {
    m2 = right - 1;
  }
  if(a[m1] < a[m2]) {
    swap(a, m1, left);
    swap(a, m2, right);
  }
  else {
    swap(a, m1, right);
    swap(a, m2, left);
  }
  // pivots
  int pivot1 = a[left];
  int pivot2 = a[right];
  // pointers
  int less = left + 1;
  int great = right - 1;
  // sorting
  for(int k = less; k <= great; k++) {
    if(a[k] < pivot1) {
      swap(a, k, less++);
    }
    else if(a[k] > pivot2) {
      while(k < great && a[great] > pivot2){
	great--;
      }
      swap(a, k, great--);
      if(a[k] < pivot1) {
	swap(a, k, less++);
      } //if
    } //if
  } //for
  // swaps
  int dist = great - less;
  if(dist < 13) {
    div++;
  }
  swap(a, less - 1, left);
  swap(a, great + 1, right);
  // subarrays
  dualPivotQuicksort(a, left, less - 2, div, limit);
  dualPivotQuicksort(a, great + 2, right, div, limit);
  // equal elements
  if(dist > length - 13 && pivot1 != pivot2) {
    for(int k = less; k <= great; k++){
      if(a[k] == pivot1) {
	swap(a, k, less++);
      }
      else if(a[k] == pivot2) {
	swap(a, k, great--);
	if(a[k] == pivot1) {
	  swap(a, k, less++);
	}
      }
    }
  }
  // subarray
  if(pivot1 < pivot2) {
    dualPivotQuicksort(a, less, great, div,limit);
  }	
}
