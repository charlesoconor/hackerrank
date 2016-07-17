#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


string d_num( int n ){
    for ( int i = n - ( n % 3 ); i >= 0; i-=3 ){
       if ( (n - i) % 5  == 0 ){
           string str = "";
           for( int j = 0; j < i; j+=3 ){
               str += "555";
           }
           for( int j = 0; j < n - i ; j+=5 ){
               str += "33333";
           }
           return str;
       } 
    }
    
    // default case 
    return "-1"; 
}

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        cout << d_num(n) << endl; 
    }
    return 0;
}
