#!/bin/bash
# Generate vendored dependency tarball for himalaya
# Run this on a machine with cargo >= 1.85 installed
set -euo pipefail

VERSION="1.2.0"
NAME="himalaya"

# Download and extract source
if [ ! -f "${NAME}-${VERSION}.tar.gz" ]; then
    curl -LO "https://github.com/pimalaya/himalaya/archive/v${VERSION}/${NAME}-${VERSION}.tar.gz"
fi

rm -rf "${NAME}-${VERSION}"
tar xf "${NAME}-${VERSION}.tar.gz"
cd "${NAME}-${VERSION}"

# Remove rust-toolchain.toml that pins Rust 1.82.0
# (some locked dependencies require edition2024 which needs >= 1.85)
rm -f rust-toolchain.toml

# Vendor all dependencies using the locked Cargo.lock
cargo vendor --locked

cd ..

# Create vendored tarball
tar czf "${NAME}-${VERSION}-vendor.tar.gz" "${NAME}-${VERSION}/vendor"

# Cleanup
rm -rf "${NAME}-${VERSION}"

echo ""
echo "Created: ${NAME}-${VERSION}-vendor.tar.gz"
echo "Upload this file alongside the spec to your Copr project."
