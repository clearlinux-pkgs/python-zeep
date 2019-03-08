#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zeep
Version  : 3.3.0
Release  : 20
URL      : https://github.com/mvantellingen/python-zeep/archive/3.3.0.tar.gz
Source0  : https://github.com/mvantellingen/python-zeep/archive/3.3.0.tar.gz
Summary  : A fast and modern Python SOAP client
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-zeep-license = %{version}-%{release}
Requires: python-zeep-python = %{version}-%{release}
Requires: python-zeep-python3 = %{version}-%{release}
Requires: appdirs
Requires: attrs
Requires: cached-property
Requires: defusedxml
Requires: isodate
Requires: lxml
Requires: pytz
Requires: requests
Requires: requests-toolbelt
Requires: six
BuildRequires : appdirs
BuildRequires : attrs
BuildRequires : buildreq-distutils3
BuildRequires : cached-property
BuildRequires : defusedxml
BuildRequires : isodate
BuildRequires : lxml
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : pytz
BuildRequires : requests
BuildRequires : requests-toolbelt-python
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
========================
Zeep: Python SOAP client
========================
A fast and modern Python SOAP client

%package license
Summary: license components for the python-zeep package.
Group: Default

%description license
license components for the python-zeep package.


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

%description python3
python3 components for the python-zeep package.


%prep
%setup -q -n python-zeep-3.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1552072066
export LDFLAGS="${LDFLAGS} -fno-lto"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-zeep
cp LICENSE %{buildroot}/usr/share/package-licenses/python-zeep/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-zeep/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
