%define name    zynjacku
%define version 6
%define release 2

Name:           %{name}
Summary:        LV2 plugin host
Version:        %{version}
Release:        %{release}

Source0:        http://download.gna.org/%name/%name-%version.tar.bz2
Source1:        zynjacku_logo.xpm
# (Fedora)Correct lv2 path on 64bit systems:
# https://gna.org/bugs/?13687
Patch0:         zynjacku-lv2path.patch
URL:            http://home.gna.org/zynjacku/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  jackit-devel
BuildRequires:  gtk2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  slv2-devel
BuildRequires:  lv2-devel
BuildRequires:  pygtk2.0-devel

Requires:       jackit
Requires:       pygtk2.0
Provides:       lv2rack

%description
zynjacku is JACK based, GTK (2.x) host for LV2 synths. It has one JACK
MIDI input port (routed to all hosted synths) and one (two for stereo
synths) JACK audio output port per plugin. Such design provides
multi-timbral sound by running several synth plugins.
zynjacku is a nunchaku weapon for JACK audio synthesis.
You have solid parts for synthesis itself and you have flexible part that
allows synthesis to suit your needs.
lv2rack is a host for LV2 effect plugins.

%prep
%setup -q
%patch0 -p1 -b .lv2path

%build
%configure2_5x --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications


#make desktop file for zynjacku
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=Zynjacku
Comment=LV2 synth plugin host
Exec=%{_bindir}/%{name}
Icon=%{_datadir}/pixmaps/zynjacku_logo.xpm
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
EOF

#make desktop file for lv2rack
cat > %{buildroot}%{_datadir}/applications/mandriva-lv2rack.desktop <<EOF
[Desktop Entry]
Name=LV2Rack
Comment=LV2 effects plugin host
Exec=%{_bindir}/lv2rack
Icon=%{_datadir}/pixmaps/zynjacku_logo.xpm
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;
EOF

# don't ship .la
find %{buildroot} -name '*.la' | xargs rm -f

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README AUTHORS NEWS

%{_bindir}/%name
%{_bindir}/zynspect
%{_bindir}/lv2rack
%{python_sitelib}/zynworld/*
%dir %{_datadir}/%name
%{_datadir}/%name/*
%{_datadir}/pixmaps/%{name}_logo.xpm
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/mandriva-lv2rack.desktop


%changelog
* Wed Apr 25 2012 Frank Kober <emuse@mandriva.org> 6-2
+ Revision: 793425
- rebuild fixing BRs

* Tue Mar 29 2011 Frank Kober <emuse@mandriva.org> 6-1
+ Revision: 648748
- new version 6

* Mon Nov 01 2010 Frank Kober <emuse@mandriva.org> 5.2-5mdv2011.0
+ Revision: 591680
- rebuild for new python

* Tue Aug 10 2010 Ahmad Samir <ahmadsamir@mandriva.org> 5.2-4mdv2011.0
+ Revision: 568288
- add patch to fix loading the plugins on 64bit systems (Fedora)
- disable static build and don't ship .la files

  + Frank Kober <emuse@mandriva.org>
    - remove obsolete dbus BR

* Tue Apr 06 2010 Frank Kober <emuse@mandriva.org> 5.2-2mdv2010.1
+ Revision: 532046
- bump release
- add desktop files and icons

* Tue Apr 06 2010 Frank Kober <emuse@mandriva.org> 5.2-1mdv2010.1
+ Revision: 532015
- fix python path for x86_64
- import zynjacku


