Summary:	Reports file access events from all running processes
Name:		fatrace
Version:	0.15
Release:	1
License:	GPL v3
Group:		Development/Debuggers
URL:		https://launchpad.net/fatrace
Source0:	https://launchpad.net/fatrace/trunk/%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	d33ec7c650ab25a835540e802bfab09f
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
fatrace reports file access events from all running processes.

Its main purpose is to find processes which keep waking up the disk
unnecessarily and thus prevent some power saving.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING NEWS
%attr(755,root,root) %{_sbindir}/fatrace
%attr(755,root,root) %{_sbindir}/power-usage-report
%{_mandir}/man1/fatrace.1*
