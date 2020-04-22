Name: python-markupsafe
Version: 0.18
Release: 1
Summary: Implements a XML/HTML/XHTML Markup safe string for Python
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: %{name}-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
A library for safe markup escaping.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python_sitearch}/markupsafe/*.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitearch}/*
