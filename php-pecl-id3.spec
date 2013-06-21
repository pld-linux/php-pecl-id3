%define		php_name	php%{?php_suffix}
%define		modname	id3
%define		status		alpha
Summary:	%{modname} - functions to read and write ID3 tags in MP3 files
Summary(pl.UTF-8):	%{modname} - funkcje do odczytu i zapisu tagów ID3 w plikach MP3
Name:		%{php_name}-pecl-%{modname}
Version:	0.2
Release:	7
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	c19445a5b676a7d5b90d5d19affa9ced
URL:		http://pecl.php.net/package/id3/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Obsoletes:	php-pear-%{modname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
id3 enables to to retrieve and update information from ID3 tags in MP3
files. It supports version 1.0 and version 1.1.

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
id3 umożliwia odbiór i aktualizację informacji w tagach ID3 w plikach
MP3. Wspiera wersję 1.0 oraz 1.1.

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}
install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS EXPERIMENTAL TODO
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
