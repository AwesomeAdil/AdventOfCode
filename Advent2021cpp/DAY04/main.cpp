#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
using namespace std;
ifstream fin("input1.in");
struct board{
int arr[5][5];
};
bool checkboard(board b){
  ////rows
for(int i=0;i<5;i++){
  bool row = true;
  for(int j=0;j<5;j++){
    if(b.arr[i][j]!=-1){
      row = false;
    }
  }
  if(row){
    return true;
  }
}
  ////columns
  for(int i=0;i<5;i++){
  bool col = true;
  for(int j=0;j<5;j++){
    if(b.arr[j][i]!=-1){
      col = false;
    }
  }
  if(col){
    return true;
  }
}
return false;
}

int calscore(board b){
  int sum = 0;
  for(int i=0;i<5;i++){
    for(int j=0;j<5;j++){
      if(b.arr[i][j]!=-1){
        sum+=b.arr[i][j];
      }
    }
  }
  return sum;
}

int main() {
board rw;
int rv;
vector<int> list;
//CHANGE BACK
for(int i=0;i<100;i++){
  int a;
  char trash;
  fin>>a>>trash;
  list.push_back(a);
}
vector<board> boards;

int n = 0;
int cn;
board cb;
while(fin>>cn){
  cb.arr[n/5][n%5]=cn;
  n++;
  if(n>=25){
    n=0;
    boards.push_back(cb);
  }
}

bool found = false;
int spot = 0;
while(!found){
  for(int q=0;q<boards.size();q++){
    for(int i=0;i<5;i++){
      for(int j=0;j<5;j++){
        if(boards[q].arr[i][j]==list[spot]){
          boards[q].arr[i][j]=-1;
        }
      }
    }
    if(checkboard(boards[q])){
      rw = boards[q];
      rv = list[spot];
      for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
          boards[q].arr[i][j]=-20;
        }
      }

      cout<<q<<" "<<rv<<" ";
           // return 0;
    }
  }
  //cout<<list[spot]<<" ";
  spot++;
  if(spot>=list.size()){

    cout<<calscore(rw)*rv;
    cout<<"NOPPE";
    return 0;
  }
}
return 0;
}
