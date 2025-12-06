#!/usr/bin/env python3
"""
Main entry point for the IR system.
Run this script to start the interactive search interface.
"""

from src.main import build_system, interactive_search

if __name__ == '__main__':
    print("="*60)
    print("Information Retrieval System")
    print("CS 516: Information Retrieval and Text Mining")
    print("="*60)
    
    # Build or load system
    retriever, indexer = build_system(rebuild_index=False)
    
    # Start interactive search
    interactive_search(retriever)

