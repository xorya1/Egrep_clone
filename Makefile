# Compiler
CC = gcc

# Compiler flags
CFLAGS = -Wall -g

# Target executable name
TARGET = daarproject1

# Source file
SRC = source_code/daarproject1.c

# Build the project
all: $(TARGET)

# Rule to build the executable
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) -o $(TARGET) $(SRC)

# Clean the generated files
clean:
	rm -f $(TARGET) *.o

# Run the program with an example file and regex pattern
run:
	./$(TARGET) example.txt "(a|b)*"

# For Windows, you might need to use this instead of './' in the run command
run_win:
	$(TARGET).exe example.txt "(a|b)*"
