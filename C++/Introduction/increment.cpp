#include <cstdio>
using namespace std;

void increment(int *v) {
  (*v)++;
}

int main() {
  int a;
  scanf("%d", &a);
  increment(&a);
  printf("%d", a);
  return 0;
}
