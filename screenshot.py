#!/usr/bin/env python3
import argparse
import os
import subprocess


def main():
    parser = argparse.ArgumentParser(description='saves a screenshot of a sublime text window')
    parser.add_argument('-o', '--output-file', help='output image filename')

    args = parser.parse_args()

    os.chdir(os.path.dirname(__file__))

    p = subprocess.run(
        ['xdotool', 'search', '--name', ' - Sublime Text'],
        stdout=subprocess.PIPE,
        universal_newlines=True,
    )
    title = p.stdout.strip()
    p = subprocess.run(
        [
            'gm',
            'import',
            '-crop',
            '800x700+224+43',
            '-window',
            title,
            f'screenshots/{args.output_file}.png',
        ]
    )


if __name__ == '__main__':
    main()
