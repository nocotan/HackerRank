#include <cstdio>
#include <algorithm>
using namespace std;

int max_of_four(int, int, int, int);

int main() {
  int a, b, c, d;
  scanf("%d %d %d %d", &a, &b, &c, &d);
  int ans = max_of_four(a, b, c, d);
  printf("%d", ans);

  return 0;
}

int max_of_four(int a, int b, int c, int d) {
  int arr[] = {a, b, c, d};
  int len = sizeof(arr)/sizeof(int);
  sort(arr, arr+len);

  return arr[3];
}
