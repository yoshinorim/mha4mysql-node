Summary: Master High Availability Manager and Tools for MySQL, Node Package
Name: mha4mysql-node
Version: 0.58
Release: 0%{?dist}
License: GPL v2
Vendor: DeNA Co.,Ltd.
Group: Utilities
URL: http://code.google.com/p/mysql-master-ha/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch: noarch
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
Requires: perl(DBD::mysql)
Requires: perl(DBI)
Source0: mha4mysql-node-%{version}.tar.gz

%description
%{summary}.

%prep
%setup -q -n mha4mysql-node-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS="vendor" INSTALLVENDORLIB=%{?perl_install_vendor_lib}
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

%changelog
* Thu Mar 22 2018 Kenny.Gryp <kenny@goss.be>
- Several bugfixes
- IPV6 support
- super_read_only support
- enforce_storage_engine support
- Version 0.58
- With the help of Marcelo Altmann <marcelo.altmann@percona.com>



* Sun May 31 2015 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- (Note: All changelogs are written here: http://code.google.com/p/mysql-master-ha/wiki/ReleaseNotes )
- Version 0.57

* Tue Apr 1 2014 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.56

* Sat Dec 1 2012 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.54

* Mon Jan 9 2012 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.53

* Fri Sep 16 2011 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.52 (0.51 was skipped)

* Sat Jul 23 2011 Yoshinori Matsunobu <Yoshinori.Matsunobu@gmail.com>
- Version 0.50
