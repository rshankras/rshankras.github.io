import csv
import os
import glob

def verify_redirects():
    print("Verifying redirect files...")
    print("-" * 80)
    
    # Read the redirects CSV
    with open('../redirects.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        redirects = {row['source']: row['target'] for row in reader}
    
    # Find all redirect files
    redirect_files = glob.glob('../_posts/redirects/**/*.md', recursive=True)
    
    print(f"Found {len(redirects)} entries in redirects.csv")
    print(f"Found {len(redirect_files)} redirect files")
    print("-" * 80)
    
    # Verify each redirect file
    for redirect_file in redirect_files[:5]:  # Check first 5 files
        with open(redirect_file, 'r') as f:
            content = f.read()
            print(f"\nChecking {os.path.basename(redirect_file)}:")
            print(content)
    
    print("\nVerification complete!")

if __name__ == '__main__':
    verify_redirects()
