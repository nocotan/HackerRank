#include<stdio.h>
#include<math.h>
int main() {
  double cost;
  int tip_per;
  int tax_per;

  scanf("%lf", &cost);
  scanf("%d", &tip_per);
  scanf("%d", &tax_per);

  double tip = cost * tip_per / 100;
  double tax = cost * tax_per / 100;
  double total = round(cost + tip + tax);

  printf("The total meal cost is %.lf dollars.", total);
  return 0;
}
