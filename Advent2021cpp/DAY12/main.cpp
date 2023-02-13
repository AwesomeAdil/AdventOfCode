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
#include <cctype>
#include <iostream>
#include <cstring>
using namespace std;

ifstream fin("input.in");



//DONT MESS UP THIS NEXT TIME
int dx[] = {1,0,0,-1,1,-1,1,-1};
int dy[] = {0,1,-1,0,1,-1,-1,1};

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
unordered_map<string,vector<string>> adj;
// vector<string> adjlist[1005];
unordered_map<string,int> mp;




////////////////////////////



int main() {
  string s;

while(getline(fin,s)){
  stringstream ss(s);
  string a;
  string b;
  getline(ss,a,'-');
  ss>>b;
  adj[a].push_back(b);
  adj[b].push_back(a);
  mp[a]=0;
  mp[b]=0;
}



long long sum = 0;
queue<pair<pair<string,bool>,unordered_map<string,int>>> q;

q.push({{"start",false},mp});
while(!q.empty()){
  pair<pair<string,bool>,unordered_map<string,int>> spot = q.front();
  spot.second[spot.first.first]++;
  
  q.pop();
  
  for(string u:adj[spot.first.first]){
  
  if(u=="start"){
    continue;
  }
  if(u=="end"){
      sum++;
      continue;
    }
  if((spot.second[u]==1&&islower(u[0]))&&!spot.first.second){
 
      q.push({{u,true},spot.second});
  }

  else if((spot.second[u]>=1&&islower(u[0]))&&spot.first.second){
      continue;
    }

    else{ 
      q.push({{u,spot.first.second},spot.second});
    }
  }

}


  cout<<sum;



return 0;
}