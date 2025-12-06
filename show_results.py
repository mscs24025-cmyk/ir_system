#!/usr/bin/env python3
"""
Complete demonstration of the IR system with full dataset.
"""

import sys
import os
import time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.main import build_system

print("="*80)
print("INFORMATION RETRIEVAL SYSTEM - COMPLETE DEMONSTRATION")
print("CS 516: Information Retrieval and Text Mining")
print("="*80)
print()

# Check if index exists
index_exists = os.path.exists('index.pkl')

if index_exists:
    print("Found existing index. Loading...")
    rebuild = False
else:
    print("No existing index found. Building new index...")
    rebuild = True

print()

# Build system
start_time = time.time()
retriever, indexer = build_system(rebuild_index=rebuild)
build_time = time.time() - start_time

print()
print(f"✓ System ready! ({build_time:.2f} seconds)")
print(f"✓ Total documents indexed: {len(indexer.documents)}")
print()

# Test queries with better examples
test_queries = [
    "Pakistan economy",
    "cricket match",
    "government policy",
    "stock market",
    "education system"
]

print("="*80)
print("RETRIEVAL RESULTS")
print("="*80)
print()

for query_idx, query in enumerate(test_queries, 1):
    print(f"\n{'='*80}")
    print(f"QUERY {query_idx}: '{query}'")
    print('='*80)
    
    start = time.time()
    results = retriever.retrieve(query, top_k=5)
    query_time = (time.time() - start) * 1000  # in milliseconds
    
    if not results:
        print("No results found.")
        continue
    
    print(f"\nFound {len(results)} results (Query time: {query_time:.2f} ms)\n")
    
    for i, (doc_id, score, doc_text, metadata) in enumerate(results, 1):
        heading = metadata.get('heading', 'N/A')
        date = metadata.get('date', 'N/A')
        news_type = metadata.get('news_type', 'N/A')
        
        print(f"Result {i}:")
        print(f"  Document ID: {doc_id}")
        print(f"  Relevance Score: {score:.4f}")
        print(f"  Heading: {heading}")
        print(f"  Date: {date}")
        print(f"  Type: {news_type}")
        print(f"  Preview: {doc_text[:250]}...")
        print()

print("="*80)
print("DEMONSTRATION COMPLETE")
print("="*80)
print()
print("To use the interactive search interface, run:")
print("  python run_system.py")
print()
print("To rebuild the index from scratch, run:")
print("  python -m src.main --rebuild")
print()

