#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
using namespace std;

ifstream fin("input.in");

int powe(int n,int p){
  int val = 1;
  for(int i=0;i<p;i++){
    val*=n;
  }
  return val;
}
int bint(string s)
{
    int spot = 11;
    int val = 0;
    while(spot>=0){
      if(s[s.length()-spot-1]=='1'){
       val = val+powe(2,spot);
      }

      spot--;
    } 
    return val;
}

int main() {
string s;
string most;
string least;
int len;
vector<string> list;
while(fin>>s){
  list.push_back(s);
}
len = list[1].length();
sort(list.begin(),list.end());
for(string u: list){
  cout<<u<<endl;
}
int start = 0;
int end = 999;


for(int j=0;j<len;j++){
    int mid;
    bool pass = false;
    int oner = 0;
    int zeror = 0;
    bool seen = false;
  for(int i=start;i<=end;i++){
    if(list[i][j]=='1'){
     oner++;
    if(!seen){
      mid = i;
      seen = true;
    }
    }else{
      zeror++;
    } 
  
  }
  if(start==end){
      most = list[mid];
    }
    if(end-start==1){
      most = list[end];
    }
  else if(oner>=zeror){
      start = mid;
    }else{
      end = mid-1;
    }
    if(start==end){
      most = list[mid];
    }
  
     
  
}

if(end<start){
  most = list[end];
}
cout<<start<<" "<<end<<endl;

start = 0;
end = 999;
for(int j=0;j<len;j++){
 int mid;
 bool pass = false;
 int oner = 0;
 int zeror = 0;
 bool seen = false;
  for(int i=start;i<=end;i++){
    if(list[i][j]=='1'){
     oner++;
    if(!seen){
      mid = i;
      seen = true;
    }
    }else{
      zeror++;
    } 
  
  }

    if(start==end){
      least = list[mid];
    }
    if(start-end==1){
      least = list[start];
    }
    


 
    else if(oner>=zeror){
      end = mid-1;
    }else{
      start = mid;
    }

  
  
}
if(end<start){
      least = list[end];
}
cout<<start<<" "<<end<<endl;

// cout<<most<<endl;
// cout<<least<<endl;
cout<<bint(most)*bint(least);

return 0;
} 