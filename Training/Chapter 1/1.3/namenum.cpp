/*
ID: Christo97
TASK: namenum
LANG: C++                 
*/

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ifstream fin("namenum.in");
    ofstream fout("namenum.out");
    ifstream dict("dict.txt");
    string number;
    fin >> number;
    vector<string> valid;
    string word;
    while (dict >> word) {
        if (word.length() == number.length()) {
            bool valid_word = true;
            for (int i = 0; i < word.length(); i++) {
                if (word[i] == 'Q' || word[i] == 'Z') {
                    valid_word = false;
                    break;
                }
                if (word[i] == 'A' || word[i] == 'B' || word[i] == 'C') {
                    if (number[i] != '2') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'D' || word[i] == 'E' || word[i] == 'F') {
                    if (number[i] != '3') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'G' || word[i] == 'H' || word[i] == 'I') {
                    if (number[i] != '4') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'J' || word[i] == 'K' || word[i] == 'L') {
                    if (number[i] != '5') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'M' || word[i] == 'N' || word[i] == 'O') {
                    if (number[i] != '6') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'P' || word[i] == 'R' || word[i] == 'S') {
                    if (number[i] != '7') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'T' || word[i] == 'U' || word[i] == 'V') {
                    if (number[i] != '8') {
                        valid_word = false;
                        break;
                    }
                } else if (word[i] == 'W' || word[i] == 'X' || word[i] == 'Y') {
                    if (number[i] != '9') {
                        valid_word = false;
                        break;
                    }
                }
            }
            if (valid_word) {
                valid.push_back(word);
            }
        }
    }
    if (valid.size() == 0) {
        fout << "NONE" << endl;
    } else {
        sort(valid.begin(), valid.end());
        for (int i = 0; i < valid.size(); i++) {
            fout << valid[i] << endl;
        }
    }
    return 0;
}