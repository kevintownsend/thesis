all: kourtis x_vector_reuse_cache_line cvbv delta_distribution decompose

vim:
	vim -p makefile delta_distribution.py decompose.cpp kourtis.cpp cvbv.cpp related_compression.py x_vector_reuse_cache_line.cpp cache_analysis.py 

kourtis: kourtis.cpp
	g++ -std=c++11 -O3 -o kourtis kourtis.cpp

delta_bits: delta_bits.cpp
	g++ -std=c++11 -O3 -o delta_bits delta_bits.cpp

x_vector_reuse: x_vector_reuse.cpp
	g++ -std=c++11 -O3 -o x_vector_reuse x_vector_reuse.cpp

x_vector_reuse_cache_line: x_vector_reuse_cache_line.cpp
	g++ -std=c++11 -O3 -o x_vector_reuse_cache_line x_vector_reuse_cache_line.cpp

cvbv: cvbv.cpp
	g++ -std=c++11 -O3 -o cvbv cvbv.cpp

run2:
	delta_distribution.py

run: decompose
	decompose example.mtx

matrices.zip:
	wget http://www.nvidia.com/content/NV_Research/matrices.zip

delta_distribution:
	g++ -std=c++11 -O3 -o delta_distribution delta_distribution.cpp

decompose: decompose.cpp
	g++ -std=c++11 -O3 -o decompose decompose.cpp
