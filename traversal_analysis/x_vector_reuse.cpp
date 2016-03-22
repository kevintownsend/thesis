#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <map>

using namespace std;

typedef unsigned long long ull;

int main(int argc, char* argv[]){
    if(argc != 3){
        cerr << "Usage: " << argv[0] << " matrix.mtx" << endl;
        exit(1);
    }
    FILE* inputFile = fopen(argv[1], "r");
    char line[1000];
    fgets(line, 1000, inputFile);
    bool pattern = false;
    bool symmetric = false;
    if(string(line).find("pattern") != string::npos)
        pattern = true;
    if(string(line).find("symmetric") != string::npos)
        symmetric = true;
    ull height, width, nnz;
    fscanf(inputFile, "%lld%lld%lld", &height, &width, &nnz);
    map<ull, map<ull, map<ull, double> > > rcMap;
    int subHeight = atoi(argv[2]);
    for(ull i = 0; i < nnz; ++i){
        ull tmp0, tmp1;
        double tmp2 = 1.0;
        if(pattern)
            fscanf(inputFile, "%lld%lld", &tmp0, &tmp1);
        else
            fscanf(inputFile, "%lld%lld%llf", &tmp0, &tmp1, &tmp2);
        tmp0--; tmp1--;
        rcMap[tmp0 / subHeight][tmp1][tmp0 % subHeight] = tmp2;
        if(symmetric)
            rcMap[tmp1 / subHeight][tmp0][tmp1 % subHeight] = tmp2;
    }
    ull count = 0;
    ull trueNnz = 0;
    for(auto it0 = rcMap.begin(); it0 != rcMap.end(); ++it0){
        for(auto it1 = it0->second.begin(); it1 != it0->second.end(); ++it1){
            count++;
            for(auto it2 = it1->second.begin(); it2 != it1->second.end(); ++it2){
                trueNnz++;
            }
        }
    }
    cout << count << ", " << trueNnz << ", " << width << endl;
}
