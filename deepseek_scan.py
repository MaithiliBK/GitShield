import os

def scan_code(file_path):
    """Mock AI-based security scan for vulnerabilities."""
    with open(file_path, "r", encoding="utf-8") as f:
        code = f.read()
    
    if "eval(" in code:
        return f"🚨 Vulnerability found in {file_path}: Avoid using eval()!"
    
    return None

def check_repo_for_vulnerabilities():
    """Scans all code files in the repo before Git push."""
    issues_found = []
    
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith((".py", ".js", ".ts", ".java", ".cpp")):
                file_path = os.path.join(root, file)
                result = scan_code(file_path)
                if result:
                    issues_found.append(result)
    
    return issues_found

if __name__ == "__main__":
    vulnerabilities = check_repo_for_vulnerabilities()
    
    if vulnerabilities:
        print("🚨 Security vulnerabilities detected! Fix before pushing.")
        for issue in vulnerabilities:
            print(issue)
        exit(1)  # Block the push
    else:
        print("✅ No security issues found. Proceeding with push.")
