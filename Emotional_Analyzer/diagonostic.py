#!/usr/bin/env python3
"""
Diagnostic script to check file structure and import issues
"""

import os
import sys

def check_file_structure():
    """Check if all required files exist"""
    print("🔍 CHECKING FILE STRUCTURE")
    print("=" * 40)
    
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")
    
    required_files = [
        'main.py',
        'analyzer.py', 
        'utils.py',
        'visualization.py',
        'requirements.txt'
    ]
    
    missing_files = []
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} - Found")
        else:
            print(f"❌ {file} - Missing")
            missing_files.append(file)
    
    print(f"\nAll files in current directory:")
    for item in sorted(os.listdir('.')):
        if os.path.isfile(item):
            print(f"📄 {item}")
        elif os.path.isdir(item):
            print(f"📁 {item}/")
    
    return missing_files

def check_python_path():
    """Check Python path"""
    print("\n🛤️ CHECKING PYTHON PATH")
    print("=" * 40)
    for i, path in enumerate(sys.path):
        print(f"{i+1}. {path}")

def test_imports():
    """Test individual imports"""
    print("\n🔬 TESTING IMPORTS")
    print("=" * 40)
    
    # Add current directory to path
    current_dir = os.path.dirname(os.path.abspath(__file__))
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
        print(f"Added to path: {current_dir}")
    
    imports_to_test = [
        ('utils', 'from utils import clean_text'),
        ('analyzer', 'from analyzer import SentimentAnalyzer'),
        ('visualization', 'from visualization import plot_sentiment_distribution'),
        ('main', 'from main import main'),
        ('textblob', 'from textblob import TextBlob'),
        ('pandas', 'import pandas as pd'),
        ('matplotlib', 'import matplotlib.pyplot as plt'),
        ('nltk', 'import nltk')
    ]
    
    for module_name, import_statement in imports_to_test:
        try:
            exec(import_statement)
            print(f"✅ {module_name} - Import successful")
        except ImportError as e:
            print(f"❌ {module_name} - Import failed: {e}")
        except Exception as e:
            print(f"⚠️ {module_name} - Other error: {e}")

def clean_pycache():
    """Clean __pycache__ directories"""
    print("\n🧹 CLEANING __pycache__ DIRECTORIES")
    print("=" * 40)
    
    cleaned_dirs = []
    for root, dirs, files in os.walk('.'):
        if '__pycache__' in dirs:
            pycache_path = os.path.join(root, '__pycache__')
            try:
                import shutil
                shutil.rmtree(pycache_path)
                cleaned_dirs.append(pycache_path)
                print(f"🗑️ Removed: {pycache_path}")
            except Exception as e:
                print(f"❌ Failed to remove {pycache_path}: {e}")
    
    if not cleaned_dirs:
        print("No __pycache__ directories found")
    else:
        print(f"Cleaned {len(cleaned_dirs)} __pycache__ directories")

def main():
    """Run all diagnostic checks"""
    print("🔧 SENTIMENT ANALYZER DIAGNOSTIC TOOL")
    print("=" * 50)
    
    # Check file structure
    missing_files = check_file_structure()
    
    # Check Python path
    check_python_path()
    
    # Test imports
    test_imports()
    
    # Clean pycache
    clean_pycache()
    
    print("\n📋 SUMMARY")
    print("=" * 40)
    if missing_files:
        print(f"❌ Missing files: {', '.join(missing_files)}")
        print("Please ensure all required files are in the same directory")
    else:
        print("✅ All required files found")
    
    print("\n💡 NEXT STEPS:")
    print("1. If imports failed, run: pip install -r requirements.txt")
    print("2. Try running: python run.py")
    print("3. If still failing, try: python main.py directly")

if __name__ == "__main__":
    main()