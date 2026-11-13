Name:           ghostty
Version:        1.4.0
Release:        1%{?dist}
Summary:        Fast, feature-rich, and cross-platform terminal emulator that uses platform-native UI and GPU acceleration

License:        MIT
URL:            https://github.com/ghostty-org/ghostty
Source0:        https://github.com/ghostty-org/ghostty/archive/refs/tags/v%{version}.tar.gz
Source1:        https://ziglang.org/download/0.17.0/zig-%{_arch}-linux-0.17.0.tar.xz

ExclusiveArch:  x86_64 aarch64

BuildRequires:  blueprint-compiler
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gtk4-devel
BuildRequires:  gtk4-layer-shell-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libpng-devel
BuildRequires:  mesa-libEGL-devel
BuildRequires:  oniguruma-devel
BuildRequires:  pandoc-cli
BuildRequires:  pixman-devel
BuildRequires:  pkgconf-pkg-config
BuildRequires:  wayland-protocols-devel
BuildRequires:  zlib-ng-compat-devel

Requires:       gtk4-layer-shell
Requires:       hicolor-icon-theme

%description
%{summary}.

%prep
%autosetup -n ghostty-%{version}

# Extract Zig 0.17.0 one level up so it stays outside the source tree
mkdir -p ../zig-0.17.0
tar -xf %{SOURCE1} --strip-components=1 -C ../zig-0.17.0

%build
# Ghostty builds and stages files in a single pass during %%install

%install
DESTDIR=%{buildroot} ../zig-0.17.0/zig build \
    --summary all \
    --prefix "%{_prefix}" \
    --prefix-lib-dir "%{_lib}" \
    -Dversion-string=%{version}-%{release} \
    -Doptimize=ReleaseFast \
    -Dcpu=baseline \
    -Dpie=true \
    -Demit-docs

%if 0%{?fedora} >= 42
rm -f "%{buildroot}%{_datadir}/terminfo/g/ghostty"
%endif

%find_lang com.mitchellh.ghostty

%files -f com.mitchellh.ghostty.lang
%license LICENSE
%{_bindir}/ghostty
%{_datadir}/applications/com.mitchellh.ghostty.desktop
%{_datadir}/bash-completion/completions/ghostty.bash
%{_datadir}/bat/syntaxes/ghostty.sublime-syntax
%{_datadir}/dbus-1/services/com.mitchellh.ghostty.service
%{_datadir}/fish/vendor_completions.d/ghostty.fish
%{_datadir}/ghostty
%{_datadir}/icons/hicolor/*/apps/com.mitchellh.ghostty.png
%{_datadir}/kio/servicemenus/com.mitchellh.ghostty.desktop
%{_datadir}/man/man1/ghostty.1*
%{_datadir}/man/man5/ghostty.5*
%{_datadir}/metainfo/com.mitchellh.ghostty.metainfo.xml
%{_datadir}/nautilus-python/extensions/ghostty.py
%{_datadir}/nvim/site/*/ghostty.vim
%{_datadir}/pkgconfig/libghostty-vt.pc
%{_datadir}/systemd/user/app-com.mitchellh.ghostty.service
%{_datadir}/vim/vimfiles/*/ghostty.vim
%{_datadir}/zsh/site-functions/_ghostty

%{_includedir}/ghostty
%{_libdir}/libghostty-vt.so
%{_libdir}/libghostty-vt.so.0
%{_libdir}/libghostty-vt.so.0.*
%{_datadir}/terminfo/x/xterm-ghostty
%if 0%{?fedora} < 42
%{_datadir}/terminfo/g/ghostty
%endif

%changelog
%autochangelog
