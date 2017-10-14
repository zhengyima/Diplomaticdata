#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int martrixs[81000][81000]={0};
//int id2count[81000] = {0};
int main() {
    martrixs[80000][80000] = 1;
    ifstream file("CSV/rs4.csv");
    int cnt = 0;
    while(!file.eof()){
        string str;
        int id1;
        int id2;
        getline(file,str,',');
        id1 = atoi(str.c_str());
        getline(file,str,',');
        getline(file,str,',');
        id2 = atoi(str.c_str());
        martrixs[id1][id2] += 1;
        //cout<<id1<<" "<<" "<<id2<<"  "<<martrixs[id1][id2];
        getline(file,str,'\n');
        cnt ++;
        //cout<<cnt<<endl;

    }
    file.close();
    /*
    ifstream file2("nodes_total_count.csv");
    cnt = 0;
    if(file2.peek()){
        cout<<"file2 is empty"<<endl;
    }
    cout<<"read1"<<endl;

    while(!file2.eof()){
        string str;
        int id;
        int count;
        getline(file2,str,',');
        id = atoi(str.c_str());
        getline(file2,str,'\n');
        count = atoi(str.c_str());
        if(id==0&&count==0) break;
        id2count[id] = count;
        //cout<<id<<"___"<<count<<endl;
        cnt ++;
    }
    file2.close();
    cout<<"read2"<<endl;
    //std::cout << martrixs[7818][20408]<< std::endl;
    */
    ofstream ofile("CSV/rsout_test.csv");
    int val;
    for(int i=0;i<4;i++){
        for(int j=i+1;j<80785;j++){
            val = martrixs[i][j] + martrixs[j][i];
            if(val!=0)
            //ofile<<i<<","<<(val+0.0)/(id2count[i]*id2count[j])\<<","<<j<<",CALL"<<endl;
            ofile<<i<<","<<val+0.0<<","<<j<<",CALL"<<endl;
        }
        cout<<i<<endl;
    }
    ofile<<endl;
    ofile.close();
    return 0;
}