#!/usr/bin/env bash

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd "${DIR}"/

DESIGN_SYSTEM_VERSION="73.0.3"

TEMP_DIR=$(mktemp -d)

curl -L --url "https://github.com/ONSdigital/design-system/releases/download/$DESIGN_SYSTEM_VERSION/templates.zip" --output "${TEMP_DIR}"/templates.zip
unzip "${TEMP_DIR}"/templates.zip -d "${TEMP_DIR}"/templates
rm -rf rh_ui/templates/components
rm -rf rh_ui/templates/layout
mv "${TEMP_DIR}"/templates/templates/* rh_ui/templates/
rm -rf "${TEMP_DIR}"