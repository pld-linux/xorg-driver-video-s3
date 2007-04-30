Summary:	X.org video driver for old S3 video adapters
Summary(pl.UTF-8):	Sterownik obrazu X.org dla starych kart graficznych S3
Name:		xorg-driver-video-s3
Version:	0.5.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-s3-%{version}.tar.bz2
# Source0-md5:	d95ab6445cab477f39adfbbc81006f67
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
Obsoletes:	X11-driver-s3 < 1:7.0.0
Obsoletes:	XFree86-S3
Obsoletes:	XFree86-driver-s3 < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for old S3 video adapters. It supports 964, 968,
Trio32/64, Aurora64V+, Trio64UV+, Trio64V2/DX/GX chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org dla starych kart graficznych S3. Obsługuje
układy 964, 968, Trio32/64, Aurora64V+, Trio64UV+, Trio64V2/DX/GX.

%prep
%setup -q -n xf86-video-s3-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/s3_drv.so
#%{_mandir}/man4/s3.4*
