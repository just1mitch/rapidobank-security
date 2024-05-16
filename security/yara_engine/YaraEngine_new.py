import yara
import os
import vt
import json
from pathlib import Path
import sys
import hashlib
from cryptography.include.hashes.md5 import MD5


class YaraEngine:
    def __init__(self, rule_directories: list[str], virus_total_key=None):
        self.rules = {}

        for directory in rule_directories:
            yara_files = [f for f in os.listdir(directory) if f.endswith('.yar') or f.endswith('.yara')]
            for yara_file in yara_files:
                file_path = os.path.join(directory, yara_file)
                self.rules[yara_file] = yara.compile(filepath=file_path)

        self.virus_total_key = virus_total_key
    
    def scan(self, path: str) -> list:
        matching_rules = []
        for i, rule in enumerate(self.rules):
            matches = self.rules[rule].match(filepath=path)
            if matches:
                return True
        return False
    
    
    # Uses VirusTotal API to scan a malicious file passed by file_path
    async def virus_total_scan(self, file_path):
        print(f"\nGetting scan results for {file_path} (may take up to 5 minutes)")
        # See if file has been scanned recently - if so, use that info instead
        #hash = md5_hash_file(file_path)
        client = vt.Client(self.virus_total_key)
        with open(file_path, "rb") as f:
            result = await client.scan_file_async(f)
            print(result)
        return 1


def md5_hash_file(file_path):
    """Calculate the MD5 hash of a file."""
    hasher = hashlib.md5()
    with open(file_path, "rb") as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()