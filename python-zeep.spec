#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-zeep
Version  : 2.5.0
Release  : 10
URL      : https://github.com/mvantellingen/python-zeep/archive/2.5.0.tar.gz
Source0  : https://github.com/mvantellingen/python-zeep/archive/2.5.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: python-zeep-python3
Requires: python-zeep-python
Requires: appdirs
Requires: cached-property
Requires: defusedxml
Requires: isodate
Requires: lxml
Requires: pytz
Requires: requests
Requires: six
Requires: toolbelt
BuildRequires : appdirs
BuildRequires : cached-property
BuildRequires : defusedxml
BuildRequires : isodate
BuildRequires : lxml
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest

BuildRequires : python3-dev
BuildRequires : pytz
BuildRequires : requests
BuildRequires : setuptools
BuildRequires : six
BuildRequires : toolbelt-python
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
Requires: python-zeep-python3

%description python
python components for the python-zeep package.


%package python3
Summary: python3 components for the python-zeep package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-zeep package.


%prep
%setup -q -n python-zeep-2.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523300289
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
