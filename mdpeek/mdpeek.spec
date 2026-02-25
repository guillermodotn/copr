Name:           mdpeek
Version:        0.1.0
Release:        1%{?dist}
Summary:        Lightweight CLI markdown previewer with live reload

License:        GPL-3.0-or-later
URL:            https://github.com/guillermodotn/mdpeek
Source0:        %%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(libcmark-gfm)

Requires:       gtk4
Requires:       webkitgtk6.0
Requires:       cmark-gfm-libs

%description
mdpeek renders GitHub Flavored Markdown in a native GTK4 window and
automatically refreshes when the file changes on disk.

Features include GFM support (tables, strikethrough, autolinks, task lists),
GitHub-style alert/admonition blocks, pixel-perfect GitHub CSS rendering via
WebKitGTK, and scroll position preservation across reloads.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/mdpeek

%changelog
* Wed Feb 25 2026 guillermodotn - 0.1.0-1
- Initial package
