Summary: MySQL-MasterHA-Node Perl module
Name: MySQL-MasterHA-Node
Version: 0.51
Release: 0.%{?dist}
License: GPL v2
Vendor: DeNA Co.,Ltd.
Group: Utilities
URL: http://code.google.com/p/mysql-master-ha/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.42
Requires: perl(DBD::mysql)
Requires: perl(DBI)
Source0: MySQL-MasterHA-Node-%{version}.tar.gz

%description
%{summary}.

%prep
%setup -q -n MySQL-MasterHA-Node-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS="vendor" %{?perl_install_vendor_lib}
make %{?_smp_mflags} OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -a \( -name perllocal.pod -o -name .packlist \
  -o \( -name '*.bs' -a -empty \) \) -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

for brp in %{_prefix}/lib/rpm/%{_build_vendor}/brp-compress \
  %{_prefix}/lib/rpm/brp-compress
do
  [ -x $brp ] && $brp && break
done

find $RPM_BUILD_ROOT -type f \
| sed "s@^$RPM_BUILD_ROOT@@g" \
> %{name}-%{version}-%{release}-filelist

if [ "$(cat %{name}-%{version}-%{release}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root,-)

