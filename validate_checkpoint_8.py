#!/usr/bin/env python3
"""
Checkpoint 8 Validation Script
Validates HTML structure and base styles for landing-page-simples
"""

import os
import re
from pathlib import Path
from html.parser import HTMLParser

class ValidationReport:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.successes = []
    
    def add_error(self, message):
        self.errors.append(f"❌ ERROR: {message}")
    
    def add_warning(self, message):
        self.warnings.append(f"⚠️  WARNING: {message}")
    
    def add_success(self, message):
        self.successes.append(f"✅ SUCCESS: {message}")
    
    def print_report(self):
        print("\n" + "="*70)
        print("CHECKPOINT 8 VALIDATION REPORT")
        print("="*70 + "\n")
        
        if self.successes:
            print("SUCCESSES:")
            for success in self.successes:
                print(f"  {success}")
            print()
        
        if self.warnings:
            print("WARNINGS:")
            for warning in self.warnings:
                print(f"  {warning}")
            print()
        
        if self.errors:
            print("ERRORS:")
            for error in self.errors:
                print(f"  {error}")
            print()
        
        print("="*70)
        print(f"Total: {len(self.successes)} successes, {len(self.warnings)} warnings, {len(self.errors)} errors")
        print("="*70 + "\n")
        
        return len(self.errors) == 0

class HTMLValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.sections = []
        self.css_links = []
        self.js_scripts = []
        self.has_doctype = False
        self.has_viewport = False
        self.has_charset = False
        self.semantic_elements = []
        
    def handle_decl(self, decl):
        if 'DOCTYPE' in decl.upper():
            self.has_doctype = True
    
    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        
        # Track semantic elements
        if tag in ['header', 'nav', 'main', 'section', 'article', 'aside', 'footer']:
            self.semantic_elements.append(tag)
        
        # Track sections by ID
        if tag == 'section' and 'id' in attrs_dict:
            self.sections.append(attrs_dict['id'])
        
        # Track CSS links
        if tag == 'link' and attrs_dict.get('rel') == 'stylesheet':
            self.css_links.append(attrs_dict.get('href', ''))
        
        # Track JS scripts
        if tag == 'script' and 'src' in attrs_dict:
            self.js_scripts.append(attrs_dict['src'])
        
        # Check for viewport meta
        if tag == 'meta' and attrs_dict.get('name') == 'viewport':
            self.has_viewport = True
        
        # Check for charset
        if tag == 'meta' and 'charset' in attrs_dict:
            self.has_charset = True

def validate_html_structure(report):
    """Validate the HTML structure of index.html"""
    print("Validating HTML structure...")
    
    html_path = Path('landing-page-simples/index.html')
    
    if not html_path.exists():
        report.add_error("index.html not found")
        return
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Parse HTML
        parser = HTMLValidator()
        parser.feed(html_content)
        
        # Check DOCTYPE
        if parser.has_doctype:
            report.add_success("HTML has DOCTYPE declaration")
        else:
            report.add_error("HTML missing DOCTYPE declaration")
        
        # Check charset
        if parser.has_charset:
            report.add_success("HTML has charset meta tag")
        else:
            report.add_error("HTML missing charset meta tag")
        
        # Check viewport
        if parser.has_viewport:
            report.add_success("HTML has viewport meta tag for responsiveness")
        else:
            report.add_error("HTML missing viewport meta tag")
        
        # Check required sections
        required_sections = ['hero', 'features', 'social-proof', 'lead-form']
        for section in required_sections:
            if section in parser.sections:
                report.add_success(f"Section '{section}' found")
            else:
                report.add_error(f"Required section '{section}' not found")
        
        # Check for footer
        if 'footer' in parser.semantic_elements:
            report.add_success("Footer element found")
        else:
            report.add_error("Footer element not found")
        
        # Check semantic HTML usage
        if len(parser.semantic_elements) >= 5:
            report.add_success(f"Good use of semantic HTML ({len(parser.semantic_elements)} semantic elements)")
        else:
            report.add_warning(f"Limited use of semantic HTML ({len(parser.semantic_elements)} semantic elements)")
        
    except Exception as e:
        report.add_error(f"Failed to parse HTML: {str(e)}")

