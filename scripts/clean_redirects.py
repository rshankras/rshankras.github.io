#!/usr/bin/env python3
"""
Clean up duplicate redirects in _redirects file
"""

def clean_redirects_file():
    redirects_file = "/Users/rshankar/Work/MyProjects/rshankras.github.io/_redirects"

    # Read existing redirects
    with open(redirects_file, 'r') as f:
        lines = f.readlines()

    # Separate original redirects from auto-generated ones
    original_redirects = []
    auto_generated = []

    in_auto_generated = False
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            if line == '# Auto-generated 404 fixes':
                in_auto_generated = True
            continue

        if in_auto_generated:
            auto_generated.append(line)
        else:
            original_redirects.append(line)

    # Remove duplicates from auto-generated redirects
    unique_auto_generated = list(set(auto_generated))
    unique_auto_generated.sort()

    # Write cleaned redirects back to file
    with open(redirects_file, 'w') as f:
        # Write original redirects
        for redirect in original_redirects:
            f.write(f"{redirect}\n")

        f.write("\n# Auto-generated 404 fixes (deduplicated)\n")

        # Write unique auto-generated redirects
        for redirect in unique_auto_generated:
            f.write(f"{redirect}\n")

    print(f"Cleaned redirects: removed {len(auto_generated) - len(unique_auto_generated)} duplicates")
    print(f"Final count: {len(original_redirects)} original + {len(unique_auto_generated)} generated = {len(original_redirects) + len(unique_auto_generated)} total redirects")

if __name__ == '__main__':
    clean_redirects_file()
