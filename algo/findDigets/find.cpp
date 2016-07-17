#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <sstream> 
using namespace std;

int main(){
    int t;
    cin >> t;
    for(int a0 = 0; a0 < t; a0++){
        int n;
        cin >> n;
        stringstream ss;
        ss << n;
        char diget_c;
        int count = 0; 
        while ( ss >> diget_c ){
            int diget = diget_c - '0';
            if ( diget != 0 && n % diget == 0 ) {
                ++count;
            }
        }
        cout << count << endl; 
    }
    return 0;
}
