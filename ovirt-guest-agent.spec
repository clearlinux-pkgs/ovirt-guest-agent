#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ovirt-guest-agent
Version  : 1.0.14
Release  : 5
URL      : https://github.com/oVirt/ovirt-guest-agent/archive/1.0.14.tar.gz
Source0  : https://github.com/oVirt/ovirt-guest-agent/archive/1.0.14.tar.gz
Summary  : The oVirt Guest Agent
Group    : Development/Tools
License  : Apache-2.0
Requires: ovirt-guest-agent-config
Requires: ovirt-guest-agent-lib
Requires: ovirt-guest-agent-data
BuildRequires : Linux-PAM-dev
BuildRequires : cmake
BuildRequires : gdm-dev
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-2.0)
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : systemd-dev

%description
This is the oVirt management agent running inside the guest. The agent
interfaces with the oVirt manager, supplying heart-beat info as well as
run-time data from within the guest itself. The agent also accepts
control commands to be run executed within the OS (like: shutdown and
restart).

%package config
Summary: config components for the ovirt-guest-agent package.
Group: Default

%description config
config components for the ovirt-guest-agent package.


%package data
Summary: data components for the ovirt-guest-agent package.
Group: Data

%description data
data components for the ovirt-guest-agent package.


%package lib
Summary: lib components for the ovirt-guest-agent package.
Group: Libraries
Requires: ovirt-guest-agent-data

%description lib
lib components for the ovirt-guest-agent package.


%prep
%setup -q -n ovirt-guest-agent-1.0.14

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519407421
%autogen --disable-static --without-gdm \
--without-kdm \
--sysconfdir=/usr/share/defaults/ovirt-guest-agent \
--with-pam-prefix=/usr/share/pam.d
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1519407421
rm -rf %{buildroot}
%make_install
## make_install_append content
mkdir -p %{buildroot}/usr/share/dbus-1/system.d/
mv %{buildroot}/usr/share/defaults/ovirt-guest-agent/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf \
%{buildroot}/usr/share/dbus-1/system.d/org.ovirt.vdsm.Credentials.conf
## make_install_append end

%files
%defattr(-,root,root,-)

%files config
%defattr(-,root,root,-)
/usr/lib/systemd/system/ovirt-guest-agent.service

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
/usr/share/ovirt-guest-agent/__pycache__/LockActiveSession.cpython-36.pyc
/usr/share/ovirt-guest-agent/__pycache__/LogoutActiveUser.cpython-36.pyc
/usr/share/ovirt-guest-agent/__pycache__/OVirtAgentLogic.cpython-36.pyc
/usr/share/ovirt-guest-agent/__pycache__/VirtIoChannel.cpython-36.pyc
/usr/share/ovirt-guest-agent/__pycache__/hooks.cpython-36.pyc
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
