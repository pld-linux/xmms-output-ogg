Summary:	Ogg Vorbis output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS kompresuj±ca wyj¶cie do plików Ogg Vorbis
Name:		xmms-output-ogg
Version:	0.2
Release:	1
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/my-xmms-plugs/oggre-%{version}.tar.gz
Patch0:		%{name}-enc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libogg-devel
BuildRequires:	libvorbis-devel
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is the oggre output plugin for xmms. It enables you to output all
media played using xmms into the Ogg-Vorbis.

%prep
%setup -q -n oggre
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{_libdir}/xmms/Output/*
