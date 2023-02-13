#include <iostream>
#include <fstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstring>
#include <utility>

using namespace std;


/* 
AWESOME FIRST DIJKSTRAS IMPLEMENTATION.... next time try not to use ur note book. Very similar to bfs

set visited with distance and all
make sure u add distance properly 
and make sure u dont go out of bounds
make sure that the distance added is distance already have + new dist

MAIN ISSUE: Reading the problem....
i swear to god...
anyway see the loop around. 
SHOULDVE SEEN that the smaller array not being
read properly with the while loop

*/




long long dx[] = {1,-1,0,0};
long long dy[] = {0,0,-1,1};
priority_queue<pair<long long,pair<long long,long long> >, vector<pair<long long,pair<long long,long long> >>, greater<pair<long long,pair<long long,long long> >>> pq;
long long dist[505][505];
ifstream fin("input.in");
long long arr[505][505];
long long smr[105][105];

//bool visited[505][505];
int main() {
  string s;
  int count = 0;

  
  while(getline(fin,s)){

    long long len = s.length();

      
          for(long long y=0;y<len;y++){
            

            smr[count][y] = stoi(s.substr(y,1));
          
           }
           count++;
        }
  

  // for(int i=0;i<10;i++){
  //   for(int j=0;j<10;j++){
  //     cout<<smr[i][j];
  //   }
  //   cout<<endl;
  // }

    for(long long i=0;i<5;i++){
      for(long long j=0;j<5;j++){
          for(int x=0;x<100;x++){
            for(int y=0;y<100;y++){
              long long nx = x+100*i;
              long long ny = y+100*j;
              arr[nx][ny] = (smr[x][y]+i+j-1)%9+1;
              dist[nx][ny] = -1;
            }
          }

          
       }
    }
    
  
      
  
 
  pair<long long,pair<long long,long long>> poi = {arr[0][0],{0,0}};
  pq.push(poi);
  while(!pq.empty()){
    pair<long long,pair<long long,long long> > spot = pq.top();
    pq.pop();
    if(dist[spot.second.first][spot.second.second]!=-1){
      continue;
    }
    dist[spot.second.first][spot.second.second] = spot.first;
    
    for(long long i=0;i<4;i++){
      long long nx = spot.second.first+dx[i];
      long long ny = spot.second.second+dy[i];
      if(nx<0||ny<0||nx>=500||ny>=500) continue;

      if(dist[nx][ny]==-1){
        pq.push({spot.first+arr[nx][ny],{nx,ny}});
      }
    }


  }
  // for(long long i=0;i<50;i++){
  //   for(long long j=0;j<50;j++){
  //     cout<<dist[i][j];
  //   }
  //   cout<<endl;
  // }
  cout<<dist[499][499]-dist[0][0];
} 