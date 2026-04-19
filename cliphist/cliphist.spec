# https://github.com/sentriz/cliphist
%global goipath         go.senan.xyz/cliphist
Version:                0.7.0

%gometa

Name:           cliphist
Release:        %autorelease
Summary:        Wayland clipboard manager with support for multimedia

License:        GPL-3.0-only
URL:            https://github.com/sentriz/cliphist
Source0:        https://github.com/sentriz/cliphist/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  go-rpm-macros
BuildRequires:  golang(go.etcd.io/bbolt)
BuildRequires:  golang(github.com/rivo/uniseg)
BuildRequires:  golang(go.senan.xyz/flagconf)
BuildRequires:  golang(golang.org/x/image/bmp)

%global common_description %{expand:
Wayland clipboard manager with support for multimedia. It works with any
Wayland compositor that supports wlr-data-control-unstable-v1, such as
Sway and Hyprland. Cliphist listens for clipboard changes via wl-clipboard
and stores them in a local database, supporting text and images.}

%description %{common_description}

%prep
%goprep

%build
%gobuild -o %{gobuilddir}/bin/%{name} %{goipath}

%install
install -Dpm0755 %{gobuilddir}/bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc CHANGELOG.md readme.md version.txt
%{_bindir}/%{name}

%changelog
%autochangelog
