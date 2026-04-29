from app.services.ai_service import generate_plan

def test_generate_plan():
    result = generate_plan("Paris", 3, "food")
    
    assert result is not None
    assert isinstance(result, str)
    assert len(result) > 0