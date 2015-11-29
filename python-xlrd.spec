%define		module	xlrd
Summary:	Python interface to extracting data from Excel datasheets
Summary(pl.UTF-8):	Pythonowy interfejs do odczytywania danych z arkuszy Excela
Name:		python-%{module}
Version:	0.9.3
Release:	2
License:	BSD-style
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/x/xlrd/%{module}-%{version}.tar.gz
# Source0-md5:	6f3325132f246594988171bc72e1a385
URL:		http://www.lexicon.net/sjmachin/xlrd.htm
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to extracting data from Excel datasheets

%description -l pl.UTF-8
Pythonowy interfejs do odczytywania danych z arkuszy Excela

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__mv} $RPM_BUILD_ROOT%{_bindir}/runxlrd{.py,}
%{__sed} -i -e 's|/usr/bin/env python|%{__python}|' $RPM_BUILD_ROOT%{_bindir}/runxlrd

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%attr(755,root,root) %{_bindir}/runxlrd
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
