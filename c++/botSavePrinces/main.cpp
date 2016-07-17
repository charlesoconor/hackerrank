#include <iostream>
#include <vector>
#include <stdexcept> // runtime_error
#include <queue>

using namespace std;

struct point {
    int x;
    int y;
};


void displayPathtoPrincess(const int n, vector <string>& grid){
    //your logic here
    

    point start;
    queue<point> to_check
    start.y = -1;

    for ( int i = 0; i < n; ++j ){
        for( int j = 0; j < n; ++j ){

            if ( grid[i][j] == 'm' ){
                start.x = i;
                start.y = j;
            }
        }
    }

    if ( start.y == -1 ){
        throw runtime_error("No princess");
    }

    to_check.push(start);

    while( !to_check.empty() ){
        point current_point = to_check.pop();

        if ( 
    }



}

int main(void) {

    int m;
    vector <string> grid;

    cin >> m;

    for(int i=0; i<m; i++) {
        string s; cin >> s;
        grid.push_back(s);
    }

    displayPathtoPrincess(m,grid);

    return 0;
}
