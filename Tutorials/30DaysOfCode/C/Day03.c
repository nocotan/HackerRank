#include<stdio.h>
#include<stdbool.h>
int main() {
  int n;
  scanf("%d", &n);


  if (n%2!=0) {
    printf("Weird");
  } else if (2 <= n && n <= 5) {
    printf("Not Weird");
  } else if (6 <= n && n <= 20) {
    printf("Weird");
  } else {
    printf("Not Weird");
  }
  return 0;
}
