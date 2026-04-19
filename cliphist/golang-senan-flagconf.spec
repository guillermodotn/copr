# https://github.com/sentriz/flagconf
%global goipath         go.senan.xyz/flagconf
%global forgeurl        https://github.com/sentriz/flagconf
Version:                0.1.11

%gometa -L

%global archivename     flagconf-%{version}
%global golicenses      LICENSE
%global godocs          README.md

Name:           golang-senan-flagconf
Release:        %autorelease
Summary:        Extensions to Go's flag package for env vars and config files

License:        MIT
URL:            %{forgeurl}
Source:         %{forgeurl}/archive/v%{version}/%{archivename}.tar.gz

BuildArch:      noarch
BuildRequires:  go-rpm-macros

%global common_description %{expand:
Extensions to Go's flag package to support prefixed environment variables
and a simple config file format.}

%description %{common_description}

%gopkg

%prep
%goprep -k

%install
%gopkginstall

%files
%license LICENSE
%doc README.md
%gopkgfiles

%changelog
%autochangelog
