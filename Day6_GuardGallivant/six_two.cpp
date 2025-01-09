#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

// input file
const string FILENAME = "map.txt";

// Guard class tracks guard's position and direction
class Guard {
    public:
        // class members
        pair<int, int> location;
        string direction;

        // constructor always initializes guard facing up 
        Guard(pair<int, int> origin)
            : location(origin), direction("up") {}

        // function to move the guard to the next valid position
        void move(vector<string>& grid) {
            // assignment for better readability
            auto& x = location.first;
            auto& y = location.second;

            // check if guard is headed up
            if (direction == "up") {
                // check that there is no obstacle
                if(grid[y-1][x] != '#') {
                    // check if guard has visited this position before
                    if(grid[y-1][x] == '.'){
                        // drop up/down breadcrumb
                        grid[y-1][x] = '|';
                    } else if(grid[y-1][x] == '='){ 
                        // paths have crossed drop intersection breadcrumb
                        grid[y-1][x] = '+';
                    } // otherwise don't drop breadcrumb
                    // step up
                    y -= 1;
                } else { // obstacle encountered
                    // turn +90 degrees
                    direction = "right";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "right") { // check if the guard is headed right
                // check that there is no obstacle
                if(grid[y][x+1] != '#') {
                    // check if guard has visited this position before
                    if(grid[y][x+1] == '.'){
                        // drop left/right breadcrumb
                        grid[y][x+1] = '=';
                    } else if(grid[y][x+1] == '|'){
                        // paths have crossed drop intersection breadcrumb
                        grid[y][x+1] = '+';
                    } // otherwise don't drop breadcrumb
                    // step right
                    x += 1;
                } else { // obstacle encountered
                    // turn +90 degrees
                    direction = "down";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "down") { // check if the guard is headed down
                // check that there is no obstacle
                if(grid[y+1][x] != '#') {
                    // check if guard has visited this position before
                    if(grid[y+1][x] == '.'){
                        // drop up/down breadcrumb
                        grid[y+1][x] = '|';
                    } else if(grid[y+1][x] == '='){
                        // paths have crossed drop intersection breadcrumb
                        grid[y+1][x] = '+';
                    } // otherwise don't drop breadcrumb
                    // step down
                    y += 1;
                } else { // obstacle ancountered
                    // turn +90 degrees
                    direction = "left";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "left") { // check if the guard is headed left
                // check that there is no obstacle
                if(grid[y][x-1] != '#') {
                    // check if guard has visited this position before
                    if(grid[y][x-1] == '.'){
                        // drop left/right breadcrumb
                        grid[y][x-1] = '=';
                    } else if(grid[y][x-1] == '|'){
                        // paths have crossed drop intersection breadcrumb
                        grid[y][x-1] = '+';
                    } // otherwise don't drop breadcrumb
                    // step left
                    x -= 1;
                } else {
                    // turn +90 degrees
                    direction = "up";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            }
        }

        /*
        void dropBreadcrumb(vector<string>& grid){
            
        }
        */
};

// Laboratory class loads data from input file into a grid and tracks the guard within the grid
class Laboratory {
    public:
        // class members
        vector<string> grid;
        Guard guard;
        
        // Constructor initializes guard and loads data from file
        Laboratory(const string FILENAME) : guard({0, 0}) {
            loadData(FILENAME);
            // drop breadcrumb at origin
            grid[guard.location.second][guard.location.first] = 'X';
        }

        void loadData(string filename) {
            // place holder for each line of data read in
            string line;
            // read file
            ifstream file(filename);

            // collect all lines of data into one map vector
            while(getline(file, line)) {
                // record the current line
                grid.push_back(line);

                // check if the guard is on this line
                if(line.find('^') != string::npos) {
                    // find and initialize guard
                    guard = Guard({line.find('^'), grid.size() - 1});
                }
            }
        }

        void placeObstacle(int x, int y){
            grid[y][x] = 'O';
        }

        void printMap(){
            for(string line : grid){
                cout << line << endl;
            }
        }
};

int main() {
    // initialize lab
    Laboratory lab(FILENAME);

    // variables for easy access
    auto& x = lab.guard.location.first;
    auto& y = lab.guard.location.second;
    auto& grid = lab.grid;

    // as long as the guard stays within the lab, keep moving
    while(y > 0 && x > 0 && y < grid.size() - 1 && x < grid[y].size() - 1) {
        lab.guard.move(grid);
    }

    lab.printMap();

    return 0;

    // https://adventofcode.com/2024/day/6#part2
    // ANSWER: ??? (varies with input file)
}