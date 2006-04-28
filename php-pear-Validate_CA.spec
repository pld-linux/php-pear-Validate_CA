%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_subclass	CA
%define		_status		alpha
%define		_pearname	Validate_CA

Summary:	%{_pearname} - Validation class for Canada
Summary(pl):	%{_pearname} - Klasa sprawdzaj±ca poprawno¶æ dla Kanady
Name:		php-pear-%{_pearname}
Version:	0.1.2
Release:	1
Epoch:		0
License:	New BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8e3b42b51b749f19a21d3c512ea45742
URL:		http://pear.php.net/package/Validate_CA/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pcre
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package contains locale validation for Canada such as:
- Social Insurance Numbers (SIN)
- Postal Codes
- Regions (Provinces)
- Phone Numbers

In PEAR status of this package is: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno¶ci dla Kanady danych takich jak:
- numer ubezpieczenia spo³ecznego (SIN)
- kod pocztowy
- region (prowincja)
- numer telefonu

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Validate/CA.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Validate_CA
