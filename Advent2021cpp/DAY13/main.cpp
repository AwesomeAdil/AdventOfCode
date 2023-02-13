#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
#include <unordered_map>
#include <queue>
#include <iomanip>
#include <stack>
#include <set>
#include <cstring>
using namespace std;

ifstream fin("input.in");
ofstream fout("output.out");

/* BRUHHHHHHHHH this time what you do is be more confident that array wont go out,
Make sure to read in strings well and to do better next time. MAKE FUNCTIONS THE FIRST TIME*/

bool arr[1500][1500];

void foldy(int val){

for(int i=0;i<1500;i++){
    for(int j=val;j<1500;j++){
      if(arr[i][j]){
        arr[i][2*val-j] = 1;
      }
      arr[i][j] = 0;
    }
  }


}

void foldx(int val){

  
for(int j=0;j<1500;j++){
  for(int i=val;i<1500;i++){
    
      if(arr[i][j]){
        //cout<<"MOOOO";
        arr[2*val-i][j] = 1;
      }
      arr[i][j] = 0;
    }
  }


}



////////////////////////////



//unordered_map< pair<int,int>, char> mp;


int main() {
string s;
int n = 866;

for(int i=0;i<1500;i++){
  for(int j=0;j<1500;j++){
    arr[i][j] = false;
  }
}
//866

//18

for(int i=0;i<n;i++){
  getline(fin,s);
  stringstream ss(s);
  int a,b;
  int com = s.find(",");
  a = stoi(s.substr(0,com));
  b = stoi(s.substr(com+1,s.length()-com-1));
  arr[a][b] |= 1;

}

// 2

//12
string newer,trash = "uhuhuh";
getline(fin,trash);
int minx = 100000;
int miny = 100000;

while(getline(fin,newer)){



bool folderx = true;
if (newer.find("y") != std::string::npos) {
    folderx = false;
 
}

//cout<<trash;

//
 int val = stoi(newer.substr(newer.find("=")+1,newer.length()-newer.find("=")-1));
cout<<folderx<<" "<<val<<endl;
if(folderx){
  foldx(val);
 // cout<<"VALLLL"<<val;
  minx = min(minx,val);
}else{
  foldy(val);
  miny = min(miny,val);
}

}
int counter = 0;


for(int i=minx+5;i>=0;i--){
  for(int j=0;j<miny+5;j++){
    if(arr[i][j]){
      fout<<"*";
    }else{
      fout<<".";
    }
  }
  fout<<endl;
}

cout<<minx<<" "<<miny;

cout<<counter;





return 0;
}