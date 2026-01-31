import hashlib

def generate_hashes(text):
    print(f"\nOriginal Text: {text}")
    print("-" * 50)
    print(f"{'Algorithm':<10} | {'Hash'}")
    print("-" * 50)
    
    algorithms = {
        "MD5": hashlib.md5,
        "SHA1": hashlib.sha1,
        "SHA256": hashlib.sha256,
        "SHA512": hashlib.sha512
    }
    
    for name, func in algorithms.items():
        h = func(text.encode()).hexdigest()
        print(f"{name:<10} | {h}")

def identify_hash(hash_str):
    length = len(hash_str)
    print(f"\nAnalyzing Hash: {hash_str}")
    print(f"Length: {length} characters")
    
    candidates = []
    if length == 32:
        candidates.append("MD5")
    if length == 40:
        candidates.append("SHA1")
    if length == 64:
        candidates.append("SHA-256")
    if length == 128:
        candidates.append("SHA-512")
        
    if candidates:
        print(f"[+] Possible Types: {', '.join(candidates)}")
    else:
        print("[-] Unknown hash type or non-standard length.")

def main():
    print("\n=== Hash Generator & Identifier ===")
    print("[1] Generate Hashes from Text")
    print("[2] Identify Hash Type")
    
    choice = input("\nSelect option: ")
    
    if choice == '1':
        text = input("Enter text to hash: ")
        generate_hashes(text)
    elif choice == '2':
        h = input("Enter hash to identify: ").strip()
        identify_hash(h)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
    input("\nPress Enter to return to menu...")
