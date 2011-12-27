%define module	enable
%define name	python-%{module}
%define version	4.1.0
%define release %mkrel 1

Summary:	Enthought Tool Suite - enable project
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://www.enthought.com/repo/ets/%{module}-%{version}.tar.gz
License:	BSD
Group:		Development/Python
Url:		http://code.enthought.com/projects/enable/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:	python-enthought-enable
Requires:	python-numpy >= 1.1.0
Requires: 	python-reportlab, python-opengl
Requires:	python-pyface >= 4.1.0
Requires:	python-traitsui >= 4.1.0
BuildRequires:	python-setuptools >= 0.6c8
BuildRequires:	swig >= 1.3.30, python-cython >= 0.13
BuildRequires:	python-numpy-devel >= 1.1.0
BuildRequires:	freetype-devel, libx11-devel, MesaGL-devel, MesaGLU-devel
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
pushd docs
make html
popd

%install
%__rm -rf %{buildroot}

PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc *.txt *.rst examples/ docs/build/html
