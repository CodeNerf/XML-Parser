import os
import argparse

banned_words = ['known', '!', 'dupe', 'kown', '(dup)', '?', 'needs work', 'need work', 'needs scale', 'needs scaling', 'need scale', 'need scales', 'need scaling', '*']

def check(filename):
    found = []
    f = open(filename)
    all_lines = f.readlines()
    for i, line in enumerate(all_lines):
        if "<TxMsgs>" in line:
            break
        if "<Description>" in line:
            if "<Signal>" in all_lines[i-1]:
                parsed_line = line.replace("<Description>", "").replace("</Description>", "").strip()
                check_line = parsed_line.lower()
                good = True
                if parsed_line not in found:
                    for word in banned_words:
                        if word in check_line:
                            good = False
                else:
                    good = False
                if good:
                    found.append(parsed_line)

    with open(f'readout_{filename}.txt', 'w+') as f:
        for line in sorted(found):
            print(line)
            f.write(line + '\n')

    print(f"Finished!   Found {len(found)} items")

parser = argparse.ArgumentParser(description="Get a list of VS3 Signals")
parser.add_argument('-file', type=str, nargs=1, help='A .VS3 file')

args = vars(parser.parse_args())

if '.vs3' in (args['file'][0]):
    check(args['file'][0])
else:
    print("Invalid file format")

