%define         module  xlrd
Summary:	Python interface to extracting data from Excel datasheets
Summary(pl.UTF-8):	Pythonowy interfejs do odczytywania danych z arkuszy Excela
Name:		python-%{module}
Version:	0.6.1
Release:	0.2
License:	BSD-style
Group:		Development/Languages/Python
Source0:	http://www.lexicon.net/sjmachin/%{module}-%{version}.zip
URL:		http://www.lexicon.net/sjmachin/xlrd.htm
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python interface to extracting data from Excel datasheets

%description -l pl.UTF-8
Pythonowy interfejs do odczytywania danych z arkuszy Excela

%prep
%setup -q -n %{module}-%{version}

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install xlrd/examples/namesdemo.xls $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install xlrd/examples/xlrdnameAPIdemo.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install scripts/runxlrd.py  $RPM_BUILD_ROOT%{_bindir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_ocomp $RPM_BUILD_ROOT%{_bindir}
%py_comp $RPM_BUILD_ROOT%{_bindir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xlrd/doc/compdoc.html xlrd/doc/HISTORY.html xlrd/doc/README.html xlrd/doc/xlrd.html
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_bindir}/runxlrd.py[oc]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
