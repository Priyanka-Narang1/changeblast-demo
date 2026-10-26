# ChangeBlast Demo

A small Python e-commerce application for evaluating code dependency
and change-impact analysis.

## Architecture

- `app/pricing.py`: calculates prices and discounts.
- `app/checkout.py`: calculates the total for a collection of items.
- `app/invoice.py`: generates invoices using checkout.
- `app/orders.py`: coordinates order creation and invoice generation.
- `tests/`: unit tests for pricing, checkout, and invoice generation.

## Dependency chain

Pricing -> Checkout -> Invoice -> Order workflow

The order workflow also calls Checkout directly.

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -v
```

## Purpose

This repository is a controlled example for testing whether AI development
tools can identify direct and indirect dependencies, relevant tests, and
potential impacts of a code change.

Static dependency analysis may not discover every runtime relationship.
