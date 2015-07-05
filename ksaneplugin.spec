Name:		ksaneplugin
Summary:	KDE Scan Service
Version:	15.04.3
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2
URL:		http://www.kde.org
Source:		http://download.kde.org/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libksane) >= 0.3.0
Requires:	libksane
Conflicts:	kdegraphics4-core < 2:4.6.90

%description
This is a KScan plugin that implements the scanning through libksane.

%files
%{_kde_libdir}/kde4/ksaneplugin.so
%{_kde_services}/ksane_scan_service.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

