from pathlib import Path


def test_initiative_card_template_exists():
    assert Path("docs/hq/templates/initiative-card.md").exists()


def test_bd_pipeline_contract_mentions_core_fields():
    text = Path("docs/hq/bd-pipeline-contract.md").read_text()
    for field in ["name", "stage", "target_customer", "value_proposition", "decision_state", "metrics"]:
        assert field in text
