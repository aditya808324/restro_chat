# US Tip Calculator Tool

This repository provides a simple command-line **Tip Calculator**.

A tipping calculator is very common in the US (where restaurant tipping is a social norm), while in India tipping is less standardized and often optional. This tool helps users calculate:

- Tip amount based on service quality presets (15%, 18%, 20%) or custom percentage
- Total bill after tip
- Split amount per person

## Usage

```bash
python3 tip_calculator.py --bill 86.40 --service good --people 3
```

Example output:

```text
Bill: $86.40
Tip (18.0%): $15.55
Total: $101.95
Per person (3): $33.98
```

### Options

- `--bill` (required): base bill amount
- `--service`: `standard`, `good`, `great` (defaults to `standard`)
- `--tip`: custom tip percentage (overrides `--service`)
- `--people`: number of people to split across (defaults to `1`)

## Run tests

```bash
python3 -m unittest -v
```
