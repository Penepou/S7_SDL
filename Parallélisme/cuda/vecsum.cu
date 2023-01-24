/*Copyright (C) 2022 - Pénélope Delabrière, <penelope.delabriere@master-developpement-logiciel.fr>
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.*/

#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <time.h>
#include <string.h>
#include <assert.h>

__global__ void kreduce(float *vec, int size)
{
	int index = threadIdx.x;
	for (int i = size / 2; i > 0; i /= 2)
	{
		if (index < i)
		{
			vec[index] += vec[i + index];
		}
		__syncthreads();
	}
	return;
}

void reduce(float *vec, float *sum, int size)
{
	float *d_vec;
	int bytes = size * sizeof(float);
	cudaMalloc((void **)&d_vec, bytes);
	cudaMemcpy(d_vec, vec, bytes, cudaMemcpyHostToDevice);
	kreduce<<<1, size>>>(d_vec, size);
	cudaMemcpy(sum, d_vec, sizeof(float), cudaMemcpyDeviceToHost);
	cudaFree(d_vec);
	return;
}

int main(int argc, char **argv)
{
	float *vec, *sum;
	int size = 1024, incr;

	vec = (float *)malloc(size * sizeof(float));
	sum = (float *)malloc(size * sizeof(float));

	for (incr = 0; incr < size; incr++)
	{
		vec[incr] = 1.;
	}

	reduce(vec, sum, size);
	for (int i = 0; i < size; i++)
		printf("%f\n", sum[i]);

	free(vec);
	free(sum);
	return;
}

/*
int main(int argc, char **argv){
  if (argc < 2){
	printf("Usage: <filename>\n");
	exit(-1);
  }
  int size;
  float sum[1024];
  float *vec;
  FILE *f = fopen(argv[1],"r");
  fscanf(f,"%d\n",&size);
  size = 1 << size;
  if (size >= (1 << 20)){
	printf("Size (%u) is too large: size is limited to 2^20\n",size);
	exit(-1);
  }
   vec = (float *) malloc(size * sizeof(float)); assert(vec);
  for (int i=0; i<size; i++){
	fscanf(f, "%f\n",&(vec[i]));
  }

  for (int i=0; i<size; i++){
	sum[i]=0.;
  }
  reduce(vec, sum, size);
  printf("sum = %f\n", sum[0]);
  fclose(f);
}*/
