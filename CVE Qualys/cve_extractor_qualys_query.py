# Extracts CVE #s and generates Qualys search string
import argparse
import pathlib
import re
import requests
from bs4 import BeautifulSoup
import PyPDF2

# Matches CVE regex of a .txt, .csv, .json, or other plain text files


def qualyis_extractor_text(path):
    with open(path, 'r') as f:
        text = f.readlines()
        file_text = " ".join(text)
        match_CVE = CVE_re.findall(file_text)
        qualyis_compiler(match_CVE)

# Matches CVE regular expression of a .pdf


def qualyis_extractor_pdf(path):
    pdfFileObject = open(path, "rb")
    pdfReader = PyPDF2.PdfFileReader(pdfFileObject)
    count = pdfReader.numPages
    output = ''
    for i in range(count):
        page = pdfReader.getPage(i)
        output += page.extractText()
    match_CVE = CVE_re.findall(output)
    qualyis_compiler(match_CVE)

# Matches CVE regular expression of a parsed URl page


def qualyis_extractor_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    match_CVE = soup.find_all(text=CVE_re)
    qualyis_compiler(match_CVE)


# filters, removes duplicates, and formats CVE matches
def qualyis_compiler(match):
    match = [i for i in match if CVE_re.match(i)]
    match = list(set(match))
    text_match = ','.join(str(i) for i in match)
    print("vulnerabilities.vulnerability.cveIds:["+text_match+"]")


# CVE regex pattern
CVE_re = re.compile('(CVE-[0-9]{4}-[0-9]{4,7})')

# List of matching results
match_CVE = []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Extract CVEs &or IPs from/to plaintext. \n\n **Example:\n python3 atomic_extractor.py -f Myfile -o NewFile\n\n")
    parser.add_argument("-t", "--text", type=pathlib.Path,
                        required=False, help=".csv, .json, or plaintext file")
    parser.add_argument("-p", "--pdf", type=pathlib.Path,
                        required=False, help=".pdf")
    parser.add_argument("-u", "--url", type=str,
                        required=False, help="full url")

    args = parser.parse_args()
    if args.text is not None:
        qualyis_extractor_text(args.text)
    elif args.pdf is not None:
        qualyis_extractor_pdf(args.pdf)
    elif args.url is not None:
        qualyis_extractor_url(args.url)
    else:
        print("You must choose an input: -t, -p, or -u. Use -h or --help for more.")
