%define		_modname	id3
%define		_status		alpha

Summary:	%{_modname} - functions to read and write ID3 tags in MP3 files
Summary(pl):	%{_modname} - funkcje do odczytu i zapisu tagów ID3 w plikach MP3
Name:		php-pecl-%{_modname}
Version:	0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	c19445a5b676a7d5b90d5d19affa9ced
URL:		http://pecl.php.net/package/id3/
BuildRequires:	php-devel >= 3:5.0.0
Requires:	php-common >= 3:5.0.0
Obsoletes:	php-pear-%{_modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php
%define		extensionsdir	%{_libdir}/php

%description
id3 enables to to retrieve and update information from ID3 tags in MP3
files. It supports version 1.0 and version 1.1.

In PECL status of this extension is: %{_status}.

%description -l pl
id3 umo¿liwia odbiór i aktualizacjê informacji w tagach ID3 w plikach
MP3. Wspiera wersjê 1.0 oraz 1.1.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/php-module-install install %{_modname} %{_sysconfdir}/php-cgi.ini

%preun
if [ "$1" = "0" ]; then
	%{_sbindir}/php-module-install remove %{_modname} %{_sysconfdir}/php-cgi.ini
fi

%files
%defattr(644,root,root,755)
%doc %{_modname}-%{version}/{CREDITS,EXPERIMENTAL,TODO}
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
