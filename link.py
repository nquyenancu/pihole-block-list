import os

def main():
    for item in os.listdir():
        link = 'https://raw.githubusercontent.com/nquyenancu/pihole-block-list/main/%s' % item
        write_file(link)

def write_file(text):
    with open('README.md', 'a') as out:
        out.write(text + '\n \n')

main()