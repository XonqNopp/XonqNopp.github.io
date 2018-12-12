#!/usr/bin/env python3
"""
Fix build of pelican to use only one repo for both source and generated files.
"""
import os


def main():
    """
    Main function
    """
    for dirpath, dirnames, filenames in os.walk('output'):
        for filename in filenames:
            fullname = os.path.join(dirpath, filename)
            if filename.endswith('.html'):
                with open(fullname, 'r') as fileReader:
                    data = fileReader.read()

                with open(fullname, 'w') as fileWriter:
                    for line in data.split('\n'):
                        fileWriter.write(line.replace('"/', '"/output/') + '\n')


if __name__ == '__main__':
    main()

