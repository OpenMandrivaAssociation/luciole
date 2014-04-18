Summary:	A stop motion software for animation movie realization
Name:		luciole
Version:	0.9.3
Release:	1
License:	GPLv3
Group:		Video
Source0:	http://launchpad.net/luciole/0.9/0.9.3/+download/%{name}-%{version}.tar.gz
Source100:	luciole.rpmlintrc
Patch0:		luciole-0.8.2-use-system-default-theme.patch
Url:		http://festival.inattendu.org/Luciole
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
Requires:	pygtk2.0
Requires:	python-imaging
Requires:	python-dbus
Requires:	python-goocanvas
Requires:	gstreamer0.10-python
Requires:	pygtk2.0-libglade
Requires:	imagemagick
Requires:	mencoder
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	gstreamer0.10-plugins-base
Requires:	gstreamer0.10-plugins-good
Suggests:	gtk-theme-clearlooks
Suggests:	murrine

%description
Luciole is a stop motion software for animation movie realization. It can make
live capture of images from external devices as webcam or DV cam.

%prep
%setup -q 
%patch0 -p0 -b .default-theme

%install
python setup.py install --root %{buildroot}

%files
%doc COPYING RELEASE
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*
%py_puresitedir/pitivi
%py_puresitedir/luciole
%py_puresitedir/*egg-info
%_mandir/man1/*

