# EvoWorth Product Spec

## Product Goal

EvoWorth helps EA FC Ultimate Team players estimate the market-equivalent value of an EVO card by comparing its final attributes to live market prices for similar tradable cards. The product exists to answer a specific question: "If this EVO existed as a market card, what would it likely be worth?"

## Core User Story

As an Ultimate Team player considering or evaluating an EVO path, I want to enter the finished card attributes and see a defensible market-equivalent value range based on comparable cards, so I can decide whether the EVO is worth the coins, fodder, and opportunity cost.

## MVP Scope

- Public landing page explaining the product and its valuation approach.
- Input flow for an EVO card's final state:
  - player name
  - base card type
  - final overall
  - positions
  - weak foot and skill moves
  - playstyles and playstyles+
  - face stats
  - optional in-game stats
  - platform
- Valuation response with:
  - current median market-equivalent value
  - supporting comparable cards
  - source prices used in the estimate
  - confidence score
  - short explanation of how the estimate was produced
- API surface that supports the above workflow with stable request and response models.
- Stubbed or normalized valuation-provider layer that can later be replaced with real data sources.

## Non-Goals

- Predicting the exact sale price a specific user's EVO card would achieve if listed.
- Building a trading bot, sniping tool, or live market execution product.
- Portfolio tracking, club management, or broader FUT account analytics.
- Authentication, subscriptions, payments, or admin tooling in the first release.
- Automated scraping infrastructure as part of the initial product foundation.

## Roadmap

### Phase 1: Foundation

- Ship the landing page and basic valuation API.
- Establish a clear schema for EVO inputs, comparables, source prices, and confidence.
- Validate the core UX thesis: players want a quick benchmark for whether an EVO is "worth it."

### Phase 2: Real Market Intelligence

- Replace mock valuation inputs with real normalized market data.
- Improve comparable-card selection using position, stats, playstyles, and role similarity.
- Add value ranges, not just a single point estimate.

### Phase 3: Decision Support

- Add "worth it" analysis against EVO costs.
- Show value delta versus the base card and versus likely alternative upgrades.
- Add saved comparisons for multiple EVO paths.

### Phase 4: Product Depth

- Personalized preferences by platform and play style.
- Historical trend context for comparable cards.
- Content features such as featured EVO opportunities and market inefficiencies.

## Positioning Statement

For EA FC Ultimate Team players who want to judge whether an EVO is worth doing, EvoWorth is a market-equivalent valuation tool that estimates what an evolved card is worth by benchmarking it against tradable comparables. Unlike generic FUT databases or simple price trackers, EvoWorth focuses on the implied market value of a custom, often untradeable card outcome.

## Homepage Headline and Subheadline

### Headline

What is your EVO really worth?

### Subheadline

Estimate the market-equivalent value of any finished EVO card using comparable tradable cards, source prices, and a transparent confidence score.

## Why This Is a Market-Equivalent Value Product Rather Than a Sell-Price Product

EVO cards are often untradeable, custom to the user's upgrade path, or otherwise not directly listed on the market in the exact form the player owns. Because of that, EvoWorth should not claim to tell the user what their card would literally sell for today. In many cases, there is no direct sellable market for the exact card being evaluated.

Instead, the correct product framing is market-equivalent value. That means EvoWorth estimates the value of the card by asking what similar tradable cards are worth in the live market and then using those comparables to infer the implied worth of the EVO outcome.

This distinction matters for three reasons:

- It is more honest. The product is estimating implied value, not pretending to observe a sale that cannot actually happen.
- It matches the user decision. Players are usually deciding whether an EVO is worth the cost relative to market alternatives, not whether they can liquidate the card.
- It supports a defensible methodology. Comparable cards, median source prices, and confidence scoring are appropriate for inferred market-equivalent value, while they would be too indirect to justify a precise sell-price claim.

In short, EvoWorth is a valuation product for decision-making, not a resale-price product for execution.
