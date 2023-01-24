// -----------------------------------------------------------
// (C) 2022 Pénélope Delabrière, Toulouse, France
// Released under GNU Affero General Public License v3.0 (AGPLv3)
// -----------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>


int main(int argc, char** argv){
    int size = 1024;
    float* vec = calloc(size, size*sizeof(float));
    float* sum;
    reduce(vec, sum, size);
    
    return;
}

void reduce ( float * vec , float *sum , int size ) {
    float * d_vec ;
    int bytes = size * sizeof ( float ) ;
    cudaMalloc (( void **) & d_vec , bytes ) ;
    cudaMemcpy ( d_vec , vec , bytes , cudaMemcpyHostToDevice ) ;
    kreduce < < <1 , size > > >( d_vec , size ) ;
    cudaMemcpy (sum , d_vec , sizeof ( float ) , cudaMemcpyDeviceToHost ) ;
    cudaFree ( d_vec ) ;
}

__global__
void kreduce(float* vec, int size){
    int index = threadIdx.x;
    for(int i = size/2;i>0;i/=2){
        if(index<i){
            vec[index]+=vec[i+index];
        }
        __syncthreads();
    }
    return;
}
