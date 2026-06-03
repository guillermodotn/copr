Name:           mdpeek-qt
Version:        0.2.1
Release:        1%{?dist}
Summary:        Lightweight CLI markdown previewer with live reload (Qt6 backend)

License:        GPL-3.0-or-later
URL:            https://github.com/guillermodotn/mdpeek
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  pkgconfig(libcmark-gfm)

Requires:       qt6-qtbase
Requires:       qt6-qtwebengine
Requires:       cmark-gfm-libs

Conflicts:      mdpeek

%description
mdpeek renders GitHub Flavored Markdown in a native Qt6 window and
automatically refreshes when the file changes on disk.

Features include GFM support (tables, strikethrough, autolinks, task lists),
GitHub-style alert/admonition blocks, Mermaid diagram rendering, local image
support, pixel-perfect GitHub CSS rendering via QtWebEngine, and scroll position
preservation across reloads.

This package uses the Qt6 + QtWebEngine backend (Chromium-based, ~261 MB
footprint). For a lighter alternative, install the mdpeek package instead.

%prep
%autosetup -n %{name}-%{version} -c
mv mdpeek-%{version}/* .

%build
%cmake -DMDPEEK_BACKEND=qt
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/mdpeek

%changelog
%autochangelog
