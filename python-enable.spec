%define module	enable
%define name	python-%{module}
%define version	4.2.0
%define	rel		1
%if %mdkversion < 201100
%define release %mkrel %{rel}
%else
%define	release %{rel}
%endif

Summary:	Enthought Tool Suite - low-level drawing and interaction
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		https://github.com/enthought/enable/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-enable
Requires:	python-numpy >= 1.1.0
Requires: 	python-reportlab, python-opengl
Requires:	python-pyface >= 4.2.0
Requires:	python-traitsui >= 4.2.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	swig >= 1.3.30, python-cython >= 0.13
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	freetype-devel, libx11-devel, 
BuildRequires:	mesagl-devel, mesaglu-devel
BuildRequires:	python-setupdocs >= 1.0.5
BuildRequires:	python-sphinx

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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt *.rst examples/ build/docs/html
%py_platsitedir/%{module}*
%py_platsitedir/kiva*
