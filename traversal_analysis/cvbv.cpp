#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
ull nibbleCount(ull delta);

int main(int argc, char* argv[]){
    if(argc != 2){
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
    map<ull, map<ull, map<ull, map<ull, double> > > > rcrMap;
    int subHeight = 512;
    int subWidth = 8;
    for(ull i = 0; i < nnz; ++i){
        ull tmp0, tmp1;
        double tmp2 = 1.0;
        if(pattern)
            fscanf(inputFile, "%lld%lld", &tmp0, &tmp1);
        else
            fscanf(inputFile, "%lld%lld%llf", &tmp0, &tmp1, &tmp2);
        tmp0--; tmp1--;
        rcrMap[tmp0 / subHeight][tmp1 / subWidth][tmp0 % subHeight][tmp1 % subWidth] = tmp2;
        if(symmetric)
            rcrMap[tmp1 / subHeight][tmp0 / subWidth][tmp1 % subHeight][tmp0 % subWidth] = tmp2;
    }
    vector<ull> deltas;

    ll lastDelta = -1;
    ll currDelta = -1;
    ull newlines = 0;
    ull newNnz = 0;
    for(auto it0 = rcrMap.begin(); it0 != rcrMap.end(); ++it0){
        for(auto it1 = it0->second.begin(); it1 != it0->second.end(); ++it1){
            for(auto it2 = it1->second.begin(); it2 != it1->second.end(); ++it2){
                for(auto it3 = it2->second.begin(); it3 != it2->second.end(); ++it3){
                    currDelta = it1->first * subHeight * subWidth + it2->first * subWidth + it3->first;
                    deltas.push_back(currDelta - lastDelta);
                    //cerr << "delta: " << (currDelta - lastDelta - 1) << endl;
                    lastDelta = currDelta;
                    newNnz++;
                }
            }
        }
        lastDelta = -1;
        newlines++;
    }
    ull totalBitSize = 0;
    ull nonzero = 0;
    for(int i = 0; i < deltas.size(); ++i){
        if(deltas[i] == 1){
            nonzero++;
        }else{
            if(nonzero){
                totalBitSize += 4 + 4 * nibbleCount(nonzero);
            }
            totalBitSize += 4 + 4 * nibbleCount(deltas[i]);
            nonzero = 0;
        }
    }
    if(nonzero){
        totalBitSize += 4 + 4 * nibbleCount(nonzero);
    }
    cout << totalBitSize << ", " << newNnz << endl;
}

ull nibbleCount(ull delta){
    int ret = 0;
    while(delta){
        delta >>= 4;
        ret++;
    }
    return ret;
}
