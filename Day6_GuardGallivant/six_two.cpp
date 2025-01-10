#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <format>

using namespace std;

// input file
const string FILENAME = "map.txt";

// Guard class tracks guard's position and direction
class Guard {
    public:
        // class members
        pair<int, int> location;
        string direction;
        // create flag for if guard is retracing previous steps
        bool retracing = false;
        // create flag for guard being stuck in loop
        bool looping = false;

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
                if(grid[y-1][x] != '#' && grid[y-1][x] != 'O') {
                    // check if guard has not visited this position before
                    if(grid[y-1][x] == '.'){
                        // drop up/down breadcrumb
                        grid[y-1][x] = '|';
                        // reset retracing flag
                        retracing = false;
                    } else if(grid[y-1][x] == '-'){ 
                        // paths have crossed, drop intersection breadcrumb
                        grid[y-1][x] = '+';
                        // reset retracing flag
                        retracing = false;
                    } else {
                        // otherwise the guard is retracing a previous path
                        retracing = true;
                    }
                    // step up
                    y -= 1;
                } else if(retracing && (grid[y][x+1] == '-' || grid[y][x+1] == '+')) { // previous obstacle encountered
                    cout << "looping!" << endl;
                    looping = true;
                    return;
                } else { // new obstacle encountered
                    cout << "Obstacle encountered!" << endl;
                    // turn +90 degrees
                    direction = "right";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "right") { // check if the guard is headed right
                // check that there is no obstacle2
                if(grid[y][x+1] != '#' && grid[y][x+1] != 'O') {
                    // check if guard has visited this position before
                    if(grid[y][x+1] == '.'){
                        // drop left/right breadcrumb
                        grid[y][x+1] = '-';
                        // reset retracing flag
                        retracing = false;
                    } else if(grid[y][x+1] == '|'){
                        // paths have crossed, drop intersection breadcrumb
                        grid[y][x+1] = '+';
                        // reset retracing flag
                        retracing = false;
                    } else {
                        // otherwise the guard is retracing a previous path
                        retracing = true;
                    }
                    // step right
                    x += 1;
                } else if(retracing && (grid[y+1][x] == '|' || grid[y+1][x] == '+')) { // previous obstacle encountered
                    cout << "looping!" << endl;
                    looping = true;
                    return;
                } else { // new obstacle encountered
                    // turn +90 degrees
                    direction = "down";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "down") { // check if the guard is headed down
                // check that there is no obstacle
                if(grid[y+1][x] != '#' && grid[y+1][x] != 'O') {
                    // check if guard has visited this position before
                    if(grid[y+1][x] == '.'){
                        // drop up/down breadcrumb
                        grid[y+1][x] = '|';
                        // reset retracing flag
                        retracing = false;
                    } else if(grid[y+1][x] == '-'){
                        // paths have crossed, drop intersection breadcrumb
                        grid[y+1][x] = '+';
                        // reset retracing flag
                        retracing = false;
                    } else {
                        // otherwise the guard is retracing a previous path
                        retracing = true;
                    }
                    // step down
                    y += 1;
                } else if(retracing && (grid[y][x-1] == '-' || grid[y][x-1] == '+')) { // previous obstacle encountered
                    cout << "looping!" << endl;
                    looping = true;
                    return;
                } else { // new obstacle encountered
                    // turn +90 degrees
                    direction = "left";
                    // guard must turn, drop intersection breadcrumb first
                    grid[y][x] = '+';
                    // try to move again
                    move(grid);
                }
            } else if (direction == "left") { // check if the guard is headed left
                // check that there is no obstacle
                if(grid[y][x-1] != '#' && grid[y][x-1] != 'O') {
                    // check if guard has visited this position before
                    if(grid[y][x-1] == '.'){
                        // drop left/right breadcrumb
                        grid[y][x-1] = '-';
                        // reset retracing flag
                        retracing = false;
                    } else if(grid[y][x-1] == '|'){
                        // paths have crossed, drop intersection breadcrumb
                        grid[y][x-1] = '+';
                        // reset retracing flag
                        retracing = false;
                    } else {
                        // otherwise the guard is retracing a previous path
                        retracing = true;
                    }
                    // step left
                    x -= 1;
                } else if(retracing && (grid[y-1][x] == '-' || grid[y-1][x] == '+')) { // previous obstacle encountered
                    cout << "looping!" << endl;
                    looping = true;
                    return;
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
            grid[guard.location.second][guard.location.first] = '|';
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

        void placeObstacleAhead(){
            auto& x = guard.location.first;
            auto& y = guard.location.second;

            if(guard.direction == "up"){
                grid[y-1][x] = 'O';
            }
            if(guard.direction == "right"){
                grid[y][x+1] = 'O';
            }
            if(guard.direction == "down"){
                grid[y+1][x] = 'O';
            }
            if(guard.direction == "left"){
                grid[y][x-1] = 'O';
            }
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

    int loops = 0;

    // variables for easy access
    auto& x = lab.guard.location.first;
    auto& y = lab.guard.location.second;
    auto& grid = lab.grid;

    // as long as the guard stays within the lab, keep moving
    while(y > 0 && x > 0 && y < grid.size() - 1 && x < grid[y].size() - 1) {
        Laboratory tempLab = lab;
        auto& tempX = tempLab.guard.location.first;
        auto& tempY = tempLab.guard.location.second;
        auto& tempGrid = tempLab.grid;

        tempLab.placeObstacleAhead();

        while(tempY > 0 && tempX > 0 && tempY < tempGrid.size() - 1 && tempX < tempGrid[tempY].size() - 1) {
            tempLab.guard.move(tempGrid);
            if(tempLab.guard.looping){
                cout << "Guard Looping" << endl;
                loops++;
                break;
            }
        }

        lab.guard.move(grid);
    }

    lab.printMap();

    cout << loops << endl;

    return 0;

    // https://adventofcode.com/2024/day/6#part2
    // ANSWER: ??? (varies with input file)
}