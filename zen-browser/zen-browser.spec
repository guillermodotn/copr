%global install_dir /opt/zen-browser

Name:           zen-browser
Version:        1.20.2b
Release:        1%{?dist}
Summary:        Firefox-based browser focused on privacy and productivity

License:        MPL-2.0
URL:            https://github.com/zen-browser/desktop
Source0:        https://github.com/zen-browser/desktop/releases/download/%{version}/zen.linux-x86_64.tar.xz
Source1:        zen-browser.desktop

ExclusiveArch:  x86_64

# Skip RPATH checks — bundled pre-built libraries have non-standard RPATHs
%define         __brp_check_rpaths %{nil}

# Disable debug package — pre-built binaries have no debug info
%global         debug_package %{nil}

# Disable automatic dependency detection — the tarball bundles its own libs
AutoReqProv:    no

Requires:       alsa-lib
Requires:       dbus-glib
Requires:       fontconfig
Requires:       freetype
Requires:       gtk3
Requires:       libX11
Requires:       libXcomposite
Requires:       libXdamage
Requires:       libXext
Requires:       libXfixes
Requires:       libXrandr
Requires:       libXt
Requires:       libxcb
Requires:       mesa-libEGL
Requires:       nspr
Requires:       nss
Requires:       pango

Provides:       webclient


%description
Zen is a beautifully designed, privacy-focused, Firefox-based web browser
packed with features to boost your productivity. It includes workspaces,
compact mode, split view, and more — while caring about your experience,
not your data.


%prep
%setup -q -n zen


%build
# Pre-built binary — nothing to compile


%install
# Install the browser runtime
install -d %{buildroot}%{install_dir}
cp -a * %{buildroot}%{install_dir}/

# Launcher symlink
install -d %{buildroot}%{_bindir}
ln -s %{install_dir}/zen %{buildroot}%{_bindir}/zen-browser

# Desktop file
install -Dm0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/zen-browser.desktop

# Icons — extract from the bundled browser chrome
for size in 16 32 48 64 128; do
    icon=browser/chrome/icons/default/default${size}.png
    if [ -f "${icon}" ]; then
        install -Dm0644 "${icon}" \
            %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/zen-browser.png
    fi
done


%files
%{install_dir}/
%{_bindir}/zen-browser
%{_datadir}/applications/zen-browser.desktop
%{_datadir}/icons/hicolor/*/apps/zen-browser.png


%changelog
%autochangelog
