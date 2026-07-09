"""
Benchmark script to compare execution time of two Python scripts.
Usage: python benchmark.py <script1> <script2> [--runs N]
"""

import subprocess
import time
import sys
from pathlib import Path


def run_script(script_path, runs=5):
    """Run a script multiple times and measure execution time."""
    script_path = Path(script_path)
    if not script_path.exists():
        raise FileNotFoundError(f"Script not found: {script_path}")
    
    times = []
    print(f"\nRunning {script_path.name}...")
    
    for i in range(runs):
        try:
            start = time.perf_counter()
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True,
                timeout=60
            )
            elapsed = time.perf_counter() - start
            times.append(elapsed)
            print(f"  Run {i+1}: {elapsed:.4f}s", end="")
            if result.returncode != 0:
                print(f" (Exit code: {result.returncode})")
            else:
                print()
        except subprocess.TimeoutExpired:
            print(f"  Run {i+1}: TIMEOUT")
            return None
        except Exception as e:
            print(f"  Run {i+1}: ERROR - {e}")
            return None
    
    return times


def format_stats(times, name):
    """Format timing statistics."""
    if not times:
        return f"{name}: Failed to complete"
    
    min_time = min(times)
    max_time = max(times)
    avg_time = sum(times) / len(times)
    
    return {
        'name': name,
        'min': min_time,
        'max': max_time,
        'avg': avg_time,
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python benchmark.py <script1> <script2> [--runs N]")
        print("Example: python benchmark.py day10.py day10Part2.py --runs 10")
        sys.exit(1)
    
    script1 = sys.argv[1]
    script2 = sys.argv[2]
    
    runs = 5
    if "--runs" in sys.argv:
        try:
            runs = int(sys.argv[sys.argv.index("--runs") + 1])
        except (ValueError, IndexError):
            print("Invalid --runs value")
            sys.exit(1)
    
    print(f"{'='*60}")
    print(f"Benchmark: Comparing {Path(script1).name} vs {Path(script2).name}")
    print(f"Runs per script: {runs}")
    print(f"{'='*60}")
    
    # Run both scripts
    times1 = run_script(script1, runs)
    times2 = run_script(script2, runs)
    
    if not times1 or not times2:
        print("\n❌ Benchmark failed - one or both scripts failed to run")
        sys.exit(1)
    
    # Format and display results
    stats1 = format_stats(times1, Path(script1).name)
    stats2 = format_stats(times2, Path(script2).name)
    
    print(f"\n{'='*60}")
    print("RESULTS")
    print(f"{'='*60}")
    
    print(f"\n{stats1['name']}:")
    print(f"  Min:     {stats1['min']:.4f}s")
    print(f"  Max:     {stats1['max']:.4f}s")
    print(f"  Average: {stats1['avg']:.4f}s")
    
    print(f"\n{stats2['name']}:")
    print(f"  Min:     {stats2['min']:.4f}s")
    print(f"  Max:     {stats2['max']:.4f}s")
    print(f"  Average: {stats2['avg']:.4f}s")
    
    # Compare
    faster = stats1 if stats1['avg'] < stats2['avg'] else stats2
    slower = stats2 if faster['name'] == stats1['name'] else stats1
    speedup = slower['avg'] / faster['avg']
    
    print(f"\n{'='*60}")
    print(f"🏆 {faster['name']} is faster")
    print(f"   Speedup: {speedup:.2f}x")
    print(f"   Difference: {slower['avg'] - faster['avg']:.4f}s per run")
    print(f"{'='*60}\n")


if __name__ == "__main__":
    main()
