Name: perl-File-Spec
Version: 0.82
Release: 1
Packager: mailscanner@ecs.soton.ac.uk
Summary: File-Spec Perl module
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=File%3a%3aSpec
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: perl >= 0:5.00503
Buildarch: noarch
Requires: perl
Source0: File-Spec-0.82.tar.gz

%description
File-Spec Perl module
%prep
%setup -q -n File-Spec-%{version} 1

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make PREFIX=$RPM_BUILD_ROOT/usr install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > File-Spec-0.82-filelist
if [ "$(cat File-Spec-0.82-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f File-Spec-0.82-filelist
%defattr(-,root,root)

%changelog
* Sun Sep 29 2002 mailscanner@ecs.soton.ac.uk
- Specfile autogenerated

