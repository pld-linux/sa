#
# Conditional build:
%bcond_without	tests	# don't perform "make check"
#
Summary:	OSSP sa - Socket Abstraction
#Summary(pl):	OSSP sa - biblioteka 
Name:		sa
Version:	1.2.2
Release:	0.1
Epoch:		0
License:	distributable (see README)
Group:		Libraries
Source0:	ftp://ftp.ossp.org/pkg/lib/sa/%{name}-%{version}.tar.gz
# Source0-md5:	757d5298581d9b9a3d71147fba542509
Patch0:		%{name}-libs.patch
URL:		http://www.ossp.org/pkg/lib/sa/
BuildRequires:	ex-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SSP sa is an abstraction library for the Unix socket application
programming interface (API) featuring stream and datagram oriented
communication over Unix Domain and Internet Domain (TCP and UDP)
sockets. It provides the following key features: address abstraction
(local, IPv4, and IPv6), type abstraction, I/O timeouts, I/O stream
buffering and convenience I/O functions.

#%description -l pl
# TODO

%package devel
Summary:	OSSP sa - Socket Abstraction - header files and development libraries
Summary(pl):	OSSP sa - biblioteka Socket Abstraction - pliki nag³ówkowe i biblioteki dla deweloperów
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description devel
OSSP sa - Socket Abstraction - header files and development libraries

%description devel -l pl
OSSP sa - biblioteka Socket Abstraction - pliki nag³ówkowe i biblioteki dla deweloperów

%package static
Summary:	OSSP sa - Socket Abstraction - static libraries
Summary(pl):	OSSP sa - biblioteka Socket Abstraction - biblioteki statyczne
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
OSSP sa - Socket Abstraction - static libraries.

%description static -l pl
OSSP sa - biblioteka Socket Abstraction - biblioteki statyczne.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--with-ex
%{__make}

%{?with_tests:%{__make} check}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README THANKS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a
