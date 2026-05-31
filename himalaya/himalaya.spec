%bcond_without check

Name:           himalaya
Version:        1.2.0
Release:        1%{?dist}
Summary:        CLI to manage emails

License:        MIT
URL:            https://github.com/pimalaya/himalaya
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pkg-config
# Required by the keyring feature (pulled in by oauth2)
BuildRequires:  dbus-devel

# oauth2 feature requires keyring which uses dbus at runtime
Requires:       dbus-libs

ExclusiveArch:  %{rust_arches}

%description
Himalaya is a CLI to manage emails.

It supports IMAP, Maildir, SMTP, Sendmail and includes features such as
multi-account configuration, PGP via shell commands, and OAuth 2.0
authentication.

%prep
%autosetup -n %{name}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -f imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2

%build
%cargo_build -f imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies

%install
%cargo_install -f imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2

%if %{with check}
%check
%cargo_test -f imap,maildir,smtp,sendmail,wizard,pgp-commands,oauth2
%endif

%files
%license LICENSE LICENSE.dependencies
%doc README.md CHANGELOG.md config.sample.toml
%{_bindir}/himalaya

%changelog
* Sat May 31 2026 guillermodotn <guillerm0.n@outlook.es> - 1.2.0-1
- Initial package with oauth2 feature enabled
