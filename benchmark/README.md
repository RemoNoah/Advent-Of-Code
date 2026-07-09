# Benchmark Tool

A simple Python benchmarking script to compare the execution time of two Python scripts.

## Usage

```bash
python benchmark.py <script1> <script2> [--runs N]
```

### Arguments

- `<script1>`: Path to the first script to benchmark
- `<script2>`: Path to the second script to benchmark
- `--runs N`: Number of times to run each script (default: 5)

### Examples

**Option 1: Run from the benchmark folder (recommended)**
```bash
cd benchmark
python benchmark.py "../Advent Of Code 2025/day10/day10.py" "../Advent Of Code 2025/day10/day10Part2.py"
```

**Option 2: Run from the root Advent-Of-Code folder**
```bash
python benchmark/benchmark.py "./Advent Of Code 2025/day10/day10.py" "./Advent Of Code 2025/day10/day10Part2.py"
```

**Run 10 iterations each:**
```bash
python benchmark/benchmark.py "./Advent Of Code 2025/day10/day10.py" "./Advent Of Code 2025/day10/day10Part2.py" --runs 10
```

## Output

The script displays:
- **Individual timing**: Min, max, and average execution time for each script
- **Comparison**: Which script is faster and by what factor (speedup)
- **Difference**: Exact time difference per run in seconds

### Example Output

```
============================================================
Benchmark: Comparing day10.py vs day10Part2.py
Runs per script: 3
============================================================

Running day10.py...
  Run 1: 0.3016s
  Run 2: 0.2960s
  Run 3: 0.2966s

Running day10Part2.py...
  Run 1: 0.1794s
  Run 2: 0.1860s
  Run 3: 0.1621s

============================================================
RESULTS
============================================================

day10.py:
  Min:     0.2960s
  Max:     0.3016s
  Average: 0.2981s

day10Part2.py:
  Min:     0.1621s
  Max:     0.1860s
  Average: 0.1758s

============================================================
🏆 day10Part2.py is faster
   Speedup: 1.70x
   Difference: 0.1223s per run
============================================================
```

## Features

- ✅ Multiple runs per script for statistical accuracy
- ✅ Handles script failures and timeouts gracefully
- ✅ Calculates min, max, and average execution times
- ✅ Shows speedup factor between scripts
- ✅ Clear, formatted output

## Requirements

- Python 3.6+
- No external dependencies

## Notes

- Each script is run in a separate process
- Output and errors from the scripts are captured
- Default timeout per run is 60 seconds
- Scripts with exit codes other than 0 will be noted in output
