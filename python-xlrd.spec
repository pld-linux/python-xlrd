%define		module	xlrd
Summary:	Python interface to extracting data from Excel datasheets
Summary(pl.UTF-8):	Pythonowy interfejs do odczytywania danych z arkuszy Excela
Name:		python-%{module}
Version:	0.7.9
Release:	1
License:	BSD-style
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/x/xlrd/%{module}-%{version}.tar.gz
# Source0-md5:	8e6833676d78ef65515481952eb0fd76
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
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/%{name},%{_examplesdir}/%{name}-%{version}}
cp -p xlrd/examples/namesdemo.xls $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p xlrd/examples/xlrdnameAPIdemo.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p scripts/runxlrd.py  $RPM_BUILD_ROOT%{_bindir}
mv $RPM_BUILD_ROOT%{_bindir}/runxlrd.py $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/runxlrd.py \
	$RPM_BUILD_ROOT%{py_sitescriptdir}/xlrd/{examples,doc}

cat > $RPM_BUILD_ROOT%{_bindir}/runxlrd <<'EOF'
#!/bin/sh
exec %{__python} %{_datadir}/%{name}/runxlrd.pyc "$@"
EOF
chmod a+x $RPM_BUILD_ROOT%{_bindir}/runxlrd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc xlrd/doc/compdoc.html xlrd/doc/xlrd.html
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{_examplesdir}/%{name}-%{version}
%{_datadir}/%{name}/runxlrd.pyc
%attr(755,root,root) %{_bindir}/runxlrd
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-*.egg-info
%endif
