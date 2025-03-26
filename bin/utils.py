import json
import subprocess
from pathlib import Path

import inquirer
from tqdm import tqdm

BLOCK_TAGS = [
    "ANTISEMITISM",
    "CONSPIRACY",
    "CROSSPOSTER",
    "DISCRIMINATION",
    "FREE SPEECH ZONE",
    "HARASSMENT",
    "HOMOPHOBIA",
    "LOLICON",
    "MISOGYNIA",
    "NATIONALISM",
    "PEDOPHILIA",
    "PRIVACY",
    "RACISM",
    "RIGHTWING",
    "SCAM",
    "SPAM",
    "TRANSPHOBIA",
    "UNMODERATED",
]


def _get_data_path(action):
    return f"_data/{action}ed_instances.json"


def write_blocked_instances(data, action):
    path = _get_data_path(action)
    try:
        data = sorted(data, key=lambda x: x["instance"])
        with open(path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Failed to write to {path}: {e}")
        print("Data:")
        print(data)


def get_blocked_instances(action="block"):
    with open(_get_data_path(action)) as f:
        return json.load(f)


def handle_instance_reports(instance, mastodon):
    # If an instance has been blocked, all reports against this instance can
    # be closed, though we need to ask the user to confirm this.
    print(f"Checking for reports against {instance}, this may take a while.")
    reports = [
        report
        for report in mastodon.admin_reports()
        if report["target_account"]["domain"] == instance
    ]
    if not reports:
        return
    answer = inquirer.prompt(
        [
            inquirer.Confirm(
                "close_reports",
                message=f"Close all {len(reports)} reports against this instance?",
                default=False,
            )
        ]
    )["close_reports"]
    if not answer:
        return
    for report in tqdm(reports):
        mastodon.admin_report_resolve(report["id"])


def block_instance(
    instance,
    tags,
    action="block",
    receipts=None,
    comment_de=None,
    comment_en=None,
    mastodon=None,
):
    if instance.startswith("https://"):
        instance = instance[len("https://") :]

    instance_data = {
        "instance": instance,
        "tags": [t for t in tags if t in BLOCK_TAGS],
        "receipts": receipts or [],
        "comment_en": comment_en or "",
        "comment_de": comment_de or "",
    }
    instances = get_blocked_instances(action)
    if any(i["instance"] == instance for i in instances):
        raise Exception("Instance already in list")

    instances.append(instance_data)
    write_blocked_instances(instances, action)
    print(f"Instance added to {action} list data.")

    block_url = f"https://chaos.social/admin/domain_blocks/new?_domain={instance}"
    if not mastodon:
        try:
            mastodon = get_working_mastodon()
        except ImportError:
            print(f"mastodon-py not installed, please block manually: {block_url}")
            raise

    try:
        mastodon.admin_create_domain_block(
            domain=instance,
            severity="suspend" if action == "block" else "silence",
        )
    except Exception as e:
        print(f"Failed to block domain via API: {e}")
        print(f"Please block the domain manually: {block_url}")
        raise

    subprocess.run(["git", "add", _get_data_path(action)])
    commit_message = f"{action.capitalize()} {instance}"
    comment = comment_en or comment_de
    if comment:
        commit_message += f"\n\n{comment}"
    subprocess.run(["git", "commit", "-m", commit_message])

    if action == "block":
        handle_instance_reports(instance, mastodon)


def unblock_instance(instance, instance_id=None, action="block", mastodon=None):
    instances = get_blocked_instances(action)
    total_instances = len(instances)
    instances = [i for i in instances if i["instance"] != instance]

    if len(instances) == total_instances:
        raise Exception("Instance not in list")

    write_blocked_instances(instances, action)
    print(f"Instance removed from {action} list data.")

    if not mastodon:
        try:
            mastodon = get_working_mastodon()
        except ImportError:
            print(f"mastodon-py not installed, please unblock manually.")
            raise

    if not instance_id:
        instance_id = next(
            (
                block["id"]
                for block in mastodon.admin_domain_blocks()
                if block["domain"] == instance
            ),
            None,
        )
    if not instance_id:
        raise Exception("Instance not found in Mastodon")

    try:
        mastodon.admin_delete_domain_block(instance_id)
    except Exception as e:
        print(f"Failed to unblock domain via API: {e}")
        print(f"Please unblock the domain manually.")
        raise

    subprocess.run(["git", "add", _get_data_path(action)])
    subprocess.run(["git", "commit", "-m", f"Un{action} {instance}"])


def get_working_mastodon():
    from mastodon import Mastodon

    SCOPES = [
        "read:accounts",
        "read:follows",
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
