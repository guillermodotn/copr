Name:           mdpeek
Version:        0.3.0
Release:        1%{?dist}
Summary:        Lightweight CLI markdown previewer with live reload (GTK4 backend)

License:        GPL-3.0-or-later
URL:            https://github.com/guillermodotn/mdpeek
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(libcmark-gfm)

Requires:       gtk4
Requires:       libadwaita
Requires:       webkitgtk6.0
Requires:       cmark-gfm-libs

%description
mdpeek renders GitHub Flavored Markdown in a native GTK4 window and
automatically refreshes when the file changes on disk.

Features include GFM support (tables, strikethrough, autolinks, task lists),
GitHub-style alert/admonition blocks, Mermaid diagram rendering, local image
support, pixel-perfect GitHub CSS rendering via WebKitGTK, and scroll position
preservation across reloads.

This package uses the GTK4 + WebKitGTK backend (~30 MB footprint).

%prep
%autosetup -n %{name}-%{version}

%build
%cmake -DMDPEEK_BACKEND=gtk
%cmake_build

%install
%cmake_install

%files
%doc README.md
%{_bindir}/mdpeek

%changelog
%autochangelog
