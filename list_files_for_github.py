#!/usr/bin/env python3
"""
List all files that should be uploaded to GitHub.
This script shows you exactly what to include in your repository.
"""

import os
from pathlib import Path

def list_files_to_upload():
    """List all files that should be uploaded to GitHub."""
    
    print("="*70)
    print("FILES TO UPLOAD TO GITHUB")
    print("="*70)
    print()
    
    # Essential files
    essential_files = [
        # Source code
        "src/__init__.py",
        "src/preprocessor.py",
        "src/indexer.py",
        "src/retriever.py",
        "src/evaluator.py",
        "src/main.py",
        
        # Main scripts
        "run_system.py",
        "evaluate_system.py",
        "analyze_dataset.py",
        "create_diagrams.py",
        "create_improved_pdf.py",
        "run_complete_assignment.py",
        "quick_test.py",
        
        # Configuration
        "requirements.txt",
        "README.md",
        ".gitignore",
    ]
    
    print("✅ ESSENTIAL FILES (Must Upload):")
    print("-" * 70)
    for file in essential_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"  ✓ {file:50} ({size:,} bytes)")
        else:
            print(f"  ✗ {file:50} (NOT FOUND)")
    
    print()
    print("✅ OPTIONAL FILES (Recommended):")
    print("-" * 70)
    
    optional_files = [
        "SETUP_AND_RUN.md",
        "START_HERE.md",
        "COMPLETE_CODE_SUMMARY.md",
        "run_assignment.bat",
        "run_assignment.sh",
    ]
    
    for file in optional_files:
        if os.path.exists(file):
            size = os.path.getsize(file)
            print(f"  ✓ {file:50} ({size:,} bytes)")
    
    print()
    print("✅ ASSIGNMENT SUBMISSION FOLDER:")
    print("-" * 70)
    
    if os.path.exists("assignment_submission"):
        for root, dirs, files in os.walk("assignment_submission"):
            # Skip __pycache__
            dirs[:] = [d for d in dirs if d != '__pycache__']
            
            for file in files:
                if not file.endswith(('.pyc', '.pyo')):
                    filepath = os.path.join(root, file)
                    size = os.path.getsize(filepath)
                    print(f"  ✓ {filepath:50} ({size:,} bytes)")
    
    print()
    print("❌ FILES TO EXCLUDE (Don't Upload):")
    print("-" * 70)
    
    exclude_patterns = [
        "*.pkl",
        "*.png",
        "*.pdf",
        "__pycache__/",
        "*.pyc",
        "evaluation_results.json",
        "index.pkl",
        "dataset/Articles.csv",
    ]
    
    for pattern in exclude_patterns:
        print(f"  ✗ {pattern}")
    
    print()
    print("="*70)
    print("SUMMARY")
    print("="*70)
    
    # Count files
    src_files = [f for f in os.listdir("src") if f.endswith('.py')] if os.path.exists("src") else []
    main_scripts = [f for f in os.listdir(".") if f.endswith('.py') and os.path.isfile(f)]
    
    print(f"Source code files (src/): {len(src_files)}")
    print(f"Main scripts: {len([f for f in main_scripts if f in [s.split('/')[-1] for s in essential_files]])}")
    print(f"Total Python files to upload: ~{len(src_files) + len([f for f in main_scripts if f not in ['test_pdf.py', 'demo.py', 'show_results.py']])}")
    
    print()
    print("📋 RECOMMENDED GIT COMMANDS:")
    print("-" * 70)
    print("git add src/")
    print("git add run_system.py evaluate_system.py analyze_dataset.py")
    print("git add create_diagrams.py create_improved_pdf.py")
    print("git add run_complete_assignment.py quick_test.py")
    print("git add requirements.txt README.md .gitignore")
    print("git add assignment_submission/  # if exists")
    print("git commit -m 'CS 516 Assignment 3: Complete IR System'")
    print("git push origin main")

if __name__ == '__main__':
    list_files_to_upload()

