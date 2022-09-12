PROGRAM = main

SRCS = brianlib/randomkit/randomkit.c code_objects/neurongroup_stateupdater_codeobject.cpp code_objects/statemonitor_1_codeobject.cpp code_objects/statemonitor_2_codeobject.cpp code_objects/statemonitor_codeobject.cpp main.cpp network.cpp objects.cpp run.cpp synapses_classes.cpp
H_SRCS = brianlib/clocks.h brianlib/common_math.h brianlib/dynamic_array.h code_objects/neurongroup_stateupdater_codeobject.h code_objects/statemonitor_1_codeobject.h code_objects/statemonitor_2_codeobject.h code_objects/statemonitor_codeobject.h network.h objects.h run.h synapses_classes.h
OBJS = ${SRCS:.cpp=.o}
OBJS := ${OBJS:.c=.o}
OPTIMISATIONS = -Ibrianlib/randomkit -I/home/ivan/PycharmProjects/SNNoptimization/venv/include -w -O3 -ffast-math -fno-finite-math-only -march=native -std=c++11
CXXFLAGS = -c -Wno-write-strings $(OPTIMISATIONS) -I.  
LFLAGS =  -Lbrianlib/randomkit -L/home/ivan/PycharmProjects/SNNoptimization/venv/lib -Wl,--enable-new-dtags,-R/home/ivan/PycharmProjects/SNNoptimization/venv/lib 
DEPS = make.deps

all: $(PROGRAM)

.PHONY: all clean

$(PROGRAM): $(OBJS) $(DEPS) makefile
	$(CXX) $(OBJS) -o $(PROGRAM) $(LFLAGS)

clean:
	rm $(OBJS) $(PROGRAM) $(DEPS)

make.deps: $(SRCS) $(H_SRCS)
	$(CXX) $(CXXFLAGS) -MM $(SRCS) > make.deps
	
ifneq ($(wildcard $(DEPS)), )
include $(DEPS)
endif

%.o : %.cpp makefile
	$(CXX) $(CXXFLAGS) $< -o $@