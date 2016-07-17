/*
 * main.cpp
 * Copyright (C) 2016-04-19 17:11 coconor <coconor@umich.edu>
 *
 * 
 */

#include <iostream>
#include <vector>
#include <map>

using namespace std;

bool debug = true;


struct cmp_by_x {
  bool operator()(int left, int right) const{
    return left > right;
  }
};

int main( int argc, char** argv ){
    int n, k;
    cin >> n >> k;

    vector<int> digets(n);
    map<int, int, cmp_by_x> diget_map;

    for( int i = 0; i < n; ++i){
        int in;
        cin >> in;
        digets[i]=in;
        diget_map[in]=i;
    }

    if ( debug ){
        cout << "N: " << n << endl;
        cout << "K: " << k << endl;

        for ( auto i : digets )
            cout << i;

        cout << endl;

        for( auto i : diget_map){
            cout << "( " <<  i.first << " " <<  i.second << " )\n";
        }
    }


    int index = 0;
    for( auto it = diget_map.begin(); it != diget_map.end() && k > 0; ++it){

        if (it->first < digets[index] ){
            it--;
        } else if ( it->second > index + 1 ){
            digets[it->second]=digets[index];
            digets[index]=it->first;
            --k;
        } 

        ++index;
    }


    for ( auto i : digets )
        cout << i << " ";

    cout << endl;


    return 0;
}
