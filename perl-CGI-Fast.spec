#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	CGI
%define		pnam	Fast
Summary:	CGI::Fast - CGI Interface for Fast CGI
Name:		perl-CGI-Fast
Version:	2.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/CGI/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7c1d93600b796b9a0eb6fa3558d3d0c1
URL:		http://search.cpan.org/dist/CGI-Fast/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-CGI >= 4
BuildRequires:	perl-FCGI >= 0.67
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Fast is a subclass of the CGI object created by CGI.pm.  It is
specialized to work with the FCGI module, which greatly speeds up CGI
scripts by turning them into persistently running server processes.
Scripts that perform time-consuming initialization processes, such as
loading large modules or opening persistent database connections, will
see large performance improvements.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Fast.pm
%{_mandir}/man3/*
