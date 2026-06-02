%bcond_without check

# Disable cargo-rpm-macros automatic behavior
%undefine __cargo_is_lib
%undefine crates_source

Name:           himalaya
Version:        1.2.0
Release:        %autorelease
Summary:        CLI to manage emails

# himalaya itself is MIT.
# Bundled dependencies have various licenses, see LICENSE.dependencies.
License:        MIT AND Apache-2.0 AND BSD-2-Clause AND BSD-3-Clause AND ISC AND Unicode-3.0 AND Zlib
URL:            https://github.com/pimalaya/himalaya
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# Vendored Rust dependencies, generated with: cargo vendor --locked
# See vendor-tarball.sh for instructions
Source1:        %{name}-%{version}-vendor.tar.gz

BuildRequires:  rust >= 1.85
BuildRequires:  cargo >= 1.85
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

ExcludeArch:    %{ix86}

%description
Himalaya is a CLI to manage emails.

It supports IMAP, Maildir, SMTP, Sendmail and includes features such as
multi-account configuration, PGP via shell commands, and OAuth 2.0
authentication.

%prep
%setup -q -n %{name}-%{version}
# Remove upstream rust-toolchain.toml that pins Rust 1.82.0
# (some vendored crates require edition2024 which needs >= 1.85)
rm -f rust-toolchain.toml
# Extract vendored dependencies
tar xf %{SOURCE1} --strip-components=1
# Set up cargo to use vendored sources
rm -rf .cargo
mkdir -p .cargo
cat > .cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
export CARGO_HOME="$PWD/.cargo"
cargo build --release --locked \
    --features imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2

%install
install -Dpm 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}

%if %{with check}
%check
export CARGO_HOME="$PWD/.cargo"
cargo test --release --locked \
    --features imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2
%endif

%files
%license LICENSE
%doc README.md CHANGELOG.md config.sample.toml
%{_bindir}/himalaya

%changelog
%autochangelog
