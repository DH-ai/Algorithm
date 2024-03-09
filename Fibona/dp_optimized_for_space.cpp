#include<iostream>


using namespace std;
int fib(int n){
    int a =0,b=1,c;
    if (n==0)return 0;
    for (int i =2;i<=n;i++){
        c=a+b;
        a=b;
        b=c;
    }
    return b;
}

int main(){
    int n ;cin>>n;
    cout<<fib(n);
    return 0;
}