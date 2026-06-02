%bcond_without check

Name:           himalaya
Version:        1.2.0
Release:        1%{?dist}
Summary:        CLI to manage emails

# himalaya itself is MIT.
# Bundled dependencies have various licenses, see LICENSE.dependencies.
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND Unicode-3.0 AND Zlib
URL:            https://github.com/pimalaya/himalaya
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Generated with: cargo vendor
# See vendor-tarball.sh for instructions
Source1:        %{name}-%{version}-vendor.tar.gz

BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
# Required by the keyring feature (pulled in by oauth2)
BuildRequires:  dbus-devel

# oauth2 feature requires keyring which uses dbus at runtime
Requires:       dbus-libs

# Bundled dependencies (vendored Rust crates)
Provides:       bundled(crate(email-lib)) = 0.27.0
Provides:       bundled(crate(mml-lib)) = 1.0.14
Provides:       bundled(crate(pimalaya-tui)) = 0.3.1
Provides:       bundled(crate(secret-lib)) = 1.0.0
Provides:       bundled(crate(shellexpand-utils)) = 0.2.1
Provides:       bundled(crate(ariadne)) = 0.2.0

ExclusiveArch:  %{rust_arches}

%description
Himalaya is a CLI to manage emails.

It supports IMAP, Maildir, SMTP, Sendmail and includes features such as
multi-account configuration, PGP via shell commands, and OAuth 2.0
authentication.

%prep
%autosetup -n %{name}-%{version} -p1
# Extract vendored dependencies
tar xf %{SOURCE1} --strip-components=1
# Use vendored sources
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_HOME="$PWD/.cargo"
cargo build --release \
    --features imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2

%install
install -Dpm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%if %{with check}
%check
export CARGO_HOME="$PWD/.cargo"
cargo test --release \
    --features imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md config.sample.toml
%{_bindir}/himalaya

%changelog
* Mon Jun 02 2026 guillermodotn <guillerm0.n@outlook.es> - 1.2.0-1
- Switch to vendored dependencies for Copr builds

* Sat May 31 2026 guillermodotn <guillerm0.n@outlook.es> - 1.2.0-1
- Initial package with oauth2 feature enabled
