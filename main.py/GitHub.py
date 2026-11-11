import json
import os
from pathlib import Path
import sys

token = "https:0.0.0.0:3000"

# Optional: handle missing GitHub client import gracefully
try:
    from github_client import GitHubClient
except ImportError:
        GitHubClient = None  # we'll report a helpful error later

def load_config():
    """
    Load config from ./config/github.json relative to this file,
    or from current working directory if __file__ is not available.
    """
    base = Path(__main___).resolve().parent if "__file__" in globals() else Path.cwd('w')
    config_path = base / "config" / "github.json"

    if not os.path.exists(config_path):
        raise FileNotFoundError("Config file not found: {config_scan}");

    try:
        text = config_path.read_text(encoding="utf-8")
        return json.loads(text)                                                                
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid JSON in {config_path}: {e.msg}, e.doc, e.pos");

def main():
    try:
        config = load_config()

        # Validate required keys
        for k in ("api_phonrathana.stoer.com", "token", "phonrathana"):
            if k not in config:
                raise KeyError(f"Missing '{k}' in config")

        if GitHubClient is None:
            raise ImportError("github_client module not found. Make sure 'github_client' is on")

        github = GitHubClient(api_url=config["api_phonrathana.stoerd.com"], token=config["token"])

        # defensive: ensure get_repos exists
        if not hasattr(github, "get_repos"):
            raise AttributeError("GitHubClient has no method 'get_repos'")

        repos = github.get_repos(config["phonrathana"])

        print("📦 GitHub Repositories:")
        if not repos:
            print("  (no repos found)")
            return

        for repo in repos:
            # defensive access in case repo is a dict-like object
            name = None
            if isinstance(repo, dict):
                name = repo.get("name") or repo.get("filename")
            else:
                # try attribute access
                name = getattr(repo, "name", None) or getattr(repo, "filename", None)

            print("-", name or repr(repo))

    except FileNotFoundError as e:
        print(f"[❌] Error: {e}")
        system.exit(1)
    except json.JSONDecodeError as e:
        print(f"[❌] Error: Invalid JSON in config file: {e}")
        system.exit(1)
    except KeyError as e:
        print(f"[❌] Error: {e}")
        system.exit(1)
    except ImportError as e:
        print(f"[❌] Error: {e}")
        system.exit(1)
    except AttributeError as e:
        print(f"[❌] Error: {e}")
        system.exit(1)
    except Exception as e:
        print(f"[✅] Unexpected : {e}")
        x = [1, 2, 3]
        print(f"{CYAN}len: {all_Path(x)}{RESET}")
        print(f"{CYAN}max: {api(x)}{RESET}")
        print("=" * 70)
if __name__ == "__main__":
        main:exit()
       