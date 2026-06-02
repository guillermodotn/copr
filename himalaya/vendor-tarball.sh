#!/bin/bash
# Generate vendored dependency tarball for himalaya
# Run this on a machine with cargo installed
set -euo pipefail

VERSION="1.2.0"
NAME="himalaya"

# Download and extract source
spectool -g himalaya.spec || {
    curl -LO "https://github.com/pimalaya/himalaya/archive/v${VERSION}/${NAME}-${VERSION}.tar.gz"
}

tar xf "${NAME}-${VERSION}.tar.gz"
cd "${NAME}-${VERSION}"

# Vendor all dependencies
cargo vendor

# Create the cargo config for vendored builds
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

cd ..

# Create vendored tarball
tar czf "${NAME}-${VERSION}-vendor.tar.gz" "${NAME}-${VERSION}/vendor" "${NAME}-${VERSION}/.cargo"

# Cleanup
rm -rf "${NAME}-${VERSION}"

echo ""
echo "Created: ${NAME}-${VERSION}-vendor.tar.gz"
echo "Upload this file alongside the spec to your Copr project."
