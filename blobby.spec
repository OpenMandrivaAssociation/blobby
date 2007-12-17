# DATE=$(date +%Y%m%d)
# svn export https://svn.sourceforge.net/svnroot/blobby/trunk blobby-$DATE
# tar cvjf blobby-$DATE.tar.bz2 blobby-$DATE

%define name blobby
%define version 0.6.a
%define svndate 20061105
%define release %mkrel 1.%{svndate}
%define distname %{name}-%{svndate}

Summary: Blobby Volley arcade game
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
Source1: http://blobby.redio.de/wiki/images/logo.png
License: GPL
Group: Games/Arcade
Url: http://blobby.redio.de/
BuildRequires: automake1.8
BuildRequires: SDL-devel
BuildRequires: GL-devel
BuildRequires: physfs-devel
BuildRequires: zip

%description
Blobby Volley is an arcade game with a simple gameplay and funny
characters design.

%prep
%setup -q -n %{distname}
chmod +x bootstrap

%build
./bootstrap
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
rm -rf %{buildroot}
%makeinstall bindir=%{buildroot}%{_gamesbindir} datadir=%{buildroot}%{_gamesdatadir}

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
%{_gamesbindir}/%{name}-server
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*.xml
%{_gamesdatadir}/%{name}/*.zip
%{_datadir}/icons/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


