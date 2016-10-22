%{?scl:%scl_package perl-JSON-PP}

Name:		%{?scl_prefix}perl-JSON-PP
Version:	2.27400
Release:	4%{?dist}
Summary:	JSON::XS compatible pure-Perl module
License:	GPL+ or Artistic
Group:		Development/Libraries
URL:		http://search.cpan.org/dist/JSON-PP/
Source0:	http://search.cpan.org/CPAN/authors/id/M/MA/MAKAMAKA/JSON-PP-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(id -nu)
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	%{?scl_prefix}perl
BuildRequires:	%{?scl_prefix}perl-generators
BuildRequires:	%{?scl_prefix}perl(ExtUtils::MakeMaker)
BuildRequires:	%{?scl_prefix}perl(lib)
# Module Runtime
BuildRequires:	%{?scl_prefix}perl(B)
BuildRequires:	%{?scl_prefix}perl(base)
BuildRequires:	%{?scl_prefix}perl(bytes)
BuildRequires:	%{?scl_prefix}perl(Carp)
BuildRequires:	%{?scl_prefix}perl(constant)
BuildRequires:	%{?scl_prefix}perl(Encode)
BuildRequires:	%{?scl_prefix}perl(Exporter)
BuildRequires:	%{?scl_prefix}perl(Math::BigFloat)
BuildRequires:	%{?scl_prefix}perl(Math::BigInt)
BuildRequires:	%{?scl_prefix}perl(overload)
BuildRequires:	%{?scl_prefix}perl(Scalar::Util)
BuildRequires:	%{?scl_prefix}perl(strict)
BuildRequires:	%{?scl_prefix}perl(subs)
BuildRequires:	%{?scl_prefix}perl(utf8)
# Script Runtime
BuildRequires:	%{?scl_prefix}perl(Data::Dumper)
BuildRequires:	%{?scl_prefix}perl(Getopt::Long)
# Test Suite
BuildRequires:	%{?scl_prefix}perl(Test::More)
BuildRequires:	%{?scl_prefix}perl(Tie::Array)
BuildRequires:	%{?scl_prefix}perl(Tie::Hash)
# Optional tests
%if !%{defined perl_bootstrap}
# Disable non-core dependencies when bootstraping a core module
BuildRequires:	%{?scl_prefix}perl(Tie::IxHash)
%endif
# Runtime
Requires:	%{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:	%{?scl_prefix}perl(Data::Dumper)
Requires:	%{?scl_prefix}perl(Encode)
Requires:	%{?scl_prefix}perl(Math::BigFloat)
Requires:	%{?scl_prefix}perl(Math::BigInt)
Requires:	%{?scl_prefix}perl(Scalar::Util)
Requires:	%{?scl_prefix}perl(subs)
Requires:	%{?scl_prefix}perl(utf8)
Conflicts:	%{?scl_prefix}perl-JSON < 2.50

%description
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.

JSON::PP is a pure-Perl module and is compatible with JSON::XS.

%prep
%setup -q -n JSON-PP-%{version}

%build
%{?scl:scl enable %{scl} '}perl Makefile.PL INSTALLDIRS=vendor && make %{?_smp_mflags}%{?scl:'}

%install
rm -rf %{buildroot}
%{?scl:scl enable %{scl} '}make pure_install DESTDIR=%{buildroot}%{?scl:'}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}

%check
%{?scl:scl enable %{scl} '}make test%{?scl:'}

%clean
rm -rf %{buildroot}

%files
%doc Changes README
%{_bindir}/json_pp
%{perl_vendorlib}/JSON/
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.3*
%{_mandir}/man3/JSON::PP::Boolean.3*

%changelog
* Mon Jul 11 2016 Petr Pisar <ppisar@redhat.com> - 2.27400-4
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.27400-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2.27400-2
- Perl 5.24 rebuild

* Mon Apr 25 2016 Paul Howarth <paul@city-fan.org> - 2.27400-1
- Update to 2.27400
  - Applied and merged long term neglected patches and pull requests
  - Modified Makefile.PL to set UNINST=1 if needed on old perls
  - Decode decimals to Perl's internal NV type
- Simplify find command using -delete

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.27300-348
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27300-347
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.27300-346
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.27300-345
- Increase release to favour standalone package

* Wed Jun 03 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2.27300-3
- Perl 5.22 rebuild

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 2.27300-2
- Disable non-core dependencies when bootstraping a core module

* Wed Oct  8 2014 Paul Howarth <paul@city-fan.org> - 2.27300-1
- Update to 2.27300
  - Fixed a problem about substr in perl 5.8.6 and below
- Classify buildreqs by usage

* Wed Sep 03 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.27203-310
- Increase release to favour standalone package

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2.27203-3
- Perl 5.20 rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27203-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Paul Howarth <paul@city-fan.org> - 2.27203-1
- Update to 2.27203
  - Fixed return/or in _incr_parse (CPAN RT#86948)
- Specify all dependencies

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27202-291
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 15 2013 Petr Pisar <ppisar@redhat.com> - 2.27202-290
- Increase release to favour standalone package

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2.27202-2
- Perl 5.18 rebuild

* Wed Mar 13 2013 Paul Howarth <paul@city-fan.org> - 2.27202-1
- Update to 2.27202
  - Fix test failures due to hash iterator randomization in perl 5.17.6 onwards
    (CPAN RT#83421)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27200-243
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Petr Šabata <contyk@redhat.com> - 2.27200-242
- Correct the URL
- Add a few missing buildtime dependencies
- Drop Getopt::Long dep; json_pp isn't tested

* Tue Aug 28 2012 Paul Howarth <paul@city-fan.org> - 2.27200-241
- BR: perl(base), perl(constant) and perl(lib)
- Install to vendor directories
- Drop %%defattr, redundant since rpm 4.4
- Don't need to remove empty directories from the buildroot

* Fri Aug 17 2012 Petr Pisar <ppisar@redhat.com> - 2.27200-240
- Increase release to replace perl sub-package (bug #848961)

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27200-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2.27200-5
- Perl 5.16 rebuild

* Fri Jun 01 2012 Petr Pisar <ppisar@redhat.com> - 2.27200-4
- Depend of Data::Dumper

* Thu Jan 12 2012 Paul Howarth <paul@city-fan.org> - 2.27200-3
- Add buildreqs for perl core modules, which might be dual-lived

* Sun Jun 19 2011 Marcela Mašláňová <mmaslano@redhat.com> - 2.27200-2
- Perl mass rebuild

* Sun May 22 2011 Paul Howarth <paul@city-fan.org> - 2.27200-1
- Update to 2.27200
  - Fixed incr_parse decoding string more correctly (CPAN RT#68032)

* Tue Mar  8 2011 Paul Howarth <paul@city-fan.org> - 2.27105-1
- Update to 2.27105
  - Removed t/900_pod.t from package because of author test
- Drop buildreq perl(Test::Pod), no longer needed

* Tue Feb  8 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.27104-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jan 27 2011 Paul Howarth <paul@city-fan.org> - 2.27104-3
- Conflict with perl-JSON < 2.50 (#672764)

* Wed Jan 26 2011 Paul Howarth <paul@city-fan.org> - 2.27104-2
- Sanitize for Fedora submission

* Tue Jan 25 2011 Paul Howarth <paul@city-fan.org> - 2.27104-1
- Initial RPM version
