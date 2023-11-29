%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6GuiAddons
%define devname %mklibname KF6GuiAddons -d
#define git 20231103

Name: kf6-kguiaddons
Version: 5.246.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kguiaddons/-/archive/master/kguiaddons-master.tar.bz2#/kguiaddons-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{version}/kguiaddons-%{version}.tar.xz
%endif
Summary: Utilities for graphical user interfaces
URL: https://invent.kde.org/frameworks/kguiaddons
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(PlasmaWaylandProtocols)
BuildRequires: cmake(Qt6WaylandClient)
Requires: %{libname} = %{EVRD}

%description
Utilities for graphical user interfaces

%package -n kde-geo-scheme-handler
Summary: Geo scheme handler for KDE (5 and 6)
Group: System/Libraries

%description -n kde-geo-scheme-handler
Geo scheme handler for KDE (5 and 6)

%package -n %{libname}
Summary: Utilities for graphical user interfaces
Group: System/Libraries
Requires: %{name} = %{EVRD}
Requires: kde-geo-scheme-handler = %{EVRD}

%description -n %{libname}
Utilities for graphical user interfaces

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Utilities for graphical user interfaces

%prep
%autosetup -p1 -n kguiaddons-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_datadir}/qlogging-categories6/kguiaddons.*

%files -n kde-geo-scheme-handler
%{_bindir}/kde-geo-uri-handler
%{_datadir}/applications/google-maps-geo-handler.desktop
%{_datadir}/applications/openstreetmap-geo-handler.desktop
%{_datadir}/applications/qwant-maps-geo-handler.desktop
%{_datadir}/applications/wheelmap-geo-handler.desktop

%files -n %{devname}
%{_includedir}/KF6/KGuiAddons
%{_libdir}/cmake/KF6GuiAddons
%{_qtdir}/doc/KF6GuiAddons.*

%files -n %{libname}
%{_libdir}/libKF6GuiAddons.so*
