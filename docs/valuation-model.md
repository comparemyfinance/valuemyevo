# EvoWorth Valuation Model

## Purpose

This document explains how EvoWorth currently turns an EVO card input into a valuation response. It is written for both product and technical readers, so it describes the product meaning of the output as well as the current implementation logic.

## Definition of Market-Equivalent Value

Market-equivalent value is EvoWorth's estimate of what an EVO outcome is worth relative to similar tradable cards in the live market.

It is not a claim about the exact amount a user could sell the card for. In many cases, the exact EVO outcome is untradeable or does not exist as a directly listed market item. Instead, EvoWorth asks a different question: if this EVO card were compared against similar tradable cards, what value would the market imply?

That framing makes the product useful for decision-making. A player usually wants to know whether an EVO is worth the cost compared with market alternatives, not whether the card can literally be sold.

## Why `median_price_now` Is Used Across Source Prices

`median_price_now` is the current single-value estimate for the card's market-equivalent value. It is calculated from the available source prices and represented as an integer coin value.

The current service logic:

- collects the list of source prices
- extracts the numeric `price` from each source
- calculates the median of those values
- converts the result to an integer

The median is used instead of the average because it is more resistant to outliers. In a market context, one unusually low or unusually high observation can distort an average more than it should. The median gives a more stable center point when source prices are uneven or noisy.

For product stakeholders, the practical meaning is simple: `median_price_now` is meant to be a robust "best current benchmark" rather than an overly reactive number.

For technical stakeholders, this is currently a pure aggregation step. No source weighting, freshness weighting, or platform adjustment is applied beyond the requirement that each source price is explicitly represented in the data model.

## Confidence Scoring Logic

The current confidence score is a bounded heuristic, not a predictive probability and not a machine-learned certainty estimate.

The implementation starts with a base confidence of `0.45`, then adds:

- `0.08` per source price, capped at `0.25`
- `0.10` per comparable card, capped at `0.20`

The final result is capped at `0.95` and rounded to two decimal places.

In plain language:

- more source prices increase confidence because the estimate is supported by more market observations
- more comparable cards increase confidence because the estimate is benchmarked against a broader comparison set
- caps are used so confidence does not grow without limit just because more records exist

This means confidence currently answers the question, "How much evidence do we have?" more than, "How accurate is this number guaranteed to be?"

## How Comparable Cards Are Represented

Comparable cards are represented as structured card objects, not just labels or price references. Each comparable card can include:

- player name
- base card type
- final overall
- positions
- weak foot
- skill moves
- playstyles
- playstyles+
- face stats
- optional in-game stats
- platform
- its own source prices
- its own `median_price_now`

This representation matters because EvoWorth is not only trying to produce a number. It is also trying to make that number inspectable. Product users need to understand what kinds of cards the system considered comparable, and technical systems need a stable schema that can support future ranking, explanation, and UI display.

## Assumptions

The current model assumes:

- comparable market cards are a valid basis for inferring the value of a custom EVO outcome
- the median of source prices is a reasonable single benchmark for current value
- a larger number of source prices and comparable cards generally improves trust in the estimate
- the input card attributes capture enough information to support meaningful future comparison logic
- platform is important enough to be modeled explicitly in both source prices and comparable cards

## Current Limitations

The current implementation is intentionally simple and still uses stubbed valuation data.

Key limitations:

- Source prices and comparables are currently mocked by the provider layer.
- The model does not yet explain how comparables are selected beyond the fact that they are included in the response.
- No weighting is applied for source quality, data freshness, scarcity, or market volatility.
- No valuation range is produced yet; the primary output is a single `median_price_now` value.
- Confidence is heuristic only. It does not yet measure historical error or model calibration.
- The system does not yet account for event-driven market swings, changing meta relevance, or supply shocks.
- The model is descriptive, not predictive. It estimates current implied value rather than future price movement.

## Working Interpretation for Stakeholders

Product teams should treat the current model as a transparent first-pass valuation framework: a clear, explainable way to estimate implied market value from source prices and comparable cards.

Engineering teams should treat it as a stable contract with room for better data and smarter ranking logic later. The schema already supports richer sourcing, comparison, and explanation layers, even though the current service is still using a simple median-and-heuristics approach.
