#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zeep
Version  : 4.1.0
Release  : 40
URL      : https://github.com/mvantellingen/python-zeep/archive/4.1.0/python-zeep-4.1.0.tar.gz
Source0  : https://github.com/mvantellingen/python-zeep/archive/4.1.0/python-zeep-4.1.0.tar.gz
Summary  : A modern/fast Python SOAP client based on lxml / requests
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-zeep-python = %{version}-%{release}
Requires: python-zeep-python3 = %{version}-%{release}
Requires: attrs
Requires: cached-property
Requires: isodate
Requires: lxml
Requires: platformdirs
Requires: pytz
Requires: requests
Requires: requests-file
Requires: requests-toolbelt
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : isodate
BuildRequires : lxml
BuildRequires : platformdirs
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytz
BuildRequires : requests
BuildRequires : requests-file
BuildRequires : requests-toolbelt
BuildRequires : requests-toolbelt-python
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Zeep: Python SOAP client
========================
A fast and modern Python SOAP client

%package python
Summary: python components for the python-zeep package.
Group: Default
Requires: python-zeep-python3 = %{version}-%{release}

%description python
python components for the python-zeep package.


%package python3
Summary: python3 components for the python-zeep package.
Group: Default
Requires: python3-core
Provides: pypi(python_zeep)
Requires: pypi(appdirs)
Requires: pypi(attrs)
Requires: pypi(cached_property)
Requires: pypi(defusedxml)
Requires: pypi(isodate)
Requires: pypi(lxml)
Requires: pypi(pytz)
Requires: pypi(requests)
Requires: pypi(requests_toolbelt)
Requires: pypi(six)

%description python3
python3 components for the python-zeep package.


%prep
%setup -q -n python-zeep-4.1.0
cd %{_builddir}/python-zeep-4.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1629134104
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
