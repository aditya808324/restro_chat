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

## Live demo

```bash
python3 tip_calculator.py --live-demo
```

This runs three sample US-style scenarios (solo diner, date night, and group dinner split).

### Options

- `--bill`: base bill amount (required unless `--live-demo` is used)
- `--service`: `standard`, `good`, `great` (defaults to `standard`)
- `--tip`: custom tip percentage (overrides `--service`)
- `--people`: number of people to split across (defaults to `1`)
- `--live-demo`: prints multiple sample scenarios in one run

## Run tests

```bash
python3 -m unittest -v
```
