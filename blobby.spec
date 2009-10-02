# DATE=$(date +%Y%m%d)
# svn export https://svn.sourceforge.net/svnroot/blobby/trunk blobby-$DATE
# tar cvjf blobby-$DATE.tar.bz2 blobby-$DATE

%define name blobby
%define version 0.7.0
%define svndate 20091002
%define rel 1
%define release %mkrel 0.%{svndate}.%{rel}
%define distname %{name}-%{svndate}

Summary: Blobby Volley arcade game
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Arcade
Url: http://sourceforge.net/projects/blobby/
Source0: %{distname}.tar.bz2
Source1: http://blobby.redio.de/wiki/images/logo.png
BuildRequires: automake1.8
BuildRequires: SDL-devel
BuildRequires: GL-devel
BuildRequires: physfs-devel
BuildRequires: zip
BuildRequires: cmake
BuildRoot: %{_tmppath}/%{name}-%{version}

%description
Blobby Volley is an arcade game with a simple gameplay and funny
characters design.

%prep
%setup -q -n %{distname}

%build
cmake .
%make

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_gamesbindir} %{buildroot}%{_gamesdatadir}/%{name}/data
for p in %{name} %{name}-server; do
    install -m 755 src/$p %{buildroot}%{_gamesbindir}/$p.real
    cat > %{buildroot}%{_gamesbindir}/$p <<EOF
#!/bin/sh
cd %{_gamesdatadir}/%{name}
exec $p.real \$@
EOF
    chmod +x %{buildroot}%{_gamesbindir}/$p
done

cp -a data/*.xml data/*.zip data/backgrounds data/gfx data/gf2x data/sounds %{buildroot}%{_gamesdatadir}/%{name}/data
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/icons/%{name}.png

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Blobby Volley
Comment=Blobby Volley arcade game
Exec=soundwrapper %_gamesbindir/%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_gamesbindir}/%{name}
%{_gamesbindir}/%{name}.real
%{_gamesbindir}/%{name}-server
%{_gamesbindir}/%{name}-server.real
%dir %{_gamesdatadir}/%{name}
%dir %{_gamesdatadir}/%{name}/data
%{_gamesdatadir}/%{name}/data/*.xml
%{_gamesdatadir}/%{name}/data/*.zip
%dir %{_gamesdatadir}/%{name}/data/backgrounds
%{_gamesdatadir}/%{name}/data/backgrounds/*.bmp
%dir %{_gamesdatadir}/%{name}/data/gfx
%{_gamesdatadir}/%{name}/data/gfx/*.bmp
%dir %{_gamesdatadir}/%{name}/data/gf2x
%{_gamesdatadir}/%{name}/data/gf2x/*.bmp
%dir %{_gamesdatadir}/%{name}/data/sounds
%{_gamesdatadir}/%{name}/data/sounds/*.wav
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop
