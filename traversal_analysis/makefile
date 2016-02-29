all: x_vector_reuse

vim:
	vim -p makefile delta_analysis.py delta_bits.cpp TODO x_vector_reuse.cpp analysis.py

delta_bits: delta_bits.cpp
	g++ -std=c++11 -O3 -o delta_bits delta_bits.cpp

x_vector_reuse: x_vector_reuse.cpp
	g++ -std=c++11 -O3 -o x_vector_reuse x_vector_reuse.cpp

run: delta_bits
	delta_bits example.mtx 2 2

matrices.zip:
	wget http://www.nvidia.com/content/NV_Research/matrices.zip
