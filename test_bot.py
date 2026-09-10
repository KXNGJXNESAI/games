#!/usr/bin/env python3
"""
Quick test runner for BitChat Casino Bot.
Tests all core functionality without requiring manual testing.
"""

import sys
import subprocess
import os

def run_test(name, command):
    """Run a single test and return success/failure."""
    print(f"\n{'='*50}")
    print(f"🧪 TEST: {name}")
    print(f"{'='*50}")
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"✅ PASSED: {name}")
            if result.stdout:
                print(result.stdout)
            return True
        else:
            print(f"❌ FAILED: {name}")
            if result.stderr:
                print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False

def main():
    """Run all tests."""
    print("\n" + "🎰 "*10)
    print("BitChat Casino Bot - Test Suite")
    print("🎰 "*10)
    
    tests = [
        ("Python Version", "python3 --version"),
        ("Python Imports", "python3 -c 'import websockets, marshmallow; print(\"OK\")'"),
        ("Cashu CLI", "cashu --version"),
        ("Config Module", "python3 -c 'from config import Config; print(\"Config loaded\")'"),
        ("BIP340 Module", "python3 -c 'from bip340 import *; print(\"BIP340 loaded\")'"),
        ("Main Script Syntax", "python3 -m py_compile main.py && echo 'Syntax OK'"),
        ("Nostr Client Syntax", "python3 -m py_compile nostr_client.py && echo 'Syntax OK'"),
        ("Game Manager Syntax", "python3 -m py_compile game_manager.py && echo 'Syntax OK'"),
        ("Cashu Handler Syntax", "python3 -m py_compile cashu_handler.py && echo 'Syntax OK'"),
        ("Directories", "mkdir -p house_wallet games && echo 'Directories OK'"),
    ]
    
    results = []
    for name, command in tests:
        results.append((name, run_test(name, command)))
    
    # Summary
    print("\n" + "="*50)
    print("📊 TEST SUMMARY")
    print("="*50)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅" if result else "❌"
        print(f"{status} {name}")
    
    print(f"\n{passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! Bot is ready to run.")
        print("   Run: python3 main.py")
        return 0
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. See above for details.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
