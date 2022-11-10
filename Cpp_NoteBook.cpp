#include <cstdio>
#include <algorithm>
using namespace std;
const int SIZE = 1<<18; // 75000*2 이상
typedef pair<int, int> P;
 
// 세그먼트 트리 구조체
struct SegTree{
    int arr[SIZE];
    SegTree(){ fill(arr, arr+SIZE, 0); }
    // n번째 리프 노드를 1 증가시킴
    void inc(int n){
        n += SIZE/2;
        while(n > 0){
            arr[n]++;
            n /= 2;
        }
    }
    // 구간 [s, e)의 합
    int sum(int s, int e){ return sum(s, e, 1, 0, SIZE/2); }
    int sum(int s, int e, int node, int ns, int ne){
        if(e <= ns || ne <= s) return 0;
        if(s <= ns && ne <= e) return arr[node];
        int mid = (ns+ne)/2;
        return sum(s, e, node*2, ns, mid) + sum(s, e, node*2+1, mid, ne);
    }
};
 
int main(){
    int T;
    scanf("%d", &T);
    for(int t=0; t<T; t++){
        SegTree ST;
        int N, range = 0;
        P p[75000];
        scanf("%d", &N);
        for(int i=0; i<N; i++){
            int x, y;
            scanf("%d %d", &x, &y);
            p[i] = P(x, y);
        }
 
        // 점들을 y좌표 순으로 정렬
        sort(p, p+N, [](P &a, P &b){
            return a.second < b.second;
        });
        // 서로 구분되는 y좌표 개수를 세며 y좌표 재설정
        int newY[750000];
        for(int i=0; i<N; i++){
            if(i>0 && p[i].second != p[i-1].second) range++;
            newY[i] = range;
        }
        for(int i=0; i<N; i++)
            p[i].second = newY[i];
        // 점들을 다시 x좌표 순으로, x좌표가 같다면 y좌표가 작아지는 순으로 정렬
        sort(p, p+N, [](P &a, P &b){
            if(a.first == b.first) return a.second > b.second;
            return a.first < b.first;
        });
 
        // 점들을 차례대로 훑으면서 이 점으로 항해할 수 있는 점 개수 세기
        long long result = 0;
        for(int i=0; i<N; i++){
            result += ST.sum(p[i].second, SIZE/2);
            ST.inc(p[i].second);
        }
        // 결과 출력
        printf("%lld\n", result);
    }
}