import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import argparse

def parse_args():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='网页爬虫')
    parser.add_argument("-u", "--url", help="要爬取的网站", required=False)
    parser.add_argument("-f", "--file", help="包含URL的输入文件", required=False)
    parser.add_argument("-o", "--output", help="输出文件", required=False)
    parser.add_argument("-d", "--deep", help="深度查找", action="store_true")
    return parser.parse_args()

def extract_and_concatenate_hrefs(base_url):
    # 从给定的URL提取并拼接超链接
    try:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.content, 'html.parser')
        hrefs = [link.get('href') for link in soup.find_all('a') if link.get('href')]
        full_urls = [urljoin(base_url, href) for href in hrefs]
        return full_urls
    except requests.RequestException as e:
        print(f"请求 {base_url} 时出错: {e}")
        return []

def deep_crawl(base_url, visited=None):
    # 深度爬取
    if visited is None:
        visited = set()
    try:
        links = extract_and_concatenate_hrefs(base_url)
        for link in links:
            if link not in visited:
                visited.add(link)
                print(link)
                if len(visited) < 50:  # 限制爬取数量
                    deep_crawl(link, visited)
    except Exception as e:
        print(f"深度爬取时出错: {e}")

def read_urls_from_file(file_path):
    # 从文件中读取URL
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def write_to_file(file_path, data):
    # 将数据写入文件
    with open(file_path, 'w') as file:
        for item in data:
            file.write("%s\n" % item)

def main():
    args = parse_args()
    all_links = []

    if args.file:
        urls = read_urls_from_file(args.file)
        for url in urls:
            if args.deep:
                deep_crawl(url, set(all_links))
            else:
                links = extract_and_concatenate_hrefs(url)
                all_links.extend(links)
    elif args.url:
        if args.deep:
            deep_crawl(args.url, set(all_links))
        else:
            all_links = extract_and_concatenate_hrefs(args.url)

    if args.output:
        write_to_file(args.output, all_links)
    else:
        for link in all_links:
            print(link)

if __name__ == "__main__":
    main()
