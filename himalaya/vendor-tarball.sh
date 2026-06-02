#!/bin/bash
# This script is used as the Copr Custom source method script.
# Paste its contents into the Copr package configuration:
#   Packages > himalaya > Edit > Source type: Custom > Script
#
# Mock chroot: fedora-rawhide-x86_64
# Build dependencies: git rust cargo spectool
# Result directory: .

set -euo pipefail
VERSION="1.2.0"
NAME="himalaya"
# Clone spec repo
git clone https://github.com/guillermodotn/copr
cp copr/himalaya/himalaya.spec .
# Download upstream source
spectool -g himalaya.spec
# Generate vendor tarball
tar xf ${NAME}-${VERSION}.tar.gz
cd ${NAME}-${VERSION}
rm -f rust-toolchain.toml
cargo vendor --locked
cd ..
tar czf ${NAME}-${VERSION}-vendor.tar.gz ${NAME}-${VERSION}/vendor
rm -rf ${NAME}-${VERSION}
