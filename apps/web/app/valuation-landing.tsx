"use client";

import { FormEvent, useState } from "react";

import type { LandingPageContent } from "../lib/content";

type Platform = "playstation" | "xbox" | "pc" | "switch";

interface FaceStats {
  pace: number;
  shooting: number;
  passing: number;
  dribbling: number;
  defending: number;
  physical: number;
}

interface ValuationRequest {
  player_name: string;
  base_card_type: string;
  final_overall: number;
  positions: string[];
  weak_foot: number;
  skill_moves: number;
  playstyles: string[];
  playstyles_plus: string[];
  face_stats: FaceStats;
  platform: Platform;
  source_prices: SourcePrice[];
}

interface SourcePrice {
  source_name: string;
  platform: Platform;
  price: number;
  currency: string;
  observed_at: string | null;
  url: string | null;
}

interface ComparableCard {
  player_name: string;
  base_card_type: string;
  final_overall: number;
  positions: string[];
  weak_foot: number | null;
  skill_moves: number | null;
  playstyles: string[];
  playstyles_plus: string[];
  face_stats: FaceStats;
  platform: Platform;
  median_price_now: number;
}

interface ValuationResponse extends ValuationRequest {
  in_game_stats?: Record<string, number | null> | null;
  median_price_now: number;
  comparable_cards: ComparableCard[];
  confidence: number;
  explanation: string;
  source_prices: SourcePrice[];
}

interface FormState {
  playerName: string;
  cardType: string;
  overall: string;
  positions: string;
  weakFoot: string;
  skillMoves: string;
  playstyles: string;
  playstylesPlus: string;
  pace: string;
  shooting: string;
  passing: string;
  dribbling: string;
  defending: string;
  physical: string;
  platform: Platform;
}

interface EvoLandingPageProps {
  apiBaseUrl: string;
  content: LandingPageContent;
}

const initialFormState: FormState = {
  playerName: "Jude Bellingham",
  cardType: "Rare Gold",
  overall: "91",
  positions: "CM, CAM",
  weakFoot: "4",
  skillMoves: "4",
  playstyles: "Incisive Pass, Technical",
  playstylesPlus: "Pinged Pass",
  pace: "84",
  shooting: "83",
  passing: "88",
  dribbling: "89",
  defending: "82",
  physical: "86",
  platform: "playstation",
};

const platformOptions: Platform[] = ["playstation", "xbox", "pc", "switch"];

const statFields: Array<keyof FaceStats> = [
  "pace",
  "shooting",
  "passing",
  "dribbling",
  "defending",
  "physical",
];

