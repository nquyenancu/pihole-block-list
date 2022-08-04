import os

def main():
    seq = 1
    for item in os.listdir():
        if item == '.git':
            continue
        link = '%s: https://raw.githubusercontent.com/nquyenancu/pihole-block-list/main/%s' % (seq, item)
        write_file(link)
        seq+=1

def write_file(text):
    with open('README.md', 'a') as out:
        out.write(text + '\n \n')

main()