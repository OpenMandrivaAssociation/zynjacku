%define name    zynjacku
%define version 6
%define release 3
%define _disable_ld_no_undefined 1

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


BuildRequires:  jackit-devel
BuildRequires:  gtk+2.0-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  slv2-devel
BuildRequires:  lv2-devel
BuildRequires:  pygtk2.0-devel
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools

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
#find . -name "*.py" |xargs 2to3 -w
sed -i '\|/usr/bin/env|d' zynworld/host.py

%build
export am_cv_python_pythondir=%{python_sitearch}
%configure2_5x --disable-static
%make

%install
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
chmod -x $RPM_BUILD_ROOT%{python_sitearch}/zynworld/*.py


%files
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


