#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("input.in");

int main() {
int a,b,c,d;
fin>>a>>b>>c>>d;
int amt = 0;
if(d>a){
  amt++;
}
int temp = d;
while(fin>>d){
  a = b;
  b = c;
  c = temp;
  if(d>a){
    amt++;
  }
  temp = d;
}
 cout<<amt;
} 