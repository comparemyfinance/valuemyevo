# EvoWorth Source Mapping

## Purpose

This document is a planning reference for future live source integration. It defines how EvoWorth should think about external card sources, URL patterns, identifiers, and platform labels before any live fetching is implemented.

This is intentionally a planning document only. No scraping, API calls, or live fetching are implemented as part of this work.

## Source Summary

| Source name | Intended card URL format | Platform naming differences | Source-specific card identifiers | Adapter status | Notes for future live integration |
| --- | --- | --- | --- | --- | --- |
| `futbin` | `https://www.futbin.com/{game_version}/player/{item_id}/{slug}` | Page copy shows separate prices for `PlayStation`, `Xbox`, and `PC`. FUTBIN also commonly treats console markets together in some views, so mapping may need both a combined `console` concept and split platform fields. | Likely `item_id` in the URL path plus a player/card slug. Same player can have multiple items across versions and promo types. | Stub adapter exists. Returns synthetic price and root URL only. No live URL builder or identifier resolver yet. | Good candidate for live price lookup because player pages visibly expose price information. Need a resolver from Evo card input to FUTBIN item IDs and a policy for handling multiple card variants for the same player. |
| `futgg` | `https://www.fut.gg/players/{player_id}-{slug}/` and then card-specific subviews beneath that page | Public snippets confirm card pages and price tracking, but platform label conventions should be confirmed during implementation. Likely `PlayStation`, `Xbox`, and `PC`, with possible grouped console presentation in some contexts. | Page content exposes both `Player ID` and `Item ID`. Planning assumption: `item_id` is the more precise identifier for a specific card, while `player_id` identifies the footballer. | Stub adapter exists. Returns synthetic price and root URL only. No live URL builder or identifier resolver yet. | Strong source for richer metadata because pages expose both player and item identifiers. Need to determine whether live price extraction is available from the main player page, a tab, or a separate internal endpoint. |
| `easysbc` | Observed examples include `https://www.easysbc.io/players/{player-slug}/{card-type}/{item_id}` and variants with query parameters such as `?player-role-id=...` | Platform naming for market prices is not yet confirmed from available snippets. EasySBC may emphasize meta ratings and player views more than explicit platform price tables, so platform support should be treated as unverified until live integration work begins. | Observed URLs include an `item_id`-like numeric segment, plus player slug and card-type segment. Query parameters may affect page state rather than card identity. | Stub adapter exists. Returns synthetic price and root URL only. No live URL builder or identifier resolver yet. | Potentially useful for card metadata and role context even if direct market price extraction proves less stable. Need to verify whether price data is first-class, derived, or absent on the page before relying on it as a valuation source. |

## Source-by-Source Notes

### FUTBIN

Planned interpretation:

- Treat FUTBIN as a likely primary market-price source.
- Prefer `item_id` as the canonical external card identifier when available.
- Preserve the human-readable slug only for URL generation and debugging.

Integration notes:

- The source may expose separate values for `PlayStation`, `Xbox`, and `PC`.
- Some FUTBIN views historically group console platforms together; if that remains true in live integration, EvoWorth should normalize grouped console prices carefully rather than assuming they are fully platform-specific.
- The live adapter will need a deterministic way to choose the correct card item when a player has many promo variants.

### FUT.GG

Planned interpretation:

- Treat FUT.GG as both a pricing source and a metadata source.
- Capture both `player_id` and `item_id` if available, because they appear to serve different purposes.
- Prefer `item_id` for exact card matching and `player_id` for broader lookups or fallback search.

Integration notes:

- The root player page format appears stable enough for planning.
- The exact live price location should be verified before any parser is built.
- The source may support richer card context than FUTBIN, which could help later comparable-card selection and explanation features.

### EasySBC

Planned interpretation:

- Treat EasySBC as a secondary source until price visibility and platform granularity are confirmed.
- Assume the numeric path segment is the most likely candidate for a stable card identifier.
- Treat query parameters as optional page-state hints unless proven necessary for identity.

Integration notes:

- EasySBC may be better suited for metadata enrichment than as a core price source.
- If price data is not consistently available, the adapter may still remain useful for role, meta, or card classification context.
- Implementation should avoid overfitting to one observed URL variant because the site appears to use multiple path shapes.

## Cross-Source Mapping Plan

For future live integration, EvoWorth should maintain a normalized internal source mapping record with at least:

- `source_name`
- `source_player_id` when available
- `source_item_id` when available
- `source_url`
- `platform_label_raw`
- `platform_normalized`
- `observed_at`
- `price`
- `currency`

This allows the application to preserve what the source actually said while still normalizing the result into the internal `SourcePrice` schema.

## Proposed Platform Normalization

Current internal platform enum:

- `playstation`
- `xbox`
- `pc`
- `switch`

Planning rules for future integration:

- Preserve the raw platform label exactly as observed at the source.
- Normalize known labels to the internal enum where there is a clear mapping.
- Support a future grouped-console case if a source reports `console`, `PlayStation/Xbox`, or similar combined wording.
- Do not invent `switch` support from a source unless it is explicitly present in that source's live card pricing.

## Current Adapter Status

The codebase currently has placeholder adapters for:

- `FutbinAdapter`
- `FutggAdapter`
- `EasySbcAdapter`

Current status across all three:

- each adapter returns a synthetic `SourcePrice`
- each adapter uses the incoming card platform directly
- each adapter points to the source home page, not a real card URL
- no live identifier lookup exists
- no live HTML parsing or API integration exists

## Assumptions and Open Questions

Current planning assumptions:

- `item_id` will likely be the most important identifier for exact card matching across sources.
- Source-specific slugs are useful for readable URLs but should not be treated as the canonical identity.
- Platform labels may differ by source even when they map to the same internal enum.

Open questions for live integration:

- Which source has the most stable and parseable price surface?
- Are console prices grouped or split consistently by source?
- Which source updates fastest and most reliably?
- Which identifier is stable across game updates, promo releases, and repeated card versions?
- Can EvoWorth resolve a source card directly from structured card attributes, or will it need a search stage first?

## Implementation Guardrails for Later

When live integration work begins:

- keep adapter logic source-specific and isolated
- store raw source identifiers and raw platform labels alongside normalized values
- avoid assuming URL patterns are permanent without a fallback search path
- prefer deterministic identifier resolution over fuzzy name matching wherever possible
- treat this document as the starting contract, then update it once real source behavior is verified in code
