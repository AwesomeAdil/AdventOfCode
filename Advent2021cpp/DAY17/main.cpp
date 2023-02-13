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


int x = 0;
int y =0;
    int xstart = 155;
    int xend = 182;
    int ystart = -67;
    int yend = -117;


bool work(int vx,int vy){
  while(x<=xend&&y>=yend){
    if(x>=xstart&&y<=ystart){
      return true;
    }
    
    x+=vx;
    y+=vy;
    if(vx!=0){
      vx--;
    }
    vy--;

  }
  return false;
}



    int main(){
      int count = 0;
      for(int i=0;i<1500;i++){
        for(int j=-174;j<250;j++){
          x = 0;
          y= 0;
          if(work(i,j)){
            count++;
          }
        }
      }
    cout<<count;
    }
