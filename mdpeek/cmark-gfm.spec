Name:           cmark-gfm
Version:        0.29.0.gfm.13
Release:        1%{?dist}
Summary:        GitHub's fork of cmark, a CommonMark parsing and rendering library

License:        BSD-2-Clause AND MIT
URL:            https://github.com/github/cmark-gfm
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake >= 3.0
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make

%description
cmark-gfm is GitHub's fork of cmark, a C library for parsing CommonMark
(Markdown) documents to an AST and rendering to HTML, groff man, LaTeX,
CommonMark, or an XML representation. It includes GitHub Flavored Markdown
extensions: tables, strikethrough, autolinks, task lists, and tag filtering.

%package libs
Summary:        Shared libraries for cmark-gfm

%description libs
Shared libraries for cmark-gfm, providing CommonMark parsing and rendering
with GitHub Flavored Markdown extensions.

%package devel
Summary:        Development files for cmark-gfm
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel
Headers, static libraries, pkg-config, and CMake files for developing
applications that use cmark-gfm.

%prep
%autosetup -n %{name}-%{version}

%build
%cmake \
    -DCMARK_TESTS=OFF \
    -DCMARK_SHARED=ON \
    -DCMARK_STATIC=ON
%cmake_build

%install
%cmake_install

%files
%license COPYING
%doc README.md
%{_bindir}/cmark-gfm
%{_mandir}/man1/cmark-gfm.1*

%files libs
%license COPYING
%{_libdir}/libcmark-gfm.so.*
%{_libdir}/libcmark-gfm-extensions.so.*

%files devel
%{_includedir}/cmark-gfm.h
%{_includedir}/cmark-gfm_export.h
%{_includedir}/cmark-gfm_version.h
%{_includedir}/cmark-gfm-extension_api.h
%{_includedir}/cmark-gfm-core-extensions.h
%{_libdir}/libcmark-gfm.so
%{_libdir}/libcmark-gfm-extensions.so
%{_libdir}/libcmark-gfm.a
%{_libdir}/libcmark-gfm-extensions.a
%{_libdir}/pkgconfig/libcmark-gfm.pc
%{_libdir}/cmake/cmark-gfm.cmake
%{_libdir}/cmake/cmark-gfm-release.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions.cmake
%{_libdir}/cmake-gfm-extensions/cmark-gfm-extensions-release.cmake
%{_mandir}/man3/cmark-gfm.3*

%changelog
* Wed Feb 25 2026 gleiro - 0.29.0.gfm.13-1
- Initial package
