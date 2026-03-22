from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


Platform = Literal["playstation", "xbox", "pc", "switch"]


class FaceStats(BaseModel):
    model_config = ConfigDict(extra="forbid")

    pace: int = Field(ge=0, le=99)
    shooting: int = Field(ge=0, le=99)
    passing: int = Field(ge=0, le=99)
    dribbling: int = Field(ge=0, le=99)
    defending: int = Field(ge=0, le=99)
    physical: int = Field(ge=0, le=99)


class InGameStats(BaseModel):
    model_config = ConfigDict(extra="forbid")

    acceleration: int | None = Field(default=None, ge=0, le=99)
    sprint_speed: int | None = Field(default=None, ge=0, le=99)
    positioning: int | None = Field(default=None, ge=0, le=99)
    finishing: int | None = Field(default=None, ge=0, le=99)
    shot_power: int | None = Field(default=None, ge=0, le=99)
    long_shots: int | None = Field(default=None, ge=0, le=99)
    volleys: int | None = Field(default=None, ge=0, le=99)
    penalties: int | None = Field(default=None, ge=0, le=99)
    vision: int | None = Field(default=None, ge=0, le=99)
    crossing: int | None = Field(default=None, ge=0, le=99)
    free_kick_accuracy: int | None = Field(default=None, ge=0, le=99)
    short_passing: int | None = Field(default=None, ge=0, le=99)
    long_passing: int | None = Field(default=None, ge=0, le=99)
    curve: int | None = Field(default=None, ge=0, le=99)
    agility: int | None = Field(default=None, ge=0, le=99)
    balance: int | None = Field(default=None, ge=0, le=99)
    reactions: int | None = Field(default=None, ge=0, le=99)
    ball_control: int | None = Field(default=None, ge=0, le=99)
    dribbling: int | None = Field(default=None, ge=0, le=99)
    composure: int | None = Field(default=None, ge=0, le=99)
    interceptions: int | None = Field(default=None, ge=0, le=99)
    heading_accuracy: int | None = Field(default=None, ge=0, le=99)
    defensive_awareness: int | None = Field(default=None, ge=0, le=99)
    standing_tackle: int | None = Field(default=None, ge=0, le=99)
    sliding_tackle: int | None = Field(default=None, ge=0, le=99)
    jumping: int | None = Field(default=None, ge=0, le=99)
    stamina: int | None = Field(default=None, ge=0, le=99)
    strength: int | None = Field(default=None, ge=0, le=99)
    aggression: int | None = Field(default=None, ge=0, le=99)


class SourcePrice(BaseModel):
    model_config = ConfigDict(extra="forbid")

    source_name: str = Field(min_length=1, max_length=100)
    platform: Platform
    price: int = Field(ge=0)
    currency: str = Field(default="coins", min_length=1, max_length=16)
    observed_at: str | None = Field(
        default=None,
        description="ISO-8601 timestamp for when the price was observed.",
    )
    url: str | None = Field(default=None, max_length=500)


class ComparableCard(BaseModel):
    model_config = ConfigDict(extra="forbid")

    player_name: str = Field(min_length=1, max_length=100)
    base_card_type: str = Field(min_length=1, max_length=100)
    final_overall: int = Field(ge=0, le=99)
    positions: list[str] = Field(min_length=1)
    weak_foot: int | None = Field(default=None, ge=1, le=5)
    skill_moves: int | None = Field(default=None, ge=1, le=5)
    playstyles: list[str] = Field(default_factory=list)
    playstyles_plus: list[str] = Field(default_factory=list)
    face_stats: FaceStats
    in_game_stats: InGameStats | None = None
    platform: Platform
    source_prices: list[SourcePrice] = Field(default_factory=list)
    median_price_now: int = Field(ge=0)


class EvoCardInput(BaseModel):
    model_config = ConfigDict(extra="forbid")

    player_name: str = Field(min_length=1, max_length=100)
    base_card_type: str = Field(min_length=1, max_length=100)
    final_overall: int = Field(ge=0, le=99)
    positions: list[str] = Field(min_length=1)
    weak_foot: int = Field(ge=1, le=5)
    skill_moves: int = Field(ge=1, le=5)
    playstyles: list[str] = Field(default_factory=list)
    playstyles_plus: list[str] = Field(default_factory=list)
    face_stats: FaceStats
    in_game_stats: InGameStats | None = None
    platform: Platform
    source_prices: list[SourcePrice] = Field(default_factory=list)


class ValuationResponse(BaseModel):
    model_config = ConfigDict(extra="forbid")

    player_name: str = Field(min_length=1, max_length=100)
    base_card_type: str = Field(min_length=1, max_length=100)
    final_overall: int = Field(ge=0, le=99)
    positions: list[str] = Field(min_length=1)
    weak_foot: int = Field(ge=1, le=5)
    skill_moves: int = Field(ge=1, le=5)
    playstyles: list[str] = Field(default_factory=list)
    playstyles_plus: list[str] = Field(default_factory=list)
    face_stats: FaceStats
    in_game_stats: InGameStats | None = None
    platform: Platform
    source_prices: list[SourcePrice] = Field(default_factory=list)
    median_price_now: int = Field(ge=0)
    comparable_cards: list[ComparableCard] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0)
    explanation: str = Field(min_length=1, max_length=2000)
