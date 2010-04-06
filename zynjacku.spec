%define name    zynjacku
%define version 5.2
%define release %mkrel 1

Name:           %{name} 
Summary:        LV2 plugin host
Version:        %{version} 
Release:        %{release}

Source:         http://download.gna.org/%name/%name-%version.tar.bz2
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

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README AUTHORS

%{_bindir}/%name
%{_bindir}/zynspect
%{_bindir}/lv2rack
%dir %{_libdir}/python2.6/site-packages/zynworld
%{_libdir}/python2.6/site-packages/zynworld/*
%dir %{_datadir}/%name
%{_datadir}/%name/*
