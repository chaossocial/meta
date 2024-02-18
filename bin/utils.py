


def get_working_mastodon():
    from pathlib import Path
    from mastodon import Mastodon

    SCOPES = [
        "admin:read:accounts",
        "admin:read:domain_blocks",
        "admin:read:reports",
        "admin:write:accounts",
        "admin:write:domain_blocks",
        "admin:write:reports",
    ]

    if not Path(".mastodon-client.secret").absolute().exists():
        Mastodon.create_app(
            "meta.chaos.social automation",
            api_base_url="https://chaos.social",
            to_file=".mastodon-client.secret",
            scopes=SCOPES,
        )

    if not Path(".mastodon-usercred.secret").absolute().exists():
        mastodon = Mastodon(
            client_id=".mastodon-client.secret", api_base_url="https://chaos.social"
        )
        url = mastodon.auth_request_url(
            client_id=".mastodon-client.secret",
            scopes=SCOPES,
        )
        mastodon.log_in(
            code=input(f"Enter the code from {url}").strip(),
            to_file=".mastodon-usercred.secret",
            scopes=SCOPES,
        )
    else:
        mastodon = Mastodon(
            access_token=".mastodon-usercred.secret",
            api_base_url="https://chaos.social",
        )
    return mastodon
