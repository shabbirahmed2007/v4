Summary: perl-Filesys-Statvfs_Statfs_Df Perl module
Name: perl-Filesys-Statvfs_Statfs_Df
Version: 0.78
Release: 2
Packager: mailscanner@ecs.soton.ac.uk
License: GPL or Artistic
Group: Development/Libraries
URL: http://search.cpan.org/dist/Filesys-Statvfs_Statfs_Df/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
#BuildRequires: perl >= 0:5.00503
Source0: Filesys-Statvfs_Statfs_Df-0.78.tar.gz

%description
Filesys-Statvfs_Statfs_Df Perl module

%description
Filesys-Statvfs_Statfs_Df Perl module
%prep
%setup -q -n Filesys-Statvfs_Statfs_Df-%{version} 1

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
make install DESTDIR=$RPM_BUILD_ROOT

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > Filesys-Statvfs_Statfs_Df-%{version}-filelist
if [ "$(cat Filesys-Statvfs_Statfs_Df-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Filesys-Statvfs_Statfs_Df-%{version}-filelist
%defattr(-,root,root)

%changelog
* Sun Apr 16 2006 Julian Field <mailscanner@ecs.soton.ac.uk>
- Specfile autogenerated

