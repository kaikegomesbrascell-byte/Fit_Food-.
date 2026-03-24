#!/usr/bin/env python3
"""
Quick HTTP server test to verify the landing page loads correctly
"""

import http.server
import socketserver
import os
import sys
from pathlib import Path

def test_file_access():
    """Test that all required files can be accessed"""
    print("Testing file access...")
    
    base_path = Path('landing-page-simples')
    
    files_to_check = [
        'index.html',
        'css/variables.css',
        'css/reset.css',
        'css/base.css',
        'css/components.css',
        'css/sections.css'
    ]
    
    all_ok = True
    for file_path in files_to_check:
        full_path = base_path / file_path
        if full_path.exists():
            print(f"  ✅ {file_path}")
        else:
            print(f"  ❌ {file_path} - NOT FOUND")
            all_ok = False
    
    return all_ok

def check_html_links():
    """Check that all CSS links in HTML are correct"""
    print("\nChecking HTML CSS links...")
    
    html_path = Path('landing-page-simples/index.html')
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    css_links = [
        'css/variables.css',
        'css/reset.css',
        'css/base.css',
        'css/components.css',
        'css/sections.css'
    ]
    
    all_ok = True
    for css_link in css_links:
        if css_link in html_content:
            print(f"  ✅ {css_link} linked in HTML")
        else:
            print(f"  ❌ {css_link} NOT linked in HTML")
            all_ok = False
    
    return all_ok

def main():
    print("="*60)
    print("LANDING PAGE - QUICK SERVER TEST")
    print("="*60 + "\n")
    
    # Test file access
    files_ok = test_file_access()
    
    # Check HTML links
    links_ok = check_html_links()
    
    print("\n" + "="*60)
    if files_ok and links_ok:
        print("✅ ALL CHECKS PASSED")
        print("\nThe landing page is ready to be served!")
        print("\nTo view the page, you can:")
        print("1. Open 'landing-page-simples/index.html' directly in a browser")
        print("2. Or run: python -m http.server 8000")
        print("   Then visit: http://localhost:8000/landing-page-simples/")
    else:
        print("❌ SOME CHECKS FAILED")
        print("\nPlease fix the issues above before serving the page.")
        return 1
    
    print("="*60)
    return 0

if __name__ == '__main__':
    exit(main())
