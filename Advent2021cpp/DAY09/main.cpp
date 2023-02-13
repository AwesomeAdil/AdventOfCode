#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <utility>
#include <string>
#include <sstream>
using namespace std;
ifstream fin("input.in");
 int arr[105][105];
 int dx[] = {1,-1,0,0};
int dy[] = {0,0,1,-1};

bool checkmin(int x,int y){
  for(int i=0;i<4;i++){
    if(dx[i]+x>=100||dy[i]+y>=100||dx[i]+x<0||dy[i]+y<0){
      continue;
    }
    else if(arr[dx[i]+x][dy[i]+y]<=arr[x][y]){
      return false;
    }
  }
  return true;
}

bool visited[105][105];

void reset(){
  for(int i=0;i<105;i++){
    for(int j=0;j<105;j++){
      visited[i][j]=false;
    }
  }
}
int findsize(int x,int y,int curval){
  int big = 1;
  if(visited[x][y]){
    return 0;
  }
  visited[x][y] = true;
  for(int i=0;i<4;i++){
    if(dx[i]+x>=100||dy[i]+y>=100||dx[i]+x<0||dy[i]+y<0){
      continue;
    }

    int nx = dx[i]+x;
    int ny = dy[i]+y;
    if(visited[nx][ny]||arr[nx][ny]==9){
      continue;
    }
    if(curval<arr[nx][ny]){
      big+=findsize(nx,ny,arr[nx][ny]);
    }
  }
  return big;
}

int main() {
string s;
int sum = 0;

int count = 0;

while(getline(fin,s)){
 

  for(int i=0;i<s.length();i++){
    arr[count][i] = stoi(s.substr(i,1));
  }
  count++;
}

for(int i=0;i<count;i++){
  for(int j=0;j<s.length();j++){
    cout<<arr[i][j];
  }
  cout<<endl;
}

vector<int> sizes;


for(int i=0;i<count;i++){
  for(int j=0;j<s.length();j++){
    reset();
    sizes.push_back(findsize(i,j,arr[i][j]));
    sort(sizes.begin(),sizes.end());
    if(sizes.size()==4){
      sizes.erase(sizes.begin());
    }
  }
}
sort(sizes.begin(),sizes.end());
int len = sizes.size();
for(int u:sizes){
  cout<<u<<endl;
}
cout<<sizes[len-1]*sizes[len-2]*sizes[len-3];




//cout<<sum;
return 0;
}