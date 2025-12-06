#!/usr/bin/env python3
"""
Evaluation script for the IR system.
Run this to evaluate system performance on test queries.
"""

import sys
from pathlib import Path

# Add src to path (go up one level since we're in assignment_submission)
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from main import build_system
from evaluator import IREvaluator
import json

def evaluate_system():
    """Evaluate the IR system with sample queries."""
    
    # Build system
    print("Loading IR system...")
    retriever, indexer = build_system(rebuild_index=False)
    
    # Sample test queries (you should replace these with your own)
    test_queries = [
        "politics",
        "sports",
        "technology",
        "economy",
        "health"
    ]
    
    # For each query, you need to manually label relevant documents
    # This is a template - replace with actual relevant doc IDs
    query_relevance = {
        "politics": [0, 5, 12, 23],  # Example: document IDs that are relevant
        "sports": [1, 8, 15],
        "technology": [2, 9, 16],
        "economy": [3, 10, 17],
        "health": [4, 11, 18]
    }
    
    print("\n" + "="*60)
    print("EVALUATION RESULTS")
    print("="*60)
    
    all_metrics = []
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = retriever.retrieve(query, top_k=10)
        
        if query in query_relevance:
            relevant_docs = query_relevance[query]
            result_tuples = [(doc_id, score) for doc_id, score, _, _ in results]
            
            metrics = IREvaluator.evaluate_retrieval(
                result_tuples,
                relevant_docs,
                k_values=[1, 5, 10]
            )
            
            all_metrics.append({
                'query': query,
                'metrics': metrics
            })
            
            print(f"  Precision@1: {metrics['precision@1']:.4f}")
            print(f"  Precision@5: {metrics['precision@5']:.4f}")
            print(f"  Precision@10: {metrics['precision@10']:.4f}")
            print(f"  Recall@10: {metrics['recall@10']:.4f}")
            print(f"  MRR: {metrics['mrr']:.4f}")
            print(f"  MAP: {metrics['map']:.4f}")
        else:
            print("  No relevance judgments available")
    
    # Compute average metrics
    if all_metrics:
        avg_metrics = {}
        for k in ['precision@1', 'precision@5', 'precision@10', 'recall@10', 'mrr', 'map']:
            values = [m['metrics'][k] for m in all_metrics if k in m['metrics']]
            if values:
                avg_metrics[k] = sum(values) / len(values)
        
        print("\n" + "="*60)
        print("AVERAGE METRICS")
        print("="*60)
        for metric, value in avg_metrics.items():
            print(f"  {metric}: {value:.4f}")
    
    # Measure efficiency
    print("\n" + "="*60)
    print("EFFICIENCY METRICS")
    print("="*60)
    efficiency = IREvaluator.measure_efficiency(retriever, test_queries)
    for metric, value in efficiency.items():
        print(f"  {metric}: {value}")
    
    # Save results
    with open('evaluation_results.json', 'w') as f:
        json.dump({
            'query_metrics': all_metrics,
            'average_metrics': avg_metrics if all_metrics else {},
            'efficiency': efficiency
        }, f, indent=2)
    
    print("\nResults saved to evaluation_results.json")

if __name__ == '__main__':
    evaluate_system()

