Here's an edited README that includes explanations for both the C and Python implementations of your regular expression matcher:

# DAAR Project 1 - Regular Expression Matcher

## Overview

This project implements basic regular expression (RegEx) matching in both C and Python, designed to search for patterns in text files. The matcher supports the following RegEx features:

- **Concatenation**: e.g., `abc` matches the string `abc`
- **Alternation (|)**: e.g., `a|b` matches either `a` or `b`
- **Star (*) operator**: e.g., `a*` matches zero or more occurrences of `a`
- **Period (.)**: Matches any single character
- **Parantese()**.


The project has been tested on Windows.

## Requirements

- **For C Implementation**: GCC (for compiling the source code on Windows)
- **For Python Implementation**: Python 3.x
- Example test files are provided in the `Test_Files` directory.

## Compilation (C Implementation)

To compile the C project using GCC, navigate to the root directory and run the following command:


gcc -o daarproject1.exe source_code/daarproject1.c


This will produce an executable named `daarproject1.exe`.

## Running the C Program

Once compiled, you can run the C program by providing a text file and a RegEx pattern.

### Command Syntax:


daarproject1.exe <input_file> "<pattern>"


### Example 1:
Using the test file `input.txt` with a pattern that matches variations of "sargon":


daarproject1.exe Test_Files/input.txt "s(a|g)*on"


### Expected Output:
Given the following text in `input.txt`:

```
s,zpdpd
he*llo
abc123
a.b.c
alpha and omega
aaabbbccc
12345
sargon is the best
saraon
saraon
sarsargon another time
sargon isn't alive
sargon sargon sargoner
sargona
saegon
sgon
```

The output will be:

```
Match found on line 8: sargon is the best
Match found on line 11: sarsargon another time
Match found on line 12: sargon isn't alive
Match found on line 13: sargon sargon sargoner
Match found on line 14: sargona
Match found on line 15: saegon
Match found on line 16: sgon
```

### Example 2:
Using the `TextFileFromDB.txt` obtained from the **Gutenberg Project**:


daarproject1.exe Test_Files/TextFileFromDB.txt ".(ion|ed)"


### Expected Output:

```
Match found on line 1943: the intention (which he later abandoned) of giving it verbal expression.
Match found on line 3258: are acquainted); or, "that reminds me of something that happened
Match found on line 15894: phrase “Project Gutenberg” is associated) is accessed, displayed,
```

## Python Implementation

In addition to the C implementation, a Python version of the matcher is provided for ease of use and rapid development.

### Running the Python Program

To run the Python matcher, use the following command syntax:


python clone3.py <input_file> "<pattern>"


### Example Command:
To match variations of "sargon":


python clone3.py Test_Files/input.txt "s(a|g)*on"


### Expected Output:
The output will indicate the number of matches found and average execution time, similar to the C implementation.

## Test Files

Several test files are available in the `Test_Files` directory for testing both implementations, including:

- `input.txt`: A file with sample patterns to match variations of "sargon."
- `TextFileFromDB.txt`: A file obtained from the **Gutenberg Project** for broader testing.

### Example Test Command for Python:


python clone3.py Test_Files/input.txt "s(a|g)*on"


This will search `input.txt` for all lines that match patterns similar to "sargon."

## Notes

- Ensure that the `daarproject1.exe` file and the test files are in the same working directory, or provide the full path to the test files when running the C program.
- The matcher supports only basic regular expressions, as described in the **Overview** section.

The above commands will search for patterns in the respective text files and output matching lines.

