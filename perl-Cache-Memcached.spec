Summary:	Client library for memcached (memory cache daemon) 
Name: 		perl-Cache-Memcached
Version: 	1.20
Release:	%mkrel 1
License:	GPL
Group: 		Development/Perl
URL:		http://search.cpan.org/~bradfitz/Cache-Memcached/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/Cache-Memcached-%{version}.tar.bz2
BuildRequires:  perl(Storable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(String::CRC32)
BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-buildroot

%description
This is the Perl API for memcached, a distributed memory cache daemon. See the
documentation within the module for details on its use.

%prep

%setup -q -n Cache-Memcached-%{version}

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
%{_mandir}/*/*


