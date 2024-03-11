#include<iostream>
using namespace std;

int b_search(int *arr,int ts);

void sort(int *arr){
    for (int i = 0; i < sizeof(arr)-1; ++i) {
        for (int j = 0; j < sizeof(arr) - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                std::swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int main(){
    int arr[10]={1,23,12,32,22,40,13,87,9,7};

    

    cout<<((b_search(arr,0))?"Founded":"Not Founded")<<endl;
    
    return 0;
}

int b_search(int *arr,int ts){
    sort(arr);

    int left = 0;
    int right = 9;
    while (left <= right) {
        int mid = left + (right - left) / 2;

        if (arr[mid] == ts) {
            return 1;  
        } else if (arr[mid] < ts) {
            left = mid + 1;  
        } else {
            right = mid - 1;  
        }
    }
    return 0;
}