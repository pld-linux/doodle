# Conditional build:
%bcond_without  static_libs     # don't build static library

Summary:	A tool to search the meta-data in your files via a database
Summary(pl):	Narzędzie do szybkiego przeszukiwania dokumentów w specjalnej bazie danych
Name:		doodle
Version:	0.6.3
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://gnunet.org/doodle/download/%{name}-%{version}.tar.gz
# Source0-md5:	cd9cd75157d177aa9421588d97474ae3
URL:		http://gnunet.org/doodle/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	libtool
BuildRequires:	libextractor-devel
Requires:	doodle-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doodle is a tool to quickly search the documents on a computer. Doodle
builds an index using meta-data contained in the documents and allows
fast searches on the resulting database.

%description -l pl
Doodle to narzędzie do szybkiego wyszukiwania dokumentów w komputerze.
W tym celu buduje indeks, korzystając z metadanych zawartych w
dokumentach i umożliwia szybkie przeszukiwanie tak powstałej bazy 
danych.

%package devel
Summary:	doodle - header files
Summary(pl):	doodle - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for doodle.

%description devel -l pl
Ten pakiet zawiera pliki nagłówkowe doodle'a.

%package libs
Summary:	Doodle library
Summary(pl):	Biblioteka doodle'a
Group:		Development/Libraries
Requires:	libextractor

%description libs
A doodle library.

%description libs -l pl
Biblioteka doodle'a.

%package static
Summary:	Doodle - static library
Summary(pl):	Biblioteka statyczna doodle'a
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static doodle library.

%description static -l pl
Biblioteka statyczna doodle'a.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize} --ltdl
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
        %{?with_static_libs:--enable-static}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post libs  -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so*

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.a

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/doodle*
%{_mandir}/man1/doodle*
