#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>
#include <unordered_map>
using namespace std;
ifstream fin("input.in");

bool sortbylen(string a,string b){
  return a.length()<b.length();
}


int main() {
  string s;
  int tot = 0;
  while(getline(fin,s)){
  vector<string> list;
  
    unordered_map<string,int> mp;
    stringstream ss(s);
    bool seen = false;
    string word;
   // int count=0;
    int num = 0;
    while(ss>>word){
     
       sort(word.begin(),word.end());
      if(word!="|"){list.push_back(word);}
     
      if(word=="|"){
        //cout<<"HEEEEEELLLLLLP";
        seen=true;
        sort(list.begin(),list.end(),sortbylen);
       
        mp[list[0]]=1;
        mp[list[9]] = 8;
        mp[list[1]]=7;
        mp[list[2]]=4;
        // for(int i=0;i<3;i++){
        //   if(list[1][i]!=list[0][0]){
        //     if(list[1][i]!=list[0][1]){
        //         top= list[1][i];
        //     }
            
        //   }
        // }
      
      for(int k=3;k<=5;k++){
        bool threecheck [] = {false,false,false};
        
        bool three = true;
        for(int i=0;i<5;i++){
          if(list[k][i]==list[1][0]){
            threecheck[0]=true;
          }else if(list[k][i]==list[1][2]){
            threecheck[1]=true;
          }else if(list[k][i]==list[1][1]){
            threecheck[2]=true;
          }
        }


        for(int i=0;i<3;i++){
          if(!threecheck[i]){
            three=false;
          }
        }
        if(three){
          mp[list[k]]=3;
        }
      }

      for(int k=6;k<=8;k++){
        bool ninecheck [] = {false,false,false,false};
        
        bool nine = true;
        for(int i=0;i<6;i++){
          if(list[k][i]==list[2][0]){
            ninecheck[0]=true;
          }else if(list[k][i]==list[2][2]){
            ninecheck[1]=true;
          }else if(list[k][i]==list[2][1]){
            ninecheck[2]=true;
          }else if(list[k][i]==list[2][3]){
            ninecheck[3]=true;
          }
        }


        for(int i=0;i<4;i++){
          if(!ninecheck[i]){
            nine=false;
          }
        }
        if(nine){
          mp[list[k]]=9;
         // break;
        }
      }


      string sip="";
      for(int i=6;i<=8;i++){
        bool sixcheck[]={false,false,false};
        bool six = false;
        for(int k=0;k<6;k++){
          if(list[i][k]==list[1][0]){
            sixcheck[0]=true;
          }else if(list[i][k]==list[1][1]){
            sixcheck[1]=true;
          }else if(list[i][k]==list[1][2]){
            sixcheck[2]=true;
          }
        }

        for(int j=0;j<3;j++){
          if(!sixcheck[j]){
            six=true;
            mp[list[i]]=6;
            sip=list[i];
          }
        } 
      }
    for(int k=3;k<=5;k++){
      bool five = true;
      for(int i=0;i<5;i++){
        bool works = false;
        for(int j=0;j<6;j++){
          if(sip[j]==list[k][i]){
            works=true;
          }
        }
        if(!works){
          five = false;
        }
      }
      if(five){
        mp[list[k]]=5;
      }
    }

    for(int k=3;k<=5;k++){
      if(mp[list[k]]==0){
        mp[list[k]]=2;
      }
    }

   
        
          for(int k=6;k<=8;k++){
      if(mp[list[k]]==0){
        mp[list[k]]=0;
      }
    }




      }else if(seen){
        for(int i=0;i<=9;i++){
          cout<<mp[list[i]]<<" ";
        }
        cout<<endl;
        num=num*10+mp[word];
      }
      
    }
   tot+=num; 
  }
  cout<<tot;
  return 0;
} 