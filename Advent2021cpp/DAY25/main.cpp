#include <bits/stdc++.h>

using namespace std;

ifstream fin("input.in");

string arr[137];
string brr[137];

void transfer(){

  for(int i=0;i<137;i++){
    arr[i] = brr[i];
  }
}

bool stepeast(){
  bool moved = false;
  for(int i=0;i<137;i++){
    for(int j=0;j<arr[i].length();j++){

      if(arr[i][j]=='>'&&arr[i][(j+1)%arr[i].length()]=='.'){
        brr[i][j] = '.';
        brr[i][(j+1)%arr[i].length()] = '>';
        moved = true;
      }else if(arr[i][j] == '.'&&arr[i][(j+arr[i].length()-1)%arr[i].length()]=='>'){
        continue;
      }else{
        brr[i][j] = arr[i][j];
      }
    }
  }
  transfer();
  return moved;
}

bool stepsouth(){
  bool moved = false;
  for(int i=0;i<137;i++){
    for(int j=0;j<arr[i].length();j++){
      
      if(arr[i][j]=='v'&&arr[(i+1)%137][j]=='.'){
        brr[i][j] = '.';
        brr[(i+1)%137][j] = 'v'; 
        moved = true;
      }else if(arr[i][j] == '.'&&arr[(i-1+137)%137][j]=='v'){
        continue;
      }else{
        brr[i][j] = arr[i][j];
      }
    }
  }
  transfer();
  return moved;
}





bool step(){
  bool moved = false;
  moved|=stepeast();
  moved|=stepsouth();

  return moved;
}


int main(){
  string s;
  int count = 0;

  for(int i=0;i<137;i++){
    getline(fin,s);
    arr[i] = s;
    brr[i] = s;
  }


  while(step()){
    count++;
  }

cout<<count;

} 