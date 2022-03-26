# Project Title

CVE Extractor and Compiler for Qualyis Search

## Description

Extractcs CVE's from .csv, .json, .txt, plaintext, .pdf, and from URLs. 

## Use Case

Security vendor reports may contain a large list of explioited CVEs from a group. CTI extracts 
these CVEs and searches for vulnerable assets in our network.  

## Getting Started

### Dependencies

* Python3
* BeautifulSoup
* PyPDF2
* Requests

## Install Dependecies

Mac:
If missing python3 (check with python3 --version)
  Install brew if missing:
    /bin/bash -c "$(curl -fsSL 
https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  Install python
    brew install python
  Pip is install with python3 using brew

pip install beautifulsoup4 requests pyPDF2



Windows:
If missing python3 (check with py --version in command line (cmd.exe))
  Download python3: https://www.python.org/downloads/
If missing pip (check with pip --version)
  Download the script for get-pip.py, from https://bootstrap.pypa.io/get-pip.py.
  py get-pip.py

pip install beautifulsoup4 requests pyPDF2


### Executing program

* How to run the program

```
python3 cve_extractor_qualys.py -h

```
Output
```
usage: Extracts CVEs from multiple formats and outputs a Qualys search string. 

 **Example:
 python3 cve_extractor_qualys.py -u https://www.website.com

       [-h] [-t TEXT] [-p PDF] [-u URL]

options:
  -h, --help            show this help message and exit
  -t TEXT, --text TEXT  .csv, .json, or plaintext file
  -p PDF, --pdf PDF     .pdf
  -u URL, --url URL     full url


```


* Example: python3 cve_extractor_qualys.py -u 
"https://www.tenable.com/blog/contileaks-chats-reveal-over-30-vulnerabilities-used-by-conti-ransomware-affiliates"

```
python3 atomic_extractor.py -f -f [~/Relative/path/file] -o [file]

```

Output
```
vulnerabilities.vulnerability.cveIds:[CVE-2018-13379,CVE-2018-13374,CVE-2020-0796,CVE-2020-0609,CVE-2020-0688,CVE-2021-21972,CVE-2021-21985,CVE-2021-22005,CVE-2021-26855,CVE-2015-2546,CVE-2016-3309,CVE-2017-0101,CVE-2018-8120,CVE-2019-0543,CVE-2019-0841,CVE-2019-1064,CVE-2019-1069,CVE-2019-1129,CVE-2019-1130,CVE-2019-1215,CVE-2019-1253,CVE-2019-1315,CVE-2019-1322,CVE-2019-1385,CVE-2019-1388,CVE-2019-1405,CVE-2019-1458,CVE-2020-0638,CVE-2020-0787,CVE-2020-1472,CVE-2021-1675,CVE-2021-1732,CVE-2021-34527,CVE-2021-44228,CVE-2022-23277,CVE-2022-24508]
```

## Authors

Derek Herrington 
[@xploitive](https://twitter.com/xploitive)

## Version History

* 0.1
    * Initial Release
