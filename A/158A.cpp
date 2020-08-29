    #include<iostream>
    #include<cstdio>
    using namespace std;

    int main(){

    int n,k,x,i;
    int c=0;
    int a[50];
    cin>>n>>k;

    for( i=1;i<=n;i++){
        scanf("%d",&a[i]);
    }

    x=a[k];
    i=1;
    fflush(stdin);

    if(x>0){
    while(i<=n&&a[i]>=x){
            c++;
            ++i;
    }
    }

    else{
        while(i<=n&&a[i]>0){
            c++;
            ++i;
    }
    }


    cout<<c<<endl;
    return 0;
    }