#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module	xlrd
Summary:	Python interface to extracting data from Excel datasheets
Summary(pl.UTF-8):	Pythonowy interfejs do odczytywania danych z arkuszy Excela
Name:		python-%{module}
Version:	2.0.1
Release:	4
License:	BSD-style
Group:		Development/Languages/Python
Source0:	https://files.pythonhosted.org/packages/source/x/xlrd/%{module}-%{version}.tar.gz
# Source0-md5:	ae3f951c857a490d432f0a7d722352bf
URL:		https://www.python-excel.org/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to extracting data from Excel datasheets

%description -l pl.UTF-8
Pythonowy interfejs do odczytywania danych z arkuszy Excela

%package -n python3-%{module}
Summary:	Python interface to extracting data from Excel datasheets
Summary(pl.UTF-8):	Pythonowy interfejs do odczytywania danych z arkuszy Excela
Requires:	python3-modules >= 1:3.6

%description -n python3-%{module}
Python interface to extracting data from Excel datasheets

%description -n python3-%{module} -l pl.UTF-8
Pythonowy interfejs do odczytywania danych z arkuszy Excela

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%{__sed} -i -e 's|/usr/bin/env python|%{__python}|' $RPM_BUILD_ROOT%{_bindir}/runxlrd.py
%endif

%if %{with python3}
%py3_install
%{__sed} -i -e 's|/usr/bin/env python|%{__python3}|' $RPM_BUILD_ROOT%{_bindir}/runxlrd.py
%endif

%{__mv} $RPM_BUILD_ROOT%{_bindir}/runxlrd{.py,}


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%if %{without python3}
%attr(755,root,root) %{_bindir}/runxlrd
%endif
%{py_sitescriptdir}/%{module}-*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%attr(755,root,root) %{_bindir}/runxlrd
%{py3_sitescriptdir}/%{module}-*.egg-info
%endif
