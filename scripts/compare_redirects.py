import csv
import os
from collections import defaultdict

def read_csv_redirects(file_path):
    redirects = set()
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Get source URL without domain and trailing slash
                source = row.get('source', '').replace('http://blogmines.com', '').strip('/')
                redirects.add(source)
    return redirects

def analyze_redirection_log(file_path):
    redirect_counts = defaultdict(int)
    unique_redirects = set()
    total_entries = 0
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_entries += 1
                source = row.get('source', '').replace('http://blogmines.com', '').strip('/')
                redirect_counts[source] += 1
                unique_redirects.add(source)
    
    return total_entries, len(unique_redirects), redirect_counts

def compare_redirects():
    # Read redirects.csv
    redirects_csv = read_csv_redirects('../redirects.csv')
    
    # Analyze redirection-log.csv
    total_log_entries, unique_log_redirects, log_counts = analyze_redirection_log('../redirection-log.csv')
    
    # Find missing redirects
    missing_redirects = set()
    for source in log_counts.keys():
        if source not in redirects_csv:
            missing_redirects.add(source)
    
    # Print statistics
    print(f"Statistics:")
    print(f"1. redirects.csv:")
    print(f"   - Total unique redirects: {len(redirects_csv)}")
    print(f"\n2. redirection-log.csv:")
    print(f"   - Total entries: {total_log_entries}")
    print(f"   - Unique redirects: {unique_log_redirects}")
    
    print(f"\n3. Missing redirects count: {len(missing_redirects)}")
    
    if missing_redirects:
        print("\nMissing redirects (with hit counts):")
        for redirect in sorted(missing_redirects):
            print(f"  {redirect}: {log_counts[redirect]} hits")
            
    # Print top accessed redirects
    print("\nTop 10 most accessed redirects:")
    sorted_redirects = sorted(log_counts.items(), key=lambda x: x[1], reverse=True)
    for source, count in sorted_redirects[:10]:
        print(f"  {source}: {count} hits")

if __name__ == '__main__':
    compare_redirects()
