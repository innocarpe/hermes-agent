from pathlib import Path


def test_discord_channel_topology_exists():
    assert Path("docs/hq/discord-channel-topology.md").exists()


def test_discord_channel_topology_mentions_recommended_channels():
    text = Path("docs/hq/discord-channel-topology.md").read_text()
    for channel in ["#bd-intake", "#bd-triage", "#bd-review", "#bd-decisions", "#bd-metrics", "#hq-ops"]:
        assert channel in text


def test_discord_channel_topology_mentions_core_controls():
    text = Path("docs/hq/discord-channel-topology.md").read_text()
    for key in ["allowed_channels", "free_response_channels", "no_thread_channels", "auto_thread", "require_mention", "channel_skill_bindings"]:
        assert key in text


def test_discord_channel_topology_mentions_bootstrap_channels():
    text = Path("docs/hq/discord-channel-topology.md").read_text()
    for key in ["bootstrap_guild_id", "bootstrap_channels", "Manage Channels"]:
        assert key in text


def test_discord_channel_bootstrap_templates_exist():
    assert Path("docs/hq/discord-bootstrap-config.yaml").exists()
    assert Path("docs/hq/discord-channel-id-mapping.template.yaml").exists()
    assert Path("docs/hq/discord-channel-policy.yaml").exists()
    assert Path("docs/hq/discord-channel-role-map.md").exists()
    assert Path("docs/hq/discord-channel-topics.yaml").exists()


def test_discord_channel_policy_mentions_recommended_defaults():
    text = Path("docs/hq/discord-channel-policy.yaml").read_text()
    for key in ["allowed_channels", "free_response_channels", "no_thread_channels", "channel_skill_bindings"]:
        assert key in text


def test_discord_channel_role_map_mentions_expansion_rule():
    text = Path("docs/hq/discord-channel-role-map.md").read_text()
    for key in ["01-전략", "04-채널", "06-재무", "09-아카이브", "Expansion rule for future channels", "channel_skill_bindings"]:
        assert key in text


def test_discord_channel_topics_file_mentions_activities():
    text = Path("docs/hq/discord-channel-topics.yaml").read_text()
    for key in ["01-전략", "02-제품", "04-채널", "09-아카이브", "activities", "topic"]:
        assert key in text


def test_discord_channel_operating_map_exists():
    assert Path("docs/hq/discord-channel-operating-map.md").exists()


def test_discord_channel_operating_map_mentions_all_channels():
    text = Path("docs/hq/discord-channel-operating-map.md").read_text()
    for channel in [
        "01-전략",
        "02-개인사업자-운영",
        "02-제품",
        "03-콘텐츠",
        "04-채널",
        "05-운영",
        "06-재무",
        "07-회고",
        "08-브랜딩",
        "09-아카이브",
    ]:
        assert channel in text
