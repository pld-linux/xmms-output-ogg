Summary:	Ogg Vorbis output plugin for XMMS
Summary(pl):	Wtyczka dla XMMS kompresuj±ca wyj¶cie do plików Ogg Vorbis
Name:		xmms-output-ogg
Version:	0.2
Release:	2
License:	GPL
Group:		Development/Libraries
Source0:	http://dl.sourceforge.net/my-xmms-plugs/oggre-%{version}.tar.gz
# Source0-md5:	247eff58c8310a1f21bb84c46d3e5848
Patch0:		%{name}-enc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libogg-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Requires:	xmms
Provides:	xmms-output-plugin
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the oggre output plugin for xmms. It enables you to output all
media played using xmms into the Ogg-Vorbis files.

%description -l pl
To jest wtyczka wyj¶ciowa oggre dla xmms. Umo¿liwia przekierowanie
wyj¶cia ca³ego d¼wiêku odgrywanego przez xmms do plików Ogg-Vorbis.

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

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	libdir=%{xmms_output_plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS
%attr(755,root,root) %{xmms_output_plugindir}/*
