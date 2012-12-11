%define upstream_name    Role-HasMessage
%define upstream_version 0.005

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	A thing with a String::Errf-powered message
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Role/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(String::Errf)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(namespace::clean)
BuildArch:	noarch

%description
This is another extremely simple role. A class that includes
Role::HasMessage is promising to provide a 'message' method that returns a
string summarizing the message or event represented by the object. It does
_not_ provide any actual behavior.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.5.0-2mdv2011.0
+ Revision: 657465
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-1
+ Revision: 639037
- import perl-Role-HasMessage

