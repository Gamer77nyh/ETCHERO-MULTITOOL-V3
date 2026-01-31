import os
import glob
import py_compile
from colorama import Fore, init

init(autoreset=True)

def check_syntax(file_path):
    try:
        py_compile.compile(file_path, doraise=True)
        return True, None
    except py_compile.PyCompileError as e:
        return False, str(e)
    except Exception as e:
        return False, str(e)

def main():
    print(f"{Fore.CYAN}Starting syntax check for all tools...\n")
    
    tools_dir = "tools"
    files = glob.glob(os.path.join(tools_dir, "*.py"))
    files.append("ETCHERO.py") # Check the main script too
    
    passed = 0
    failed = 0
    
    for file_path in files:
        if not os.path.exists(file_path):
            continue
            
        success, error_msg = check_syntax(file_path)
        
        if success:
            print(f"{Fore.GREEN}✅ [PASS] {file_path}")
            passed += 1
        else:
            print(f"{Fore.RED}❌ [FAIL] {file_path}")
            print(f"{Fore.YELLOW}   Error: {error_msg}")
            failed += 1
            
    print(f"\n{Fore.CYAN}--- Summary ---")
    print(f"{Fore.GREEN}Passed: {passed}")
    if failed > 0:
        print(f"{Fore.RED}Failed: {failed}")
    else:
        print(f"{Fore.GREEN}Failed: 0")
        print(f"\n{Fore.GREEN}🎉 All tools passed syntax check!")

if __name__ == "__main__":
    main()
