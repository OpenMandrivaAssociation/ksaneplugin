Name:		ksaneplugin
Summary:	KDE Scan Service
Version:	15.12.0
Release:	2
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
%{_libdir}/kde4/ksaneplugin.so                                                                         
%{_datadir}/kde4/services/ksane_scan_service.desktop  

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

