# libSSH-bypass
Implementation of CVE-2018-10933 // but with a CIDR block scanner.

Didn't feel like spending $$ on Shodan's API, so i've added a range scanner that dumps vuln servers into a file with a soft scan.  

you'll need to pip install paramiko as a dependency.

this is an early PoC version, I'll later branch of @blackbunny's to add the range scanner.
