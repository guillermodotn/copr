Name:           flagconf
Version:        0.1.11
Release:        %autorelease
Summary:        Extensions to Go's flag package to support prefixed environment variables and a simple config file format

License:        MIT
URL:            https://github.com/sentriz/flagconf
Source:         https://github.com/sentriz/flagconf/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  go-rpm-macros
BuildRequires:  golang

# Go import path
%global goipath         go.senan.xyz/flagconf

# Generate Go packaging metadata
%gometa -L

# Define archivename for tarball extraction
%global archivename     %{name}-%{version}

# License and docs to install
%global golicenses      LICENSE
%global godocs          README.md

%global common_description %{expand:
Extensions to Go's flag package to support prefixed environment variables and a
simple config file format.}

%description %{common_description}

# Define Go package
%gopkg

%prep
%goprep

%build
# Library package - no binary to build

%install
# Install license and docs from the nested directory
install -dm 0755 %{buildroot}%{_licensedir}/%{name}
install -pm 0644 %{archivename}/LICENSE %{buildroot}%{_licensedir}/%{name}/

install -dm 0755 %{buildroot}%{_docdir}/%{name}
install -pm 0644 %{archivename}/README.md %{buildroot}%{_docdir}/%{name}/

%gopkginstall

%files
%license %{_licensedir}/%{name}/LICENSE
%doc %{_docdir}/%{name}/README.md

# Include Go package files
%gopkgfiles

%changelog
%autochangelog
