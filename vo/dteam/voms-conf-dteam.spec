Name:           voms-conf-dteam
Version:        20110325
Release:        1%{?dist}
Summary:        VOMS Configuration Files for the dteam VO

Group:          Applications/System
License:        ASL 2.0
URL:            https://wiki.egi.eu/wiki/Dteam_vo
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
Configuration files to enabled the dteam VO.

%prep
%setup -q

%build
#Nothing to build.

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/vomses
%config(noreplace) %{_sysconfdir}/vomses/*
%dir %{_sysconfdir}/grid-security
%dir %{_sysconfdir}/grid-security/vomsdir
%config(noreplace) %{_sysconfdir}/grid-security/vomsdir/*.lsc
%doc README ChangeLog LICENSE



%changelog
* Sun Dec 12 2010 Steve Traylen <steve@traylen.net> - 20120325-1
- Remove CERN VOMS servers.

* Sun Dec 12 2010 Steve Traylen <steve@traylen.net> - 20101212-1
- First version.
