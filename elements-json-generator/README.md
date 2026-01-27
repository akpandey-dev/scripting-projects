# Periodic Table JSON Generator

A Python script that generates a **structured JSON dataset of chemical elements**, including real, predicted, and theoretical elements, using a fixed schema and consistent property ordering.

This project focuses on **data consistency, schema design, and scientific dataset construction**.

---

## What This Project Does

- Defines a **fixed schema (keys)** for element properties
- Stores each element as an ordered list of values
- Converts element lists into dictionaries using the schema
- Exports all elements into a single `elements.json` file
- Includes **natural, synthetic, and predicted elements** (up to element 120)

This approach ensures:
- Consistent data shape
- Easy validation
- Clean JSON output suitable for APIs, apps, or research tools

---

## Dataset Structure

Each element contains the following categories (non-exhaustive):

- Atomic identity (number, symbol, name)
- Physical properties (mass, density, phase)
- Periodic table placement (group, period, block)
- Atomic behavior (valency, bonding, oxidation states)
- Discovery & origin data
- Radioactivity & toxicity
- Practical uses
- Isotopic and theoretical information

Total properties per element: **~35+ fields**

---

## Output

The script generates:

```text
elements.json
Structure:

[
  {
    "atomicNumber": 1,
    "symbol": "H",
    "name": "Hydrogen",
    "atomicMass": 1.008,
    ...
  },
  ...
]

```

## Requirements

- Python 3.x
- Standard library only (json)

No external dependencies.

---

## How to Run

```bash
python calculator.py
```