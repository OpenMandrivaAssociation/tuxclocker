Name: tuxclocker
Version: 1.4.0
Release: 1
Source0: https://github.com/Lurkki14/tuxclocker/archive/%{version}/%{name}-%{version}.tar.gz
# Correct revisions for internalized 3rd party components
# can be seen at https://github.com/Lurkki14/tuxclocker/tree/%{version}/src/include/deps
Source1: https://github.com/Dobiasd/FunctionalPlus/archive/25363e38172db64a744c4983cc2a5088838cb519.tar.gz
Source2: https://github.com/mpark/patterns/archive/b3270e0dd7b6312f7a4fe8647e2333dbb86e355e.tar.gz
Summary: Graphical overclocking tool
URL: https://github.com/Lurkki14/tuxclocker
License: GPL-3.0
Group: System
BuildRequires: gettext
BuildRequires: meson ninja
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Gui)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5DBus)
BuildRequires: pkgconfig(Qt5X11Extras)
BuildRequires: pkgconfig(Qt5Charts)
BuildRequires: pkgconfig(libdrm)
BuildRequires: pkgconfig(libdrm_amdgpu)
BuildRequires: qt5-linguist-tools
BuildRequires: hwdata
BuildRequires: git-core
BuildRequires: boost-devel
BuildRequires: qmake5

%description
TuxClocker is a hardware controlling and monitoring program. TuxClocker
consists of a DBus daemon and a Qt GUI that uses the daemon.

%prep
%autosetup -p1
cd src/include/deps
tar xf %{S:1}
tar xf %{S:2}
rm -rf FunctionalPlus patterns
mv FunctionalPlus-* FunctionalPlus
mv patterns-* patterns
cd -
%meson

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang tuxclocker

%files -f tuxclocker.lang
%{_bindir}/tuxclocker-qt
%{_bindir}/tuxclockerd
%{_libdir}/libtuxclocker.so
%dir %{_libdir}/tuxclocker
%dir %{_libdir}/tuxclocker/plugins
%{_libdir}/tuxclocker/plugins/libamd.so
%{_libdir}/tuxclocker/plugins/libcpu.so
%{_datadir}/dbus-1/system-services/org.tuxclocker.service
%{_datadir}/dbus-1/system.d/org.tuxclocker.conf
%{_datadir}/applications/tuxclocker.desktop
%{_iconsdir}/hicolor/scalable/apps/tuxclocker-logo.svg
