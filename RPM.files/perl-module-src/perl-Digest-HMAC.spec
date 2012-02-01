Summary: Digest-HMAC Perl module
Name: perl-Digest-HMAC
Version: 1.01
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Digest-HMAC/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Digest-HMAC-1.01.tar.gz

%description
Digest-HMAC Perl module

%description
Digest-HMAC Perl module
%prep
%setup -q -n Digest-HMAC-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL INSTALLDIRS="vendor"
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make pure_install DESTDIR=$RPM_BUILD_ROOT

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.gz" | \
	grep -v "\.packlist" > Digest-HMAC-%{version}-filelist
if [ "$(cat Digest-HMAC-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Digest-HMAC-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

