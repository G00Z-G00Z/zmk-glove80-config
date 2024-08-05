#!/bin/bash

set -euo pipefail

python ./scripts/update-max-combo.py ./config/glove80.keymap ./config/glove80.conf

IMAGE=glove80-zmk-config-docker
BRANCH="${1:-main}"

docker build -t "$IMAGE" .
docker run --rm -v "$PWD:/config" -e UID="$(id -u)" -e GID="$(id -g)" -e BRANCH="$BRANCH" "$IMAGE"
