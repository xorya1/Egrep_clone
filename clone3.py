import sys
import re

def kmp_pattern_search(text, pattern):
    """KMP algorithm for exact pattern matching."""
    def compute_lps_array(pattern):
        # Prepare the longest prefix-suffix (LPS) array for the pattern
        lps = [0] * len(pattern)
        length = 0  # Tracks the length of the previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps_array(pattern)
    i = 0  # Index for text
    j = 0  # Index for pattern

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        # Match found
        if j == m:
            return True  # Just return True if we find a match
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return False  # No match found

def search_in_file(pattern, filename):
    """Search for the pattern in each line of the file using KMP or regex."""
    try:
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                line = line.strip()  # Get rid of any newline characters

                # Check if there are any regex special characters in the pattern
                if re.search(r'[.*+?^${}()|[\]\\]', pattern):
                    # If regex characters are found, use regex search
                    if re.search(pattern, line):
                        print(f"Match found on line {line_number}: '{line}'")  # Show the match
                else:
                    # Use KMP for exact pattern matching
                    if kmp_pattern_search(line, pattern):
                        print(f"Match found on line {line_number}: '{line}'")  # Show the match

                line_number += 1  # Move to the next line

    except FileNotFoundError:
        print(f"Error: Could not open file {filename}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <filename> <pattern>")
        return 1

    filename = sys.argv[1]
    pattern = sys.argv[2]

    search_in_file(pattern, filename)

if __name__ == "__main__":
    main()
