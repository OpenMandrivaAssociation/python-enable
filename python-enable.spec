%define module	enable

Summary:	Enthought Tool Suite - low-level drawing and interaction
Name:		python-%{module}
Version:	4.2.0
Release:	2
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/enable/
Obsoletes:	python-enthought-enable
Requires:	python-numpy >= 1.1.0
Requires: 	python-reportlab, python-opengl
Requires:	python-pyface >= 4.2.0
Requires:	python-traitsui >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	swig >= 1.3.30
BuildRequires:	python-cython >= 0.13
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	freetype-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	mesagl-devel
BuildRequires:	mesaglu-devel
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx
BuildRequires:	pkgconfig(lapack)

%description
The Enable project provides two related multi-platform packages for
drawing GUI objects.

* Enable: An object drawing library that supports containment and
  event notification.
* Kiva: A multi-platform DisplayPDF vector drawing engine.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build
%__python setup.py build_docs

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%files
%doc *.txt *.rst examples/ build/docs/html
%py_platsitedir/%{module}*
%py_platsitedir/kiva*


%changelog
* Mon Aug 13 2012 Lev Givon <lev@mandriva.org> 4.2.0-1
+ Revision: 814713
- Update to 4.2.0.

* Tue Dec 27 2011 Lev Givon <lev@mandriva.org> 4.1.0-1
+ Revision: 745666
- Update to 4.1.0.

* Thu Jul 07 2011 Lev Givon <lev@mandriva.org> 4.0.0-1
+ Revision: 689182
- import python-enable


