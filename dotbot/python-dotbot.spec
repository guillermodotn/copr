Name:           python-dotbot
Version:        1.24.0
Release:        %autorelease
Summary:        A tool that bootstraps your dotfiles

License:        MIT
URL:            https://github.com/anishathalye/dotbot
Source0:        %{pypi_source dotbot}

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-pytest

%global _description %{expand:
Dotbot makes installing your dotfiles as easy as
'git clone $url && cd dotfiles && ./install', even on a freshly installed
system. It is designed to be lightweight and self-contained, with no external
dependencies. Dotbot can also be a drop-in replacement for any other tool you
were using to manage your dotfiles.}

%description %_description

%package -n python3-dotbot
Summary:        %{summary}
%{?python_provide:%python_provide python3-dotbot}

%description -n python3-dotbot %_description

%bcond check 0

%prep
%autosetup -p1 -n dotbot-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dotbot

%if %{with check}
%check
%pytest
%endif

%files -n python3-dotbot -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/dotbot

%changelog
%autochangelog
