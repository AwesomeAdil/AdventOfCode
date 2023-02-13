#include <bits/stdc++.h>

using namespace std;

ifstream fin("input.in");

long long dp[11][11][22][22];
bool seen [11][11][22][22];
long long amts[10];

long long rec(int spot1, int spot2, int score1, int score2){
  long long val = 0;

 if(score1>=21){
    return 1;
  }

  if(score2>=21){
    return 0;
  }
 if(seen[spot1][spot2][score1][score2]) return dp[spot1][spot2][score1][score2];
  seen[spot1][spot2][score1][score2] = true;
  for(int i=3;i<=9;i++){
    for(int j=3;j<=9;j++){
      int nspot1 = (spot1+i-1)%10+1;
      int nscore1 = score1+nspot1;
      if(nscore1>=21){
        val+=amts[i];
        break;
      }

      int nspot2 = (spot2+j-1)%10+1;;
      int nscore2= score2+nspot2;
      val+=amts[i]*amts[j]*rec(nspot1,nspot2,nscore1, nscore2);
        }
  }

  dp[spot1][spot2][score1][score2] = val;
  return val;

}


int main() {
  amts[3] = 1;
  amts[9] = 1;
  amts[4] = 3;
  amts[8] = 3;
  amts[5] = 6;
  amts[7] = 6;
  amts[6] = 7;
  int start1 = 3;
  int start2 = 10;
  int score1 = 0;
  int score2 = 0;
  int dice = 1;
  int num  = 0;

  cout<<rec(3,10,0,0);

  

  // while(score1<1000&&score2<1000){
  //   int move = dice+((dice)%100+1)+((dice+1)%100)+1;
  //  // cout<<move<<endl;
  //   dice = ((dice+2)%100)+1;
  //   if(num%2==0){
  //     start1 = (start1+(move)-1)%10+1;
  //     score1+=start1;
  //     cout<<"1: "<<score1<<endl;
  //   }else{
  //     start2 = (start2+(move)-1)%10+1;
  //     score2+= start2;
  //     cout<<"2: "<<score2<<endl;
  //   }

  //   num++;
  // }

  // cout<<num<<endl;
  // cout<<score2<<endl;
  // cout<<min(score1,score2)*num*3;
  unordered_map<int,int> mp1;
  unordered_map<int,int> mp2;
 


} 