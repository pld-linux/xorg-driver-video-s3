Summary:	X.org video driver for old S3 video adapters
Summary(pl):	Sterownik obrazu X.org dla starych kart graficznych S3
Name:		xorg-driver-video-s3
Version:	0.3.5.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-s3-%{version}.tar.bz2
# Source0-md5:	33f85caafaac11abfd64131c63df8742
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for old S3 video adapters. It supports 964, 968,
Trio32/64, Aurora64V+, Trio64UV+, Trio64V2/DX/GX chipsets.

%description -l pl
Sterownik obrazu X.org dla starych kart graficznych S3. Obs�uguje
uk�ady 964, 968, Trio32/64, Aurora64V+, Trio64UV+, Trio64V2/DX/GX.

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
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/s3_drv.so
#%{_mandir}/man4/s3.4x*
