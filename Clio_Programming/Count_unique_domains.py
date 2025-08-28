# Problem Statement:
# Imagine you're building an internal analytics tool. You're given a file that contains one domain name per line, like this:
# Your task is to write a function that reads the file and returns the number of unique domains, ignoring any subdomains.
# So for the above input, the correct output would be: 2
# (clio.com and clio.ca)

def count_domains(logfile):
    unique_domains = set()   # using set to store unique domains



    with open(logfile, 'r') as f:
        for line in f:
            line = line.strip().lower()
            if not line: continue
            parts = line.split(".")
            if len(parts) >= 2:
                base_domain = parts[-2] + "." + parts[-1]
                unique_domains.add(base_domain)

    return len(unique_domains)


# Time Complexity:
# O(n), where n = number of lines in the file
# Space Complexity:
# O(d), where d = number of unique domains

# Example usage:
logfile = r"C:\Users\Gurekam\Desktop\University of Windsor\HCLcoding\Clio_Programming\domains.txt"
print(count_domains(logfile))  # Output: 3