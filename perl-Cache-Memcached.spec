%define upstream_name    Cache-Memcached
%define upstream_version 1.30
Name:		perl-%{upstream_name}
Version:	1.30
Release:	1

Summary:	Client library for memcached (memory cache daemon) 
License:	GPL
Group: 		Development/Perl
Url:		https://metacpan.org/dist/Cache-Memcached
Source0:	https://cpan.metacpan.org/authors/id/D/DO/DORMANDO/Cache-Memcached-1.30.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Storable)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(String::CRC32)
BuildArch:	noarch

%description
This is the Perl API for memcached, a distributed memory cache daemon. See the
documentation within the module for details on its use.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# seems to fail on ABF
#make test

%install
%makeinstall_std

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO
%{perl_vendorlib}/Cache/Memcached.pm
%dir %{perl_vendorlib}/Cache/Memcached
%{perl_vendorlib}/Cache/Memcached/GetParser.pm
%{_mandir}/*/*


