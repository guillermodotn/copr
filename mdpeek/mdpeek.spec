Name:           mdpeek
Version:        0.2.1
Release:        1%{?dist}
Summary:        Lightweight CLI markdown previewer with live reload

License:        GPL-3.0-or-later
URL:            https://github.com/guillermodotn/mdpeek
Source0:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cmake >= 3.16
BuildRequires:  gcc
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
* Thu Apr 17 2026 guillermodotn - 0.2.1-1
- Fix local image loading in the viewer
- Intercept right-click reload to re-render markdown and preserve scroll
  position across all reloads
- Update README with screenshot, full feature list, and dependency graph

* Thu Mar 12 2026 guillermodotn - 0.2.0-1
- Render Mermaid diagrams in fenced code blocks via Mermaid.js
- Redirect stderr to /dev/null to silence GTK/WebKit/Mesa noise
- Open clicked links in the default browser
- Switch to libadwaita for system theme integration and add Escape to close
- Update COPR badge

* Wed Feb 25 2026 guillermodotn - 0.1.0-1
- Initial package
