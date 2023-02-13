#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
using namespace std;
ifstream fin("input.in");

int main() {
  int n;
  char trash;
  int miner=2000; 
  int maxer=-1;
  long long minamt;
  vector<int> vect;
  int spot=-9;
  while(fin>>n){
    fin>>trash;
    vect.push_back(n);
    miner = min(miner,n);
    maxer = max(maxer,n);
  }
  minamt = 190000*vect.size();
  sort(vect.begin(),vect.end());
  long long camt = 0;
  for(int i=0;i<maxer;i++){
    camt = 0;
    for(int j=0;j<vect.size();j++){
      int sep = abs(vect[j]-i);
      if(sep%2==0){
        camt+=sep/2*(sep+1);
      }else{
        camt+=(sep+1)/2*sep;
      }
    }
    if(minamt>camt){
      minamt = camt;
      spot = i;
    }
  }


  cout<<spot<<vect.size()<< " "<<minamt;
} 