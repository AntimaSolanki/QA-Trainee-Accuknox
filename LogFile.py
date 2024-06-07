import re
from collections import Counter

def analyze_logs(log_file_path):
    ip_regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    status_code_regex = r' (\d{3}) '
    requested_page_regex = r'\"(GET|POST) ([^\s]+)'

    total_requests_count = 0
    error_404_count = 0
    page_requests = Counter()
    ip_address_requests = Counter()

    with open(log_file_path, 'r') as file:
        for line in file:
            total_requests_count += 1
            ip_address = re.search(ip_regex, line).group()
            status_code = re.search(status_code_regex, line).group(1)
            requested_page = re.search(requested_page_regex, line).group(2)

            if status_code == '404':
                error_404_count += 1

            page_requests[requested_page] += 1
            ip_address_requests[ip_address] += 1

    print(f'Total requests: {total_requests_count}')
    print(f'404 Errors: {error_404_count}')
    print('\nMost requested pages:')
    for page, count in page_requests.most_common(5):
        print(f'{page}: {count} requests')
    print('\nIP addresses with the most requests:')
    for ip_address, count in ip_address_requests.most_common(5):
        print(f'{ip_address}: {count} requests')

def main():
    log_file_path = '/path/to/access.log'
    analyze_logs(log_file_path)

if __name__ == "__main__":
    main()
