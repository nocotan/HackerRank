#include <iostream>
using namespace std;

int main() {
  int n, m;
  string num[11] = {"one", "two", "three",
    "four", "five", "six", "seven", "eight", "nine", "even", "odd"};

  cin >> n >> m;
  for(int i=n; i<=m; ++i) {
    if(i >9) {
      if(i%2==0) cout << num[9] << endl;
      else cout << num[10] << endl;
    } else {
      cout << num[i-1] << endl;
    }
  }
}
