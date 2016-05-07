#include<stdio.h>
#include<string.h>
int main() {
  int i = 4;
  double d = 4.0;
  char s[] = "HackerRank ";

  int is;
  double ds;
  char ss[105];

  scanf("%d", &is);
  scanf("%lf", &ds);
  scanf(" %[^\r\n]", ss);

  i = i + is;
  d = d + ds;

  printf("%d\n", i);
  printf("%.1lf\n", d);
  printf("%s%s", s, ss);
  printf("\n");
}
