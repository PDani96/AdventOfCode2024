#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void move(string &direction, int &x, int &y, vector<string> &map, int &breadcrumbs) {
    if (direction == "up") {
        if(map[y-1][x] != '#') {
            // check if there is already a breadcrumb
            if(map[y-1][x] != 'X'){
                // drop breadcrumb
                map[y-1][x] = 'X';
                breadcrumbs += 1;
            }
            // step up
            y -= 1;
        } else {
            // turn +90 degrees
            direction = "right";
            // try to move again
            move(direction, x, y, map, breadcrumbs);
        }
    } else if (direction == "right") {
        if(map[y][x+1] != '#') {
            // check if there is already a breadcrumb
            if(map[y][x+1] != 'X'){
                // drop breadcrumb
                map[y][x+1] = 'X';
                breadcrumbs += 1;
            }
            // step right
            x += 1;
        } else {
            // turn +90 degrees
            direction = "down";
            // try to move again
            move(direction, x, y, map, breadcrumbs);
        }
    } else if (direction == "down") {
        if(map[y+1][x] != '#') {
            // check if there is already a breadcrumb
            if(map[y+1][x] != 'X'){
                // drop breadcrumb
                map[y+1][x] = 'X';
                breadcrumbs += 1;
            }
            // step down
            y += 1;
        } else {
            // turn +90 degrees
            direction = "left";
            // try to move again
            move(direction, x, y, map, breadcrumbs);
        }
    } else if (direction == "left") {
        if(map[y][x-1] != '#') {
            // check if there is already a breadcrumb
            if(map[y][x-1] != 'X'){
                // drop breadcrumb
                map[y][x-1] = 'X';
                breadcrumbs += 1;
            }
            // step left
            x -= 1;
        } else {
            // turn +90 degrees
            direction = "up";
            // try to move again
            move(direction, x, y, map, breadcrumbs);
        }
    }
}

int main() {
    // read file
    ifstream file("map.txt");

    // place holder for each line of data read in
    string line;
    // place holder coordinates for guard location
    int x = 0;
    int y = 0;
    // initialize breadcrumb counter
    int breadcrumbs = 0;
    // vector of strings to store file contents
    vector<string> map;

    // collect all lines of data into one map vector
    while(getline(file, line)) {
        // record the current line
        map.push_back(line);

        // check if the guard is on this line
        if(line.find('^') != string::npos) {
            // save x-coordinate of guard
            x = line.find('^');
            // save y-coordinate of guard
            y = map.size() - 1;
            // drop breadcrumb
            map[y][x] = 'X';
            breadcrumbs += 1;
        }
    }

    // close file
    file.close();

    // set guard's initial direction
    string direction = "up";

    while(y > 0 && x > 0 && y < map.size() - 1 && x < map[y].size() - 1) {
        move(direction, x, y, map, breadcrumbs);
    }

    // print map
    // for(string line : map) {
    //     cout << line << endl;
    // }

    // print breadcrumb count
    cout << "Breadcrumbs: " << breadcrumbs << endl;

    return 0;

    // https://adventofcode.com/2024/day/6
    // ANSWER: 4663 (varies with input file)
}