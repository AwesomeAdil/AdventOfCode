#include <iostream>
#include <fstream>
using namespace std;
ifstream fin("input.in");
int main() {
  int n;
  char trash;
  long long arr[9];
  for(int i=0;i<9;i++){
    arr[i]=0;
  }
  while(fin>>n){
    fin>>trash;
    arr[n]++;
  }
  for(int j=0;j<256;j++){
    long long temp = arr[0];
    arr[0]=arr[1];
    arr[1]=arr[2];
    arr[2]=arr[3];
    arr[3]=arr[4];
    arr[4]=arr[5];
    arr[5]=arr[6];
    arr[6]=arr[7]+temp;
    arr[7]=arr[8];
    arr[8]=temp;
  }
  long long sum = 0;
  for(int i=0;i<=8;i++){
    sum+=arr[i];
  }
  cout<<sum;
} 