def validate_css_files(report):
    """Validate that all CSS files exist and are properly linked"""
    print("Validating CSS files...")
    
    required_css_files = [
        'css/variables.css',
        'css/reset.css',
        'css/base.css',
        'css/components.css',
        'css/sections.css'
    ]
    
    html_path = Path('landing-page-simples/index.html')
    
    if html_path.exists():
        with open(html_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        for css_file in required_css_files:
            css_path = Path('landing-page-simples') / css_file
            
            # Check if file exists
            if css_path.exists():
                report.add_success(f"CSS file exists: {css_file}")
            else:
                report.add_error(f"CSS file missing: {css_file}")
            
            # Check if linked in HTML
            if css_file in html_content:
                report.add_success(f"CSS file linked in HTML: {css_file}")
            else:
                report.add_error(f"CSS file not linked in HTML: {css_file}")

def validate_css_variables(report):
    """Validate that CSS variables are properly defined"""
    print("Validating CSS variables...")
    
    variables_path = Path('landing-page-simples/css/variables.css')
    
    if not variables_path.exists():
        report.add_error("variables.css not found")
        return
    
    with open(variables_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Check for required variable categories
    required_vars = {
        '--color-primary': 'Primary color',
        '--color-secondary': 'Secondary color',
        '--color-success': 'Success color',
        '--color-error': 'Error color',
        '--font-primary': 'Primary font',
        '--text-base': 'Base text size',
        '--space-': 'Spacing system',
        '--shadow-': 'Shadow system',
        '--breakpoint-': 'Breakpoints'
    }
    
    for var, description in required_vars.items():
        if var in css_content:
            report.add_success(f"{description} defined ({var})")
        else:
            report.add_error(f"{description} not defined ({var})")

def validate_responsive_design(report):
    """Validate responsive design implementation"""
    print("Validating responsive design...")
    
    sections_path = Path('landing-page-simples/css/sections.css')
    
    if not sections_path.exists():
        report.add_error("sections.css not found")
        return
    
    with open(sections_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Check for media queries
    media_queries = re.findall(r'@media\s*\([^)]+\)', css_content)
    
    if len(media_queries) >= 3:
        report.add_success(f"Responsive design implemented ({len(media_queries)} media queries found)")
    else:
        report.add_warning(f"Limited responsive design ({len(media_queries)} media queries found)")
    
    # Check for common breakpoints
    if 'max-width: 768px' in css_content or 'max-width: 767px' in css_content:
        report.add_success("Mobile breakpoint defined")
    else:
        report.add_warning("Mobile breakpoint not found")
    
    if 'max-width: 1024px' in css_content or 'max-width: 1023px' in css_content:
        report.add_success("Tablet breakpoint defined")
    else:
        report.add_warning("Tablet breakpoint not found")

def validate_accessibility(report):
    """Validate accessibility features"""
    print("Validating accessibility features...")
    
    html_path = Path('landing-page-simples/index.html')
    
    if not html_path.exists():
        return
    
    with open(html_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Check for ARIA attributes
    if 'aria-label' in html_content:
        report.add_success("ARIA labels used")
    else:
        report.add_warning("No ARIA labels found")
    
    if 'aria-describedby' in html_content:
        report.add_success("ARIA describedby used for form fields")
    else:
        report.add_warning("ARIA describedby not found")
    
    # Check for alt text on images
    img_tags = re.findall(r'<img[^>]+>', html_content)
    imgs_with_alt = [img for img in img_tags if 'alt=' in img]
    
    if len(img_tags) == len(imgs_with_alt):
        report.add_success(f"All images have alt text ({len(img_tags)} images)")
    else:
        report.add_error(f"Some images missing alt text ({len(imgs_with_alt)}/{len(img_tags)})")
    
    # Check for form labels
    if '<label' in html_content and 'for=' in html_content:
        report.add_success("Form labels properly associated with inputs")
    else:
        report.add_warning("Form labels may not be properly associated")

def validate_components(report):
    """Validate that key components are implemented"""
    print("Validating components...")
    
    components_path = Path('landing-page-simples/css/components.css')
    
    if not components_path.exists():
        report.add_error("components.css not found")
        return
    
    with open(components_path, 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Check for CTA button styles
    if '.cta-button' in css_content:
        report.add_success("CTA button component defined")
    else:
        report.add_error("CTA button component not found")
    
    if '.cta-button--primary' in css_content:
        report.add_success("Primary CTA button variant defined")
    else:
        report.add_error("Primary CTA button variant not found")
    
    # Check for card components
    if '.feature-card' in css_content:
        report.add_success("Feature card component defined")
    else:
        report.add_error("Feature card component not found")
    
    if '.testimonial-card' in css_content:
        report.add_success("Testimonial card component defined")
    else:
        report.add_error("Testimonial card component not found")

def main():
    report = ValidationReport()
    
    print("\n" + "="*70)
    print("STARTING CHECKPOINT 8 VALIDATION")
    print("Validating HTML structure and base styles")
    print("="*70 + "\n")
    
    # Run all validations
    validate_html_structure(report)
    validate_css_files(report)
    validate_css_variables(report)
    validate_responsive_design(report)
    validate_accessibility(report)
    validate_components(report)
    
    # Print report
    success = report.print_report()
    
    if success:
        print("✅ CHECKPOINT 8 PASSED: All validations successful!")
        return 0
    else:
        print("❌ CHECKPOINT 8 FAILED: Please fix the errors above")
        return 1

if __name__ == '__main__':
    exit(main())
