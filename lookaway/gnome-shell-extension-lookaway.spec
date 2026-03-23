%global uuid        lookaway@gnome-extension
%global extdir      %{_datadir}/gnome-shell/extensions/%{uuid}

Name:           gnome-shell-extension-lookaway
Version:        1.0.0
Release:        1%{?dist}
Summary:        GNOME Shell extension for eye strain prevention using the 20/20/20 rule

License:        GPL-3.0-or-later
URL:            https://github.com/guillermodotn/lookaway
Source0:        https://github.com/guillermodotn/lookaway/archive/refs/tags/v%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  glib2

Requires:       gnome-shell >= 45

%description
LookAway is a GNOME Shell extension that protects your eyes from screen strain
using the 20/20/20 rule. Every 20 minutes of screen time, it reminds you to
look at something 20 feet (~6 metres) away for 20 seconds.

A countdown timer sits in the top bar with an eye icon. When the timer reaches
zero, the icon and text flash red and the eye icon blinks to grab your
attention. Both the screen time and eye rest durations are configurable through
a preferences dialog.


%prep
%autosetup -n lookaway-%{version}


%build
# Compile GSettings schema (bundled with the extension)
glib-compile-schemas schemas/


%install
# Extension files
install -d %{buildroot}%{extdir}
install -p -m 0644 metadata.json   %{buildroot}%{extdir}/
install -p -m 0644 extension.js    %{buildroot}%{extdir}/
install -p -m 0644 prefs.js        %{buildroot}%{extdir}/
install -p -m 0644 stylesheet.css  %{buildroot}%{extdir}/

# GSettings schema — bundled inside the extension directory
install -d %{buildroot}%{extdir}/schemas
install -p -m 0644 schemas/org.gnome.shell.extensions.lookaway.gschema.xml \
    %{buildroot}%{extdir}/schemas/
install -p -m 0644 schemas/gschemas.compiled \
    %{buildroot}%{extdir}/schemas/


%files
%license LICENSE
%doc README.md
%{extdir}/


%changelog
* Mon Mar 23 2026 guillermodotn - 1.0.0-1
- Initial RPM package
- 20/20/20 rule countdown timer in the GNOME top bar
- Flashing red text and blinking eye icon on eye rest
- Configurable screen time and eye rest durations
- Preferences dialog with libadwaita
