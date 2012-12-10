Summary:	A stop motion software for animation movie realization
Name:		luciole
Version:	0.8.2
Release:	%mkrel 2
License:	GPLv3
Group:		Video
Source0:	http://launchpad.net/luciole/0.8/0.8.2/+download/%{name}_%{version}.tar.gz
Patch0:		luciole-0.8.2-use-system-default-theme.patch
Url:		http://festival.inattendu.org/Luciole
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	python-devel
BuildRequires:	desktop-file-utils
Requires:	pygtk2.0
Requires:	python-imaging
Requires:	gnome-python
Requires:	python-dbus
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
%setup -q -n %{name}_%{version}
%patch0 -p0 -b .default-theme

%install
rm -rf %{buildroot}

#remove unneeded files
rm -f po/luciole*.po*
rm -f po/POTFILES.in po/createpot.py

mkdir -p %{buildroot}%{_datadir}/%{name}
cp -rp images luciole.py templates ui luciole_lint.rc lucioLib po sounds themes _version.py %{buildroot}%{_datadir}/%{name}

#create executable
cat > luciole  <<EOF
#!/bin/sh
 cd /usr/share/luciole
 exec python luciole.py
EOF
mkdir -p %{buildroot}%{_bindir}
install -m 755 luciole %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install	--remove-key=Encoding \
			--dir %{buildroot}%{_datadir}/applications \
			luciole.desktop

mkdir -p %{buildroot}%{_datadir}/pixmaps
cp -p images/luciole.xpm %{buildroot}%{_datadir}/pixmaps/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root)
%doc COPYING RELEASE
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/*


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-2mdv2011.0
+ Revision: 612782
- the mass rebuild of 2010.1 packages

* Thu Feb 11 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.8.2-1mdv2010.1
+ Revision: 504027
- import luciole


