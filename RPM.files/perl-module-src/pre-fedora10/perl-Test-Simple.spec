Summary: Test-Simple Perl module
Name: perl-Test-Simple
Version: 0.70
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Test-Simple/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Test-Simple-0.70.tar.gz

%description
Test-Simple Perl module

%description
Test-Simple Perl module
%prep
%setup -q -n Test-Simple-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
#make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > Test-Simple-%{version}-filelist
if [ "$(cat Test-Simple-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Test-Simple-%{version}-filelist
%defattr(-,root,root)

%changelog
* Wed Jul 11 2007 Julian Field <mailscanner@ecs.soton.ac.uk>
- Commented out the "make test" stage
* Sun Oct 06 2002 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated
