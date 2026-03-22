from fastapi import APIRouter

from app.schemas.valuation import EvoCardInput, ValuationResponse
from app.services.valuation_service import build_valuation_response


router = APIRouter(prefix="/valuation", tags=["valuation"])


@router.post("", response_model=ValuationResponse)
def value_card(card: EvoCardInput) -> ValuationResponse:
    return build_valuation_response(card)


@router.post("/evo", response_model=ValuationResponse)
def value_evo_card(card: EvoCardInput) -> ValuationResponse:
    return build_valuation_response(card)
