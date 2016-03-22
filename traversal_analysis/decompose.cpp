#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <vector>
#include <map>
#include <math.h>
#include <string>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;

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
    map<ull, map<ull, double> > rMap;
    for(ull i = 0; i < nnz; ++i){
        ull tmp0, tmp1;
        double tmp2 = 1.0;
        if(pattern)
            fscanf(inputFile, "%lld%lld", &tmp0, &tmp1);
        else
            fscanf(inputFile, "%lld%lld%llf", &tmp0, &tmp1, &tmp2);
        tmp0--; tmp1--;
        rMap[tmp0][tmp1] = tmp2;
        if(symmetric)
            rMap[tmp1][tmp0] = tmp2;
    }

    ull newlines = 0;
    ull newNnz = 0;
    vector<int> compressedRow;
    vector<int> col;
    vector<int> row;
    vector<double> val;
    for(auto it0 = rMap.begin(); it0 != rMap.end(); ++it0){
        for(auto it1 = it0->second.begin(); it1 != it0->second.end(); ++it1){
            row.push_back(it0->first);
            col.push_back(it1->first);
            val.push_back(it1->second);
            newNnz++;
        }
        newlines++;
        compressedRow.push_back(newNnz);
    }
    string matrixName(argv[1]);
    matrixName = matrixName.substr(0, matrixName.find_last_of("."));
    FILE* outputFile = fopen((matrixName + ".row").c_str(), "wb");
    fwrite(&row[0], sizeof(int), row.size(), outputFile);
    fclose(outputFile);

    outputFile = fopen((matrixName + ".col").c_str(), "wb");
    fwrite(&col[0], sizeof(int), col.size(), outputFile);
    fclose(outputFile);

    outputFile = fopen((matrixName + ".val").c_str(), "wb");
    fwrite(&val[0], sizeof(double), val.size(), outputFile);
    fclose(outputFile);

    outputFile = fopen((matrixName + ".compressedRow").c_str(), "wb");
    fwrite(&compressedRow[0], sizeof(int), compressedRow.size(), outputFile);
    fclose(outputFile);


    //fopen(string(argv[1])
}
