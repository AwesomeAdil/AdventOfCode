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
ifstream fin("input.in");

string HexToBin(string hexdec)
{
    long long i = 0;
    string res = "";
    while (hexdec[i]) {
 
        switch (hexdec[i]) {
        case '0':
            res= res + "0000";
            break;
        case '1':
            res= res + "0001";
            break;
        case '2':
            res= res + "0010";
            break;
        case '3':
            res= res + "0011";
            break;
        case '4':
            res= res +  "0100";
            break;
        case '5':
            res= res + "0101";
            break;
        case '6':
            res= res +  "0110";
            break;
        case '7':
            res= res +  "0111";
            break;
        case '8':
            res= res +  "1000";
            break;
        case '9':
            res= res +  "1001";
            break;
        case 'A':
        case 'a':
            res= res +  "1010";
            break;
        case 'B':
        case 'b':
            res= res +  "1011";
            break;
        case 'C':
        case 'c':
            res= res +  "1100";
            break;
        case 'D':
        case 'd':
            res= res +  "1101";
            break;
        case 'E':
        case 'e':
            res= res +  "1110";
            break;
        case 'F':
        case 'f':
            res= res +  "1111";
            break;
        default:
            res= res +  "\nInvalid hexadecimal digit ";
        }
        i++;
    }
    return res;
}



 long sum = 0;
 long spot = 0;
string s;
 long rec(){
  if(spot>s.length()-9){
    spot = s.length();
    return 0;
  }
  // cout<<spot<<endl;
   long val = stoll(s.substr(spot,3),0,2);
  sum+=val;
  spot+=3;
   long type = stoll(s.substr(spot,3),0,2);
  spot+=3;
  if(type==4){
   // cout<<spot<<" A"<<endl;
     long begin = spot;
     long end = 0;
     long look = s[spot]-'0';
     string cong = "";
    while(look==1){
      cout<<"moooo";
      cong+=s.substr(spot+1,4);
      end+=5;
      spot+=5;
      look = s[spot]-'0';
    }
        cong+=s.substr(spot+1,4);
    spot+=5;

    end+=5;
    cout<<"LITTTTT "<<stoll(cong,0,2)<<endl;

    cout<<begin<<" "<<spot<<endl;
    return stoll(cong,0,2);
  }else{
    vector< long> subpacks;
     long id = s[spot]-'0';
    spot++;
    if(id){
      // cout<<spot<<" B\n";
       long num = stoll(s.substr(spot,11),0,2);
      spot+=11;
      // cout<<"HHEHEHHREIHJRIEHEIHI "<<num<<endl;  
      for( long i=0;i<num;i++){
        
        subpacks.push_back(rec());
      }

    }else{
      // cout<<spot<<" "<<sum<<" C\n";
       long numbit = stoll(s.substr(spot,15),0,2);
      spot+=15;
       long curbit = 0;
       long cspot = spot;
      while(spot-cspot<numbit&&spot<s.length()){
        subpacks.push_back(rec());
      }
    }

    if(type == 0){
    
       long sumdum = 0;
      for( long i=0;i<subpacks.size();i++){
        // cout<<subpacks[0]<<" ";
        sumdum += subpacks[i];
      }
      return sumdum;
    }else if(type==1){
      // cout<<"yaaaay";
       long prodsod = 1;
      for( long i=0;i<subpacks.size();i++){
        prodsod *= subpacks[i];
      }
      return prodsod;
    }else if(type==2){
       long long miner = subpacks[0];
      for(long long u: subpacks){
        miner = min(u,miner);
      }
      
      return miner;
    }else if(type==3){
      long long maxer = subpacks[0];
      for(long long u: subpacks){
        maxer = max(u,maxer);
      }
      return maxer;
    }else if(type==5){
      return subpacks[0]>subpacks[1];
    }else if(type==6){
      return subpacks[0]<subpacks[1];
    }else{
      return subpacks[0]==subpacks[1];
    }

  }
 return 0;
}

int main() {

  while(getline(fin,s)){
    stringstream ss(s);
  }
  s = HexToBin(s);
   cout<<s.length()<<endl;
  cout<<endl<<endl<<"MOOOO: ";
  cout<<rec()<<endl;
} 