#include <cstdio>
#include <algorithm>
using namespace std;

void update(int*, int*);

int main() {
  int a, b;
  int *pa = &a, *pb = &b;

  scanf("%d %d", &a, &b);
  update(pa, pb);
  printf("%d\n%d", a, b);

  return 0;
}

void update(int *a, int *b) {
  int sum = *a + *b;
  int dif = max(*a, *b) - min(*a, *b);
  *a = sum;
  *b = dif;
};
