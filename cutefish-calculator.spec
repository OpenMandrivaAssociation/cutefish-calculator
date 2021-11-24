%define oname calculator

Name:           cutefish-calculator
Version:        0.4
Release:        1
Summary:        Calculator
License:        GPL-3.0-or-later
Group:          Productivity/Scientific
URL:            https://github.com/cutefishos/cutefish-calculator
Source:         https://github.com/cutefishos/calculator/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  qmake5
BuildRequires:  cmake
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5QuickControls2)


Requires:       fishui

%description
cutefish-calculator - CutefishOS Calculator


%prep
%autosetup -n %{oname}-%{version} -p1
sed -i 's/\(Name=\)\(Calculator\)/\1Cutefish \2/' %{name}.desktop

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files  -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
