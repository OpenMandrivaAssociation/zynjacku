%define name    zynjacku
%define version 5.2
%define release %mkrel 2

Name:           %{name} 
Summary:        LV2 plugin host
Version:        %{version} 
Release:        %{release}

Source0:        http://download.gna.org/%name/%name-%version.tar.bz2
Source1:        zynjacku_logo.xpm
URL:            http://home.gna.org/zynjacku/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 

BuildRequires:  libjack-devel
BuildRequires:  gtk2-devel
BuildRequires:  libglade2-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  slv2-devel
BuildRequires:  pygtk2.0-devel

Requires:       jackit
Requires:       pygtk2.0

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

%build
%configure2_5x
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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README AUTHORS

%{_bindir}/%name
%{_bindir}/zynspect
%{_bindir}/lv2rack
/usr/lib/python2.6/site-packages/zynworld/*
%dir %{_datadir}/%name
%{_datadir}/%name/*
%{_datadir}/pixmaps/%{name}_logo.xpm
%{_datadir}/applications/mandriva-%{name}.desktop
%{_datadir}/applications/mandriva-lv2rack.desktop
