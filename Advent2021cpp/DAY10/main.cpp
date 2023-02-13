#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>
#include <unordered_map>
#include <string>
#include <stack>
using namespace std;
ifstream fin("input.in");

unordered_map<char,int> mp;

bool match(char a, char b){
  if(a=='('&&b==')'){
    return true;
  }
if(a=='{'&&b=='}'){
    return true;
  }
  if(a=='['&&b==']'){
    return true;
  }
  if(a=='<'&&b=='>'){
    return true;
  }
  return false;
}

long long score(string s){
  stack<char> st;
  long long scorer = 0;
  for(int i=0;i<s.length();i++){
    if(s[i]=='('||s[i]=='['||s[i]=='{'||s[i]=='<'){
      st.push(s[i]);
    }else if(match(st.top(),s[i])){
      st.pop();
    }else{
      //cout<<"moo??";
      if(s[i]==')'){
        scorer+=3;
      }else if(s[i]==']'){
          scorer+=57;
      }else if(s[i]=='}'){
        scorer+=1197;
      }else{
  scorer+=25137;
      }
      st.pop();
    }


  }



  if(scorer==0&&st.size()>0){
while(!st.empty()){
     scorer*=5;

      if(st.top() =='('){
        scorer-=1;
      }else if(st.top()=='['){
          scorer-=2;
      }else if(st.top()=='{'){
        scorer-=3;
      }else{
  scorer-=4;
      }
st.pop();

    }
  
  }


  if(!st.empty()){
    return 0;
  }
  return scorer;
}


int main() {
  long long sum = 0;
  string s;
  vector<long long> scores;

  while(getline(fin,s)){
    //cout<<s<<endl;
    if(score(s)>=0){
      continue;
    }else{
//cout<<"AHA "<<score(s)<<endl;
scores.push_back(-score(s));
    }


  }
  sort(scores.begin(),scores.end());
  int plz = scores.size();

  cout<<scores[plz/2];


  //cout<<sum;

  return 0;
} 