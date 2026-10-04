# plan-regression

Offline PostgreSQL EXPLAIN JSON regression gate with structural change reports.

An offline Python 3.10+ MVP with no runtime dependencies.

## Install and first useful result

```sh
git clone https://github.com/nripankadas07/plan-regression.git
cd plan-regression
python -m venv .venv
# POSIX; on Windows use .venv\Scripts\activate
. .venv/bin/activate
python -m pip install .
plan-regression --help
python demo.py
```

The demo creates temporary synthetic inputs and prints the actual report; it does not require accounts, services, API keys or user data. CLI exit status: 0 = accepted/clean; 1 = review findings; 2 = invalid input or operational error.

## CLI example

```sh
plan-regression before.json after.json --max-ratio 1.2 --minimum-delta 10
```

Save PostgreSQL `EXPLAIN (FORMAT JSON)` outputs from comparable runs. Planner cost is not elapsed time.

## Validate

```sh
python -m unittest discover -v
python -m compileall -q plan_regression.py
python demo.py
```

## Limits

PostgreSQL JSON only. Positional paths cannot match reordered equivalent operators. Changed structures require review. Planner cost and row estimates are not measured performance. Timing inputs require equivalent workloads and repeated runs; no superiority or speed claims are made.

See [RESEARCH.md](RESEARCH.md) for the user brief and dated comparisons, [VALIDATION.md](VALIDATION.md) for exact check coverage, and [SUPPORT.md](SUPPORT.md) for contributions and security reporting. MIT licensed; original implementation, with standard-library dependencies. No competitor code or prose copied.
