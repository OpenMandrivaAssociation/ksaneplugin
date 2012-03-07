Name:          ksaneplugin
Summary:       KDE Scan Service
Version: 4.8.1
Release: 1
Epoch:         2
Group:         Graphical desktop/KDE
License:       GPLv2
URL:           http://www.kde.org
Source:        ftp://ftp.kde.org/pub/kde/stable/%version/src/%name-%version.tar.bz2
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libksane-devel >= 2:%{version}
Requires:      libksane 
Conflicts:     kdegraphics4-core < 2:4.6.90

%description
This is a KScan plugin that implements the scanning through libksane.

%files
%_kde_libdir/kde4/ksaneplugin.so
%_kde_services/ksane_scan_service.desktop

#----------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

