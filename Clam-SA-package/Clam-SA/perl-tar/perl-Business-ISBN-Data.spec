Summary: Business-ISBN-Data Perl module
Name: perl-Business-ISBN-Data
Version: 1.10
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Business-ISBN-Data/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Business-ISBN-Data-1.10.tar.gz

%description
Business-ISBN-Data Perl module

%description
Business-ISBN-Data Perl module
%prep
%setup -q -n Business-ISBN-Data-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
make test

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
	grep -v "\.packlist" > Business-ISBN-Data-%{version}-filelist
if [ "$(cat Business-ISBN-Data-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Business-ISBN-Data-%{version}-filelist
%defattr(-,root,root)

%changelog
* Fri Mar 14 2008 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

