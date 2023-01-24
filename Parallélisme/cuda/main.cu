/*Copyright (C) 2022 - Pénélope Delabrière, <penelope.delabriere@master-developpement-logiciel.fr>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.*/

#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>

__global__ void kreduce(float *d_vec, float *d_sum, int size){
    int index = blockIdx.x*blockDim.x+threadIdx.x;
    for (int i = size / 2; i > 0; i /= 2){
        if( index < i ){
            d_vec[index] += d_vec[index+i];
        }

        __syncthreads();
    }
    if(index == 0){
        d_sum[blockIdx.x] = d_vec[blockIdx.x+threadIdx.x];
    }
}


void reduce(float *vec, float *sum, int size){
    float *d_vec;
    float *d_sum;
    float *d_sum2;
    int bytes = size*sizeof(float);

    cudaMalloc((void **)&d_vec, bytes);
    cudaMalloc((void **)&d_sum, bytes);
    cudaMalloc((void **)&d_sum2, sizeof(float));
    cudaMemcpy(d_vec, vec, bytes, cudaMemcpyHostToDevice);

    kreduce<<<(size+1024-1)/1024, 1024>>>(d_vec, d_sum, size);
    kreduce<<<1, 1024>>>(d_sum, d_sum2, 1024);

    cudaMemcpy(sum, d_sum2, sizeof(float), cudaMemcpyDeviceToHost);
    cudaFree(d_vec);
    cudaFree(d_sum);
    cudaFree(d_sum2);
}

int main(int argc, char **argv){
    int size = 4096;
    float *vec = (float*) malloc(size*sizeof(float));
    float *sum = (float*) malloc(size*sizeof(float));

    for(int i = 0; i < size; i++){
        vec[i] = 1;
    }

    for(int i = 0; i < size; i++){
        sum[i] = 0;
    }

    reduce(vec, sum, size);

    printf("%f", sum[0]);


}
