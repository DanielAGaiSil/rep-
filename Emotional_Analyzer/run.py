#!/usr/bin/env python3
"""
Sentiment Analysis Tool - Entry Point
Run with: python run.py
"""

import sys
import os

def setup_imports():
    """Setup Python path for imports"""
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Add script directory to Python path if not already there
    if script_dir not in sys.path:
        sys.path.insert(0, script_dir)
    
    # Also add current working directory
    current_dir = os.getcwd()
    if current_dir not in sys.path:
        sys.path.insert(0, current_dir)
    
    print(f"Script directory: {script_dir}")
    print(f"Current directory: {current_dir}")

def check_required_files():
    """Check if all required files exist"""
    required_files = ['main.py', 'analyzer.py', 'utils.py', 'visualization.py']
    missing_files = []
    
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print(f"❌ Missing required files: {', '.join(missing_files)}")
        print("Please ensure all files are in the same directory as run.py")
        return False
    
    return True

def main():
    """Main entry point"""
    print("🚀 Starting Sentiment Analysis Tool...")
    
    # Setup import paths
    setup_imports()
    
    # Check required files
    if not check_required_files():
        sys.exit(1)
    
    # Try to import and run
    try:
        print("📦 Importing modules...")
        from main import main as main_function
        
        print("✅ All imports successful!")
        print("🎯 Starting application...\n")
        
        # Run the main application
        main_function()
        
    except ImportError as e:
        print(f"❌ Import Error: {e}")
        print("\n🔧 Troubleshooting steps:")
        print("1. Run: python diagnostic.py")
        print("2. Install dependencies: pip install -r requirements.txt")
        print("3. Try running directly: python main.py")
        sys.exit(1)
        
    except KeyboardInterrupt:
        print("\n👋 Application interrupted by user")
        sys.exit(0)
        
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        print("Run 'python diagnostic.py' for more information")
        sys.exit(1)

if __name__ == "__main__":
    main()