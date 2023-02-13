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

/* 

You did really fast on the first part. A couple things for the first was that you shouldve seen that the thingy was insert rather than making new so read the problem carefully, 

Second for the optimization: You came up with the idea really quickly. faster hands and trust urself. What mistake you kept making was counting the pairs twice when u couldve counted just the first value of the pair. Also shoudve seen that u kept changing data for the object we needed mid step

*/

using namespace std;
ifstream fin("input.in");

int dx[] = {1,1,-1,-1,0,-1,0,1}; 
int dy[] = {0,1,0,-1,1,1,-1,-1};

string por;

unordered_map<char,long long> cnt;
unordered_map<string,string> rep;
unordered_map<string,long long> pp;
vector<string> vect;




int main() {
  getline(fin,por);
  string s;
  getline(fin,s);
  while(getline(fin,s)){
    stringstream ss(s);
    string part,trash,part2;
    ss>>part>>trash>>part2;
    rep[part] = part2;
    vect.push_back(part);

  }

  for(int i=0;i<por.length()-1;i++){
    pp[por.substr(i,2)]++;
  }

  unordered_map<string,long long> temp;
  for(int t=0;t<40;t++){
     for(int i=0;i<vect.size();i++){
       string n1,n2;
       n1 = vect[i].substr(0,1)+rep[vect[i]]; 
       n2 = rep[vect[i]]+vect[i].substr(1,1); 

       temp[n1] += pp[vect[i]];
       temp[n2] += pp[vect[i]];
      
  }
  //NEEDED TO SEE THIS FASTER SHOUDLDVE NOTED THAT BOTH HIGHER THAN USUAL
  //AND ALSO THAT logically you cant go completely though one transition 
  //without changing data ur not supposed to change
    for(int i=0;i<vect.size();i++){
      pp[vect[i]] = temp[vect[i]];
      temp[vect[i]] = 0;
    }

  }

  char maxchar = 'a';
  char minchar = 'b';
  cnt['b']=10000000000000;


  for(int i=0;i<vect.size();i++){
    cnt[vect[i][0]] +=pp[vect[i]];
  }
  cnt[por[por.length()-1]]++;

  for(int i=(int)'A';i<=(int)'Z';i++){
    if(cnt[maxchar]<cnt[(char)i]){
      maxchar = (char)i;
    }else if(cnt[minchar]>cnt[(char)i]&&cnt[(char)i]!=0){
      minchar = (char)i;
    }
  }

  cout<<cnt[maxchar]-cnt[minchar];

} 