"""
Finds the maximun number of keys per combo and the max number of combo per key
It recieves these parameters:

python ./update-max-combo.py file.keymap file.conf

"""

import argparse
import re
from pathlib import Path
from functools import reduce
from collections import Counter


KEYMAP_RE = r"\s+key-positions .*<(.*)>"
KEYMAP_RE_SUB = r"$1"


# These are the values that need to be put in the conf file
CONFIG_MAX_COMBOS_PER_KEY_NAME = "CONFIG_ZMK_COMBO_MAX_COMBOS_PER_KEY"
CONFIG_MAX_KEYS_PER_COMBO_NAME = "CONFIG_ZMK_COMBO_MAX_KEYS_PER_COMBO"


def get_max_nums(filename: Path) -> tuple[int, int]:
    """
    Returns a tuple of (max_keys_per_combo, max_combos_per_key)

    """
    with open(filename, "r") as file:
        contents = file.read()

    keymap_contents: list[str] = re.findall(KEYMAP_RE, contents)

    def reduce_max_keys_per_combo(max_combo: int, match: str) -> int:
        if (keys_in_combo := match.count(" ") + 1) > max_combo:
            return keys_in_combo

        return max_combo

    max_keys_per_combo = reduce(reduce_max_keys_per_combo, keymap_contents, -1)

    all_string = Counter(" ".join(keymap_contents).split(" "))

    max_combo_per_key = all_string.most_common(1)[0][1]

    return max_keys_per_combo, max_combo_per_key


def update_value_config_file(
    conf_file: Path, max_keys_per_combo: int, max_combos_per_key
):

    with open(conf_file, "r") as file:
        content = file.read()

    subtitusions = {
        rf"{CONFIG_MAX_KEYS_PER_COMBO_NAME}=.*": rf"{CONFIG_MAX_KEYS_PER_COMBO_NAME}={max_keys_per_combo}",
        rf"{CONFIG_MAX_COMBOS_PER_KEY_NAME}=.*": rf"{CONFIG_MAX_COMBOS_PER_KEY_NAME}={max_combos_per_key}",
    }

    for pattern, replacement in subtitusions.items():
        content = re.sub(pattern, replacement, content, count=1)
        print(f"Updating combo config: {replacement}")

    with open(conf_file, "w") as file:
        file.write(content)


def main():

    parser = argparse.ArgumentParser(
        "combo_max", description="Recieves the keymap file"
    )

    parser.add_argument(
        "keymap_file",
        type=Path,
        default="config/glove80.keymap",
        help="Keymap file",
    )

    parser.add_argument(
        "config_file",
        type=Path,
        default="config/glove80.keymap",
        help="Keymap file",
    )

    args = parser.parse_args()

    keymap_file = Path(args.keymap_file)
    max_keys_per_combo, max_combos_per_key = get_max_nums(keymap_file)
    update_value_config_file(args.config_file, max_keys_per_combo, max_combos_per_key)


if __name__ == "__main__":
    main()

    pass
