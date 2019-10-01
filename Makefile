all:
	./setup.sh
	mkdir -p build ; cd build ; cmake .. ; make
	build/partitioner
	
clean:
	git clean -dfqX -- .
	
	