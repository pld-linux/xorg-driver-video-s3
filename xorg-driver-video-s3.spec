Summary:	X.org video driver for old S3 video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla starych kart graficznych S3
Name:		xorg-driver-video-s3
Version:	0.6.5
Release:	10
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3-%{version}.tar.bz2
# Source0-md5:	37248d5c5a04d7f91c6f634cc592b304
Patch0:		mibstore.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.4
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.4
Provides:	xorg-driver-video
Obsoletes:	X11-driver-s3 < 1:7.0.0
Obsoletes:	XFree86-S3
Obsoletes:	XFree86-driver-s3 < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for old S3 video adapters. It supports:
- Trio32 (86C732)
- Trio64 (86C764)
- Trio64V+ (86C765),
- Aurora64V+ (86CM65),
- Trio64UV+ (86C767),
- Trio64V2/DX (86C775),
- Trio64V2/GX (86C785),
- Vision964 (86C964),
- Vision968 (86C968).

%description -l pl.UTF-8
Sterownik obrazu X.org dla starych kart graficznych S3. Obsługuje
układy:
- Trio32 (86C732)
- Trio64 (86C764)
- Trio64V+ (86C765),
- Aurora64V+ (86CM65),
- Trio64UV+ (86C767),
- Trio64V2/DX (86C775),
- Trio64V2/GX (86C785),
- Vision964 (86C964),
- Vision968 (86C968).

%prep
%setup -q -n xf86-video-s3-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/s3_drv.so
%{_mandir}/man4/s3.4*
