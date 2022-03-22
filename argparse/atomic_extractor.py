import pathlib
import argparse
import re


def plaintext_atomic_extractor(path):
    with open(path, 'r') as f:
        text = f.readlines()
        file_text = " ".join(text)
        if args.type == "CVE":
            match_CVE = CVE_re.findall(file_text)
            with open(args.output, 'w') as f:
                for i in match_CVE:
                    f.write(i+"\n")
        elif args.type == "IPV4":
            match_IPV4 = IPV4_re.findall(file_text)
            with open(args.output, 'w') as f:
                for i in match_IPV4:
                    f.write(i+"\n")
        else:
            match_CVE = CVE_re.findall(file_text)
            match_IPV4 = IPV4_re.findall(file_text)
            with open(args.output, 'w') as f:
                for i in match_CVE+match_IPV4:
                    f.write(i+"\n")


IPV4_re = re.compile(
    '(?:(?:25[05]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)')
CVE_re = re.compile('(CVE[0-9]{4}-[0-9]{4,7})')

match_CVE = None
match_IPV4 = None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", type=pathlib.Path,
                        required=True, help=".csv, .json, or .plaintext input")
    parser.add_argument("-o", "--output", type=pathlib.Path,
                        required=True, help="output file location")
    parser.add_argument("-t", "--type", type=str, required=False,
                        choices=("CVE", "IPV4"), help="CVE or IPV4")
    args = parser.parse_args()
    plaintext_atomic_extractor(args.file)
