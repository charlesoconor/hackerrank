/*
 * main.cpp
 * Copyright (C) 2016-05-05 22:05 coconor <coconor@umich.edu>
 *
 * 
 */

#include <iostream>

using namespace std;

int main( int argc, char** argv ){
    
    int in; 
    cin >> in;
    switch( in ){
        case 1 :
            cout << "one\n";
            break;
        case 2 :
            cout << "two\n";
            break;
        case 3 :
            cout << "three\n";
            break;
        case 4 :
            cout << "four\n";
            break;
        case 5 :
            cout << "five\n";
            break;
        case 6 :
            cout << "six\n";
            break;
        case 7 :
            cout << "seven\n";
            break;
        case 8 :
            cout << "eight\n";
            break;
        case 9 :
            cout << "nine\n";
            break;
        default:
            cout << "Greater than 9\n";
            break;
    }
    return 0;
}
