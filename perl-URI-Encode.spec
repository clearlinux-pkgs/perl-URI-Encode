#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-URI-Encode
Version  : 1.1.1
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/M/MI/MITHUN/URI-Encode-v1.1.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/MI/MITHUN/URI-Encode-v1.1.1.tar.gz
Summary  : 'Simple percent Encoding/Decoding'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-URI-Encode-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
URI::Encode - Simple percent Encoding/Decoding
<a href="https://travis-ci.org/mithun/perl-uri-encode"><img src="https://travis-ci.org/mithun/perl-uri-encode.svg?branch=master"></a>

%package dev
Summary: dev components for the perl-URI-Encode package.
Group: Development
Provides: perl-URI-Encode-devel = %{version}-%{release}

%description dev
dev components for the perl-URI-Encode package.


%package license
Summary: license components for the perl-URI-Encode package.
Group: Default

%description license
license components for the perl-URI-Encode package.


%prep
%setup -q -n URI-Encode-v1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-URI-Encode
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-URI-Encode/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1URI/Encode.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/URI::Encode.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-URI-Encode/LICENSE
