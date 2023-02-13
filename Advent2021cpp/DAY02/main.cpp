#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
using namespace std;
ifstream fin("input.in");

int main() {
string s;
long long amtf = 0;
long long amtd = 0;
long long aim = 0;
while(getline(fin,s)){
  stringstream ss(s);
  string type;
  ss>>type;
  long long amt;
  ss>>amt;
  if(type=="forward"){
    amtf += amt;
    amtd+=aim*amt;
  }else if(type=="down"){
    aim+=amt;
  }else{
    aim-=amt;
  }
}

cout<<amtd*amtf;

return 0;
} 