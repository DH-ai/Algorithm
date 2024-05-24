#include <iostream>
#include <vector>
#include <set>
using namespace std;
int main(){
    int n = 2322024;
    int m = 20232023;
    
    set<int> xor_set;
    int k =0^n;
    xor_set.insert(k);
    // xor_set.
    cout<<k<<endl;
    for( int i =1;i<=m;i++){
        int ans =n^i;
        // cout<<"n "<<char(10754)<<" i = "<<ans<<endl;
        xor_set.insert(ans);
    }
    
    // for (auto it =xor_set.begin();it!=xor_set.end();it++){
        
    // }
            
        
        
    // cout<<k;
    return 0;
}