#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <iomanip>
using namespace std;
ifstream fin("input.in");

int arr[1005][1005];
int main() {
  int ans=0;
  int x1,y1,x2,y2;
  char trash;
  for(int i=0;i<1005;i++){
    for(int j=0;j<1005;j++){
      arr[i][j]=0;
    }
  }
  while(fin>>x1){
    fin>>trash>>y1;
    fin>>trash>>trash;
    fin>>x2>>trash>>y2;
    if(x1==x2){
      for(int i=min(y1,y2);i<=max(y1,y2);i++){
        arr[x1][i]++;
      }
    }else if(y1==y2){ 
      for(int i=min(x1,x2);i<=max(x1,x2);i++){
        arr[i][y1]++;
      }
    }else if(x1>x2&&y1>y2){
      for(int i=0;i<=x1-x2;i++){
        arr[x2+i][y2+i]++;
      }
    }else if(x1>x2&&y1<y2){
      for(int i=0;i<=x1-x2;i++){
        arr[x2+i][y2-i]++;
      }
    }else if(x1<x2&&y1>y2){
      for(int i=0;i<=x2-x1;i++){
        arr[x2-i][y2+i]++;
      }
    }else{
      for(int i=0;i<=x2-x1;i++){
        arr[x2-i][y2-i]++;
      }
    }
  }
  for(int i=0;i<1005;i++){
    for(int j=0;j<1005;j++){
      if(arr[i][j]>1){
        ans++;
      }
    }
  }
  cout<<ans;
} 