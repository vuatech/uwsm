Name:		uwsm
Version:	0.21.1
Release:	1
Summary:	Universal Wayland Session Manager
Group:		Hyprland
License:	MIT
URL:		https://github.com/vladimir-csp/%{name}
Source0:	%{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(desktop-file-utils)
BuildRequires:	pkgconfig(scdoc)
BuildRequires:  pkgconfig(python-dbus)

Buildsystem: meson
Buildoption: -Duuctl=enabled -Dfumon=enabled -Duwsm-app=enabled

%description
%{summary}

%undefine _debugsource_packages

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%post
%systemd_user_post fumon.service

%preun
%systemd_user_preun fumon.service

%postun
%systemd_user_postun fumon.service

%files
%doc %{_docdir}/%{name}/
%license LICENSE
%{_bindir}/%{name}
%{_bindir}/%{name}-app
%{_bindir}/%{name}-terminal
%{_bindir}/%{name}-terminal-scope
%{_bindir}/%{name}-terminal-service
%{_bindir}/fumon
%{_bindir}/uuctl
%{_datadir}/%{name}/
%{_datadir}/applications/uuctl.desktop
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/fumon.1.*
%{_mandir}/man3/%{name}-plugins.3.*
%{_userunitdir}/fumon.service


