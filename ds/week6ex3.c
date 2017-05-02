#include <stdio.h>
int main(){
    int nodes;
    int edges;
    int node_1;
    int node_2;
    scanf("%d %d", &nodes, &edges);
    for (int i=0; i<edges; i++) {
        scanf("%d %d", &node_1, &node_2);
    }
}

typedef struct GNode *PtrToGNode;
struct GNode {
    int Nv;
    int Ne;
    AdjList G;
};

typedef PtrToGNode LGraph;

typedef struct Vnode {
    PtrToAdjVNode FirstEdge;
} AdjList[MaxVertexNum]

typedef struct AdjVNode *PtrToAdjVNode;
struct AdjVNode {
    int AdjV;
    PtrToAdjVNode Next;
}
