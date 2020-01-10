#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ovirt-guest-agent
Version  : 1.0.16
Release  : 11
URL      : https://github.com/oVirt/ovirt-guest-agent/archive/1.0.16/ovirt-guest-agent-1.0.16.tar.gz
Source0  : https://github.com/oVirt/ovirt-guest-agent/archive/1.0.16/ovirt-guest-agent-1.0.16.tar.gz
Summary  : The oVirt Guest Agent
Group    : Development/Tools
License  : Apache-2.0
Requires: ovirt-guest-agent-data = %{version}-%{release}
Requires: ovirt-guest-agent-lib = %{version}-%{release}
Requires: ovirt-guest-agent-license = %{version}-%{release}
Requires: ovirt-guest-agent-services = %{version}-%{release}
BuildRequires : Linux-PAM-dev
BuildRequires : buildreq-cmake
BuildRequires : gdm-dev
BuildRequires : nose
BuildRequires : pep8
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : python3-dev
BuildRequires : systemd-dev

%description
This is the oVirt management agent running inside the guest. The agent
interfaces with the oVirt manager, supplying heart-beat info as well as
run-time data from within the guest itself. The agent also accepts
control commands to be run executed within the OS (like: shutdown and
restart).

%package data
Summary: data components for the ovirt-guest-agent package.
Group: Data

%description data
data components for the ovirt-guest-agent package.


%package lib
Summary: lib components for the ovirt-guest-agent package.
Group: Libraries
Requires: ovirt-guest-agent-data = %{version}-%{release}
Requires: ovirt-guest-agent-license = %{version}-%{release}

%description lib
lib components for the ovirt-guest-agent package.


%package license
Summary: license components for the ovirt-guest-agent package.
Group: Default

%description license
license components for the ovirt-guest-agent package.


%package services
Summary: services components for the ovirt-guest-agent package.
Group: Systemd services

%description services
services components for the ovirt-guest-agent package.


%prep
%setup -q -n ovirt-guest-agent-1.0.16
cd %{_builddir}/ovirt-guest-agent-1.0.16

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1578637621
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static --without-gdm \
--without-kdm \
--sysconfdir=/usr/share/defaults/ovirt-guest-agent \
--with-pam-prefix=/usr/share/pam.d
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1578637621
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ovirt-guest-agent
cp %{_builddir}/ovirt-guest-agent-1.0.16/COPYING %{buildroot}/usr/share/package-licenses/ovirt-guest-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890
%make_install
## install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
mv %{buildroot}/usr/share/defaults/ovirt-guest-agent/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf \
%{buildroot}/usr/share/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf
## install_append end

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf
/usr/share/defaults/ovirt-guest-agent/ovirt-guest-agent.conf
/usr/share/defaults/ovirt-guest-agent/ovirt-guest-agent/hooks.d/before_hibernation/55_flush-caches
/usr/share/defaults/ovirt-guest-agent/ovirt-guest-agent/hooks.d/before_migration/55_flush-caches
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-container-list
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-flush-caches
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-hibernate
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-locksession
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-logout
/usr/share/defaults/ovirt-guest-agent/security/console.apps/ovirt-shutdown
/usr/share/defaults/ovirt-guest-agent/udev/rules.d/55-ovirt-guest-agent.rules
/usr/share/ovirt-guest-agent/CredServer.py
/usr/share/ovirt-guest-agent/GuestAgentLinux2.py
/usr/share/ovirt-guest-agent/LockActiveSession.py
/usr/share/ovirt-guest-agent/LogoutActiveUser.py
/usr/share/ovirt-guest-agent/OVirtAgentLogic.py
/usr/share/ovirt-guest-agent/VirtIoChannel.py
/usr/share/ovirt-guest-agent/container-list
/usr/share/ovirt-guest-agent/default-logger.conf
/usr/share/ovirt-guest-agent/default.conf
/usr/share/ovirt-guest-agent/diskmapper
/usr/share/ovirt-guest-agent/hibernate
/usr/share/ovirt-guest-agent/hooks.py
/usr/share/ovirt-guest-agent/ovirt-container-list
/usr/share/ovirt-guest-agent/ovirt-flush-caches
/usr/share/ovirt-guest-agent/ovirt-guest-agent.py
/usr/share/ovirt-guest-agent/ovirt-hibernate
/usr/share/ovirt-guest-agent/ovirt-locksession
/usr/share/ovirt-guest-agent/ovirt-logout
/usr/share/ovirt-guest-agent/ovirt-osinfo
/usr/share/ovirt-guest-agent/ovirt-shutdown
/usr/share/ovirt-guest-agent/scripts/hooks/before_hibernation/55_flush-caches
/usr/share/ovirt-guest-agent/scripts/hooks/before_migration/55_flush-caches
/usr/share/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches
/usr/share/ovirt-guest-agent/scripts/hooks/defaults/55-flush-caches.consolehelper
/usr/share/ovirt-guest-agent/scripts/hooks/defaults/flush-caches
/usr/share/ovirt-guest-agent/timezone.py
/usr/share/pam.d/pam.d/ovirt-container-list
/usr/share/pam.d/pam.d/ovirt-flush-caches
/usr/share/pam.d/pam.d/ovirt-hibernate
/usr/share/pam.d/pam.d/ovirt-locksession
/usr/share/pam.d/pam.d/ovirt-logout
/usr/share/pam.d/pam.d/ovirt-shutdown

%files lib
%defattr(-,root,root,-)
/usr/lib64/security/pam_ovirt_cred.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ovirt-guest-agent/2b8b815229aa8a61e483fb4ba0588b8b6c491890

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/ovirt-guest-agent.service
