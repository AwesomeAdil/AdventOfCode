 #include<bits/stdc++.h>
 using namespace std;
 ifstream fin("input.in");

 string s;

 void addpare(string s2){
   s = "["+s+","+s2+"]";
 }


 void repl(int loc, int val){

   while(((s[loc]=='['||s[loc]==']')||s[loc]==',')&&loc<s.length()){
     loc--;
     if(loc==0) return;

   }

   if((s[loc-1]=='['||s[loc-1]==']')||s[loc-1]==','){
     int v = stoi(s.substr(loc,1))+val;
     s.replace(loc,1,to_string(v));
   }else if((s[loc-2]=='['||s[loc-2]==']')||s[loc-2]==','){
       int v = stoi(s.substr(loc-1,2))+val;
       s.replace(loc-1,2,to_string(v));

   }else{
     int v = stoi(s.substr(loc-2,2))+val;
       s.replace(loc-2,2,to_string(v));
       cout<<"WOOHOOO";

   }


 }


 void repr(int loc, int val){
 
   while(((s[loc]=='['||s[loc]==']')||s[loc]==',')&&loc<s.length()){
     loc++;
     if(loc==s.length()-1) return;

   }

   if((s[loc+1]=='['||s[loc+1]==']')||s[loc+1]==','){
     int v = stoi(s.substr(loc,1))+val;
     s.replace(loc,1,to_string(v));
   }else{
       int v = stoi(s.substr(loc,2))+val;
       s.replace(loc,2,to_string(v));

   }

 }






 //[[[[0,4],4],[7,[0,9]]],[1,1]]
 //[[[[0,4],4],[7,[0,9]]],[1,1]]
 void explode(int left, int right, int initdepth){

   int lv;
   int rv;
   int brac = initdepth;
   for(int i=left;i<right;i++){
     if(s[i]=='[') brac++;
     else if(s[i]==']') brac--;
     else if(s[i]==',') continue;
     else{
       if(brac==5){

         int com = s.find(",",i);
         lv = stoi(s.substr(i,com-i));
         rv = stoi(s.substr(com+1, s.find("]",i)-com-1));
         //cout<<"HERE: "<<lv<<" "<<rv<<endl;
        // cout<<endl;
         //cout<<s<<endl;
         repr(s.find("]",i),rv);
        

         s.replace(i-1,s.find("]",i)+2-(i),"0");
           if(s[i]==']'){
             brac--;
           }
           repl(i-2,lv);
          brac--;
           //brac = 0;
           //i=left;
          
       }
     }
   }

 }

 void spliter(){
 bool work = true;
  int val = 0;
 while(work){
   work = false;
  for(int i=0;i<s.length()-1;i++){
     if((s[i]=='['||s[i]==']')||s[i]==','){
       if(s[i]=='['){
         val++;
       }else if(s[i]==']'){
         val--;
       }
       continue;
     }
    if((s[i+1]=='['||s[i+1]==']')||s[i+1]==','){
      if(s[i+1]=='['){
          val++;
        }else if(s[i+1]==']'){
          val--;
        }
     continue;
    }
    work = true;
     //cout<<"moftuyigudfguhiouiyuthgjho ";
    // cout<<s.substr(i,2)<<endl;
    

     int valer = stoi(s.substr(i,2));
     double val = valer/1.;
     string rep = "["+to_string((int)(val/2))+","+to_string((int)ceil(val/2.))+"]";
    s.replace(i,2,rep);
   explode(i, i+rep.length()+1,val);
   //i=0;
   }

 }
 

 }






 long long magnitude(string str){
   long long val = 0;
   int brac = 0;
   if(str.find("[")==-1){
       //  cout<<"A\n";
     return stoll(str);
    
   }
   for(int i=0;i<str.length();i++){

     if(str[i]=='[') brac++;
     else if(str[i]==']') brac--;
     else{
       if(brac==1&&str[i]==','){
        // cout<<str.substr(1,i-1)<<" "<<str.substr(i+1,str.length()-2-i)<<endl;
         val+=3*magnitude(str.substr(1,i-1));
         val+=2*magnitude(str.substr(i+1,str.length()-2-i));
        // return val;
       }
     }
   }
   return val;
 }





 int main() {

   getline(fin,s);
   string ns;

   explode(0,s.length(),0);
   spliter();

   getline(fin,ns);
   swap(ns,s);
   explode(0,s.length(),0);
   spliter();
   swap(ns,s);
   addpare(ns);
   // cout<<s<<endl;
   explode(0,s.length(),0);
   cout<<"########################\n";
   cout<<s<<endl;
   spliter();

cout<<"hec\n";
 // cout<<s<<endl;

while(getline(fin,ns)){
 //swap(s,ns);
 cout<<s<<endl;

explode(0,s.length(),0);
spliter();
// swap(s,ns);
  addpare(ns);
  explode(0,s.length(),0);
  spliter();
  explode(0,s.length(),0);
  spliter();
  explode(0,s.length(),0);
  spliter();
 explode(0,s.length(),0);
  spliter();
  explode(0,s.length(),0);
  spliter();
 explode(0,s.length(),0);
  spliter();
  explode(0,s.length(),0);
  spliter();
 explode(0,s.length(),0);
  spliter();
  explode(0,s.length(),0);
  spliter();
 explode(0,s.length(),0);
  explode(0,s.length(),0);
  
}


cout<<s;

cout<<magnitude(s);
} 