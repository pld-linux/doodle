# TODO:
# - move doodled to separate package (maybe some initscript?)
#
# Conditional build:
%bcond_without  static_libs     # don't build static library
#
Summary:	A tool to search the meta-data in your files via a database
Summary(pl.UTF-8):   Narzędzie do szybkiego przeszukiwania dokumentów w specjalnej bazie danych
Name:		doodle
Version:	0.6.5
Release:	1
License:	GPL
Group:		Applications
Source0:	http://gnunet.org/doodle/download/%{name}-%{version}.tar.gz
# Source0-md5:	2ff179e8ec2af74937681ece8cc43b68
URL:		http://gnunet.org/doodle/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	bzip2-devel
BuildRequires:	fam-devel
BuildRequires:	gettext-devel >= 0.14.5
BuildRequires:	libextractor-devel
BuildRequires:	libtool
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Doodle is a tool to quickly search the documents on a computer. Doodle
builds an index using meta-data contained in the documents and allows
fast searches on the resulting database.

%description -l pl.UTF-8
Doodle to narzędzie do szybkiego wyszukiwania dokumentów w komputerze.
W tym celu buduje indeks, korzystając z metadanych zawartych w
dokumentach, po czym umożliwia szybkie przeszukiwanie tak powstałej
bazy danych.

%package devel
Summary:	doodle - header files
Summary(pl.UTF-8):   doodle - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This is the package containing the header files for doodle.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki nagłówkowe doodle'a.

%package libs
Summary:	Doodle library
Summary(pl.UTF-8):   Biblioteka doodle'a
Group:		Libraries

%description libs
A doodle library.

%description libs -l pl.UTF-8
Biblioteka doodle'a.

%package static
Summary:	Doodle - static library
Summary(pl.UTF-8):   Biblioteka statyczna doodle'a
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static doodle library.

%description static -l pl.UTF-8
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

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/doodle*
%{_mandir}/man1/doodle*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
