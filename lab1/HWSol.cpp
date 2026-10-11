// Sean Beckford
#include <iostream>
using namespace std;

bool M1(string input) {
    const int s = 0;
    const int delta[5][2] {{1, 3}, {1, 2}, {2, 2}, {4, 2}, {2, 4}};
    const bool W[5] = {false, true, false, false, true};
    int state = s;
    for (int i = 0; i < input.length(); i++) {
        char cindex = input[i] - 'a';
        state = delta[state][cindex];
    }
    return W[state];
}

int main() {
    string str;
    cin >> str;

    cout << (M1(str) ? "accept" : "reject") << endl;

    return 0;
}