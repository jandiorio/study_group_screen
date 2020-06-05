"""
Initial DevNet Study Group Skills Check - BASIC
"""
# --- Built-in pkgs

# --- Non built-in pkgs
import yaml

info = [
    {
        "first_name": "Gayle",
        "last_name": "Livermore",
        "company": "WWT",
        "email": "gayle.livermore@wwt.com",
        "github_username": "gliverm",
    }
]

with open("gayle_livermore.yaml", 'w') as file:
    yaml.dump(info, file)
