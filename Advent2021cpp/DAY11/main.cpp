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
using namespace std;

ifstream fin("input.in");



//DONT MESS UP THIS NEXT TIME
int dx[] = {1,0,0,-1,1,-1,1,-1};
int dy[] = {0,1,-1,0,1,-1,-1,1};

int arr[10][10];

void spl(vector<string>& vect, string s){
  stringstream ss(s);
  string word;
  while(ss>>word){
    vect.push_back(word);
  }
}

void spl(vector<string>& vect, string s, char split){
  
  stringstream ss(s);
  string word;
  while(getline(ss,word,split)){
    vect.push_back(word);
  }
}


void spli(vector<int>& vect, string s){
  stringstream ss(s);
  string word;
  while(ss>>word){
    vect.push_back(stoi(word));
  }
}

void spli(vector<int>& vect, string s, char split){
  
  stringstream ss(s);
  string word;
  while(getline(ss,word,split)){
    vect.push_back(stoi(word));
  }
}


int flash(int x,int y){
  int num = 1;
  arr[x][y]=-1;
  for(int i=0;i<8;i++){
    int nx = dx[i]+x;
    int ny = dy[i]+y;
    if(nx>9||ny>9||nx<0||ny<0||arr[nx][ny]==-1) {continue;}

    if(arr[nx][ny]>=9){
      num+=flash(nx,ny);
    }else{
      arr[nx][ny]++;
    }
    
    
  }
  return num;

}

void fill(){
  for(int i=0;i<10;i++){
    for(int j=0;j<10;j++){
      if(arr[i][j]==-1){
        arr[i][j]=0;
      }
    }
  }
}



int step(){
  int count = 0;
  for(int i=0;i<10;i++){
    for(int j=0;j<10;j++){
      arr[i][j]++;
    }
  }
  
  for(int i=0;i<10;i++){
    for(int j=0;j<10;j++){
      if(arr[i][j]>9){
        count+=flash(i,j);
      }
    }
  }




return count;

}




bool check(){
  for(int i=0;i<10;i++){
    for(int j=0;j<10;j++){
      if(arr[i][j]!=-1){
        return false;
      }
    }
  }
  return true;
}


////////////////////////////



int main() {
string s;
vector<int> vect;
long long sum = 0;
long long cur;
string word;
int count = 0;

while(getline(fin,s)){
  for(int i=0;i<10;i++){
    arr[count][i] = stoi(s.substr(i,1));
  }
  
  count++;
}


while(!check()){
  fill();
  step();
  sum++;
}
cout<<sum;
return 0;
} 