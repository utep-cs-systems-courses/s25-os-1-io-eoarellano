import os
import re
import sys

def word_count(input_file, output_file):

    # Open the input file for reading
    fd_in = os.open(input_file, os.O_RDONLY)
    file_size = os.path.getsize(input_file)
    content = os.read(fd_in, file_size).decode('utf-8')
    os.close(fd_in)

    # Extract words from the content
    words = re.findall(r'\b\w+\b', content.lower())

    # Count words
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

     #Sort words alphabetically
    sorted_words = sorted(word_counts.items(), key=lambda x: x[0])

    # Open the output file for writing 
    fd_out = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o644)

    # Write results to the output file
    for word, count in sorted_words:
        line = f"{word} {count}\n"
        os.write(fd_out, line.encode('utf-8'))

    os.close(fd_out)

if __name__ == "__main__":
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    word_count(input_file, output_file)