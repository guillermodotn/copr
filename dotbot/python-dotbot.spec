Name:           python-dotbot
Version:        1.24.1
Release:        %autorelease
Summary:        A tool that bootstraps your dotfiles

License:        MIT
URL:            https://github.com/anishathalye/dotbot
Source0:        %{pypi_source dotbot}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
Dotbot makes installing your dotfiles as easy as
'git clone $url && cd dotfiles && ./install', even on a freshly installed
system. It is designed to be lightweight and self-contained, with no external
dependencies. Dotbot can also be a drop-in replacement for any other tool you
were using to manage your dotfiles.}

%description %{_description}

%package -n python3-dotbot
Summary:        %{summary}

%description -n python3-dotbot %{_description}

%prep
%autosetup -p1 -n dotbot-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l dotbot

# Tests require a real home directory, filesystem symlink operations,
# and git, which are not available in the mock build environment.
# %%check
# %%pytest

%files -n python3-dotbot -f %{pyproject_files}
%doc README.md
%{_bindir}/dotbot

%changelog
%autochangelog
