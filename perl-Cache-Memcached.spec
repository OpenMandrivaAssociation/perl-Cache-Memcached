%define upstream_name    Cache-Memcached
%define upstream_version 1.29

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Client library for memcached (memory cache daemon) 
License:	GPL
Group: 		Development/Perl
Url:		http://search.cpan.org/~bradfitz/Cache-Memcached/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BR/BRADFITZ/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Storable)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(String::CRC32)
BuildArch:	noarch

%description
This is the Perl API for memcached, a distributed memory cache daemon. See the
documentation within the module for details on its use.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.290.0-2mdv2011.0
+ Revision: 680711
- mass rebuild

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.290.0-1mdv2011.0
+ Revision: 551970
- update to 1.29

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.280.0-1mdv2010.1
+ Revision: 460722
- update to 1.28

* Wed Sep 23 2009 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.0
+ Revision: 447604
- update to 1.27

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.260.0-1mdv2010.0
+ Revision: 402986
- rebuild using %%perl_convert_version

* Wed May 06 2009 Jérôme Quelin <jquelin@mandriva.org> 1.26-1mdv2010.0
+ Revision: 372676
- update to new version 1.26

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.25-1mdv2010.0
+ Revision: 371595
- update to new version 1.25

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.24-3mdv2009.0
+ Revision: 255475
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.24-1mdv2008.1
+ Revision: 136666
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.24-1mdv2008.0
+ Revision: 53363
- update to new version 1.24

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.23-1mdv2008.0
+ Revision: 46336
- update to new version 1.23

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.20-1mdv2008.0
+ Revision: 19255
-New version


* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.18-1mdv2007.0
+ Revision: 110787
- Import perl-Cache-Memcached

* Fri Jan 19 2007 Oden Eriksson <oeriksson@mandriva.com> 1.18-1mdv2007.1
- initial mandriva package

