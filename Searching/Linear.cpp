#include<iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;
int lsort(int *arr,int i, int found);
int main(){
    ifstream text_file("arr.txt");
    string line;
    vector<int> int_array;
    
    
    if(text_file.is_open()){
        getline(text_file,line);
        
        
        int j =0;
        string temp ="";
        
        
        for(int i =0;i<sizeof(line)+5;i++){
            if (line[i]=='{' || line[i]=='}'){
                continue;
            }
            if(line[i]!=','){
                string strDigit(1,line[i]);
                temp +=strDigit;

            }else{
                int_array.push_back(stoi(temp));
                temp="";
                j++;
            }
        }
        
        text_file.close();
    }
    int arr[int_array.size()];
    int i=0;
    for (auto it = int_array.begin(); it != int_array.end();it++) {
        arr[i]=*it;
        i++;
    }
    
    int_array.clear();
    
    cout<<"given no found at index "<<lsort(arr,i-1,22);
    return 0;
}

int lsort(int *arr,int i,int found){
    for(int j= 0 ; j<=i;j++){
        if (arr[j]==found)return j+1;
    }
}