function parseListField(value: string) {
  return value
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function toNumber(value: string) {
  return Number.parseInt(value, 10);
}

function formatCoins(value: number) {
  return new Intl.NumberFormat("en-GB").format(value);
}

async function readApiError(response: Response) {
  const responseText = (await response.text()).trim();
  return responseText || "Unable to value card right now.";
}

function buildValuationRequest(formState: FormState): ValuationRequest {
  return {
    player_name: formState.playerName.trim(),
    base_card_type: formState.cardType.trim(),
    final_overall: toNumber(formState.overall),
    positions: parseListField(formState.positions),
    weak_foot: toNumber(formState.weakFoot),
    skill_moves: toNumber(formState.skillMoves),
    playstyles: parseListField(formState.playstyles),
    playstyles_plus: parseListField(formState.playstylesPlus),
    face_stats: {
      pace: toNumber(formState.pace),
      shooting: toNumber(formState.shooting),
      passing: toNumber(formState.passing),
      dribbling: toNumber(formState.dribbling),
      defending: toNumber(formState.defending),
      physical: toNumber(formState.physical),
    },
    platform: formState.platform,
    source_prices: [],
  };
}

export function EvoLandingPage({ apiBaseUrl, content }: EvoLandingPageProps) {
  const [formState, setFormState] = useState<FormState>(initialFormState);
  const [result, setResult] = useState<ValuationResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [isSubmitting, setIsSubmitting] = useState(false);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setIsSubmitting(true);
    setError(null);

    const payload = buildValuationRequest(formState);

    try {
      const response = await fetch(`${apiBaseUrl}/valuation/evo`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(await readApiError(response));
      }

      const data = (await response.json()) as ValuationResponse;
      setResult(data);
    } catch (submissionError) {
      setResult(null);
      setError(
        submissionError instanceof Error
          ? submissionError.message
          : "Something went wrong while contacting the valuation API.",
      );
    } finally {
      setIsSubmitting(false);
    }
  }

  return (
    <main className="landing-shell">
      <section className="landing-intro">
        <p className="landing-badge">{content.productName} valuation</p>
        <h1>{content.headline}</h1>
        <p className="landing-copy">{content.description}</p>
      </section>

      <section className="landing-grid">
        <form className="panel panel-form" onSubmit={handleSubmit}>
          <div className="panel-heading">
            <div>
              <p className="panel-kicker">Evo input form</p>
              <h2>Card details</h2>
            </div>
            <a href={`${apiBaseUrl}/health`} target="_blank" rel="noreferrer">
              {content.healthLinkLabel}
            </a>
          </div>

          <div className="form-grid">
            <label className="field">
              <span>Player name</span>
              <input
                value={formState.playerName}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    playerName: event.target.value,
                  }))
                }
                placeholder="Jude Bellingham"
                required
              />
            </label>

            <label className="field">
              <span>Card type</span>
              <input
                value={formState.cardType}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    cardType: event.target.value,
                  }))
                }
                placeholder="Rare Gold"
                required
              />
            </label>

            <label className="field">
              <span>Overall</span>
              <input
                type="number"
                min="0"
                max="99"
                value={formState.overall}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    overall: event.target.value,
                  }))
                }
                required
              />
            </label>

            <label className="field">
              <span>Platform</span>
              <select
                value={formState.platform}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    platform: event.target.value as Platform,
                  }))
                }
              >
                {platformOptions.map((platform) => (
                  <option key={platform} value={platform}>
                    {platform}
                  </option>
                ))}
              </select>
            </label>

            <label className="field field-full">
              <span>Positions</span>
              <input
                value={formState.positions}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    positions: event.target.value,
                  }))
                }
                placeholder="CM, CAM"
                required
              />
            </label>

            <label className="field">
              <span>Weak foot</span>
              <input
                type="number"
                min="1"
                max="5"
                value={formState.weakFoot}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    weakFoot: event.target.value,
                  }))
                }
                required
              />
            </label>

            <label className="field">
              <span>Skill moves</span>
              <input
                type="number"
                min="1"
                max="5"
                value={formState.skillMoves}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    skillMoves: event.target.value,
                  }))
                }
                required
              />
            </label>

            <label className="field field-full">
              <span>Playstyles</span>
              <input
                value={formState.playstyles}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    playstyles: event.target.value,
                  }))
                }
                placeholder="Incisive Pass, Technical"
              />
            </label>

            <label className="field field-full">
              <span>Playstyles+</span>
              <input
                value={formState.playstylesPlus}
                onChange={(event) =>
                  setFormState((current) => ({
                    ...current,
                    playstylesPlus: event.target.value,
                  }))
                }
                placeholder="Pinged Pass"
              />
            </label>
          </div>

          <div className="stats-section">
            <div className="stats-heading">
              <p className="panel-kicker">Face stats</p>
              <span>0-99</span>
            </div>
            <div className="stats-grid">
              {statFields.map((stat) => (
                <label className="field" key={stat}>
                  <span>{stat}</span>
                  <input
                    type="number"
                    min="0"
                    max="99"
                    value={formState[stat]}
                    onChange={(event) =>
                      setFormState((current) => ({
                        ...current,
                        [stat]: event.target.value,
                      }))
                    }
                    required
                  />
                </label>
              ))}
            </div>
          </div>

          <button className="submit-button" type="submit" disabled={isSubmitting}>
            {isSubmitting ? "Submitting..." : "Get valuation"}
          </button>
        </form>

        <aside className="panel panel-results">
          <div className="panel-heading">
            <div>
              <p className="panel-kicker">Results panel</p>
              <h2>Valuation output</h2>
            </div>
          </div>

          {error ? <p className="status-message status-error">{error}</p> : null}

          {!result && !error ? (
            <div className="empty-state">
              <p className="empty-value">Awaiting submission</p>
              <p>
                Submit the form to render the API response, including valuation,
                explanation, sources, and comparable cards.
              </p>
            </div>
          ) : null}

          {result ? (
            <div className="results-stack">
              <div className="result-hero">
                <div>
                  <p className="result-label">Estimated value</p>
                  <p className="result-price">{formatCoins(result.median_price_now)} coins</p>
                </div>
                <div className="confidence-chip">
                  {Math.round(result.confidence * 100)}% confidence
                </div>
              </div>

              <div className="result-summary">
                <div>
                  <span>Player</span>
                  <strong>{result.player_name}</strong>
                </div>
                <div>
                  <span>Card</span>
                  <strong>{result.base_card_type}</strong>
                </div>
                <div>
                  <span>Overall</span>
                  <strong>{result.final_overall}</strong>
                </div>
                <div>
                  <span>Platform</span>
                  <strong>{result.platform}</strong>
                </div>
              </div>

              <div className="result-section">
                <h3>Explanation</h3>
                <p>{result.explanation}</p>
              </div>

              <div className="result-section">
                <h3>Source prices</h3>
                <div className="list-stack">
                  {result.source_prices.map((source) => (
                    <div className="list-card" key={`${source.source_name}-${source.platform}`}>
                      <strong>{source.source_name}</strong>
                      <span>
                        {formatCoins(source.price)} {source.currency}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              <div className="result-section">
                <h3>Comparable cards</h3>
                <div className="list-stack">
                  {result.comparable_cards.map((card) => (
                    <div className="list-card" key={`${card.player_name}-${card.final_overall}`}>
                      <div>
                        <strong>{card.player_name}</strong>
                        <p>
                          {card.base_card_type} {"\u00b7"} {card.positions.join(", ")}
                        </p>
                      </div>
                      <span>{formatCoins(card.median_price_now)} coins</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ) : null}
        </aside>
      </section>
    </main>
  );
}
