%define upstream_name    Cache-Memcached
%define upstream_version 1.26

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Client library for memcached (memory cache daemon) 
License:	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/~bradfitz/Cache-Memcached/
Source0:    http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl(Storable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(String::CRC32)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
This is the Perl API for memcached, a distributed memory cache daemon. See the
documentation within the module for details on its use.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%makeinstall_std

%clean 
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Cache/Memcached.pm
%dir %{perl_vendorlib}/Cache/Memcached
%{perl_vendorlib}/Cache/Memcached/GetParser.pm
%{_mandir}/*/*
