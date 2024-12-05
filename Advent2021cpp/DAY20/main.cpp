#include <bits/stdc++.h>

using namespace std;

ifstream fin("input.in");



vector<string> vect;
vector<string> build;
string key;

char lookup(int num){
  return key[num];
}

void incase(){
  vect.clear();
  string s;
  getline(fin,s);
  string tops="";
  for(int i=0;i<s.size()+4;i++){
    tops+=".";
  }
  vect.push_back(tops);
  s = ".."+s+"..";
  vect.push_back(s);
  while(getline(fin,s)){
    s = ".."+s+"..";
    vect.push_back(s);
  }
  vect.push_back(tops);
}


void incase(string str, int t){

if(t%2==0){
  stringstream ss(str);
  vect.clear();
  string s;
  getline(ss,s,'\n');
  string tops="";
  for(int i=0;i<s.size()+4;i++){
    tops+="#";
  }
  vect.push_back(tops);
  s = "##"+s+"##";
  vect.push_back(s);
  while(getline(ss,s,'\n')){
    s = "##"+s+"##";
    vect.push_back(s);
  }
  vect.push_back(tops);

}else{


  stringstream ss(str);
  vect.clear();
  string s;
  getline(ss,s,'\n');
  string tops="";
  for(int i=0;i<s.size()+4;i++){
    tops+=".";
  }
  vect.push_back(tops);
  s = ".."+s+"..";
  vect.push_back(s);
  while(getline(ss,s,'\n')){
    s = ".."+s+"..";
    vect.push_back(s);
  }
  vect.push_back(tops);


}

}

void incase(vector<string> build){
  vect.clear();
  string s = build[0];
  string tops="";
  for(int i=0;i<s.size()+4;i++){
    tops+=".";
  }
  vect.push_back(tops);
  s = ".."+s+"..";
  for(int i=1;i<build.size();i++){
    vect.push_back(".."+build[i]+"..");
  }
  vect.push_back(tops);

}

void conv(int time){
  build.clear();
  for(int i=0;i<vect.size();i++){
    build.push_back("");
    for(int j=1;j<vect[i].size()-1;j++){
      string pwd = "";
      for(int x=-1;x<=1;x++){
        for(int y=-1;y<=1;y++){
          int nx = i+x;
          int ny = j+y;
          if(nx<0||ny<0||nx>=vect.size()||ny>=vect[i].size()){
            if(time%2 == 0){
              pwd+="0";
              continue;
            }else{
              pwd+="1";
              continue;
            }
            
          }
          if(vect[nx][ny]=='.') pwd += "0";
          else pwd += "1";
          

        }
      }
      build[i] += lookup(stoi(pwd,0,2));

    }
  }


}


int main() {

  getline(fin,key);
  string s;
  getline(fin,s);

 incase();

  for(int i=0;i<1;i++){
    conv(i);
    incase(build);
  }
  int counter = 0;

//for(int q=0;q<1;q++){

for(int k=0;k<49;k++){

string newer="";
  for(int i=0;i<build.size();i++){
      newer+=build[i]+"\n";



  }
incase(newer, k);
conv(k+1);

}





//}






 for(int i=0;i<build.size();i++){
      counter+=count(build[i].begin(),build[i].end(),'#');
      cout<<build[i]<<endl;
    //  newer+=build[i]+"\n";
  }
cout<<counter;



} 
