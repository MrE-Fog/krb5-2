#
# TODO:
# - split kdc/kadmind/krb524d/kpropd to separate subpackages
# - finish config files and init scripts
# - SECURITY: http://securitytracker.com/alerts/2004/Aug/1011107.html
# - SECURITY: http://securitytracker.com/alerts/2004/Aug/1011106.html
#
# Conditional build:
%bcond_with	krb4	# build with Kerberos V4 support
%bcond_without	tcl	# build without tcl (needed for tests) 
#
Summary:	Kerberos V5 System
Summary(pl.UTF-8):	System Kerberos V5
Name:		krb5
Version:	1.3.1
Release:	0.2
License:	MIT
Group:		Networking
# warning: according to README, Source0 may require license to export outside USA
Source0:	http://www.crypto-publish.org/dist/mit-kerberos5/%{name}-%{version}.tar.gz
# Source0-md5:	73f868cf65bec56d7c718834ca5665fd
Source1:	%{name}kdc.init
Source2:	%{name}24d.init
Source3:	kadm5.acl
Source4:	kerberos.logrotate
Source5:	%{name}.conf
Source6:	kdc.conf
Source7:	kerberos.sysconfig
Source8:	kerberos.sh
Source9:	kerberos.csh
Source10:	klogind.inetd
Source11:	kftpd.inetd
Source12:	ktelnetd.inetd
Source13:	kshell.inetd
Source14:	propagation
Source15:	kpropd.init
Source16:	kadmind.init
URL:		http://web.mit.edu/kerberos/www/
Patch0:		%{name}-gcc33.patch
Patch1:		%{name}-telnetd.patch
Patch2:		%{name}-manpages.patch
Patch3:		%{name}-netkit-rsh.patch
Patch4:		%{name}-rlogind-environ.patch
Patch5:		%{name}-ksu-access.patch
Patch6:		%{name}-ksu-path.patch
Patch7:		%{name}-tiocgltc.patch
Patch8:		%{name}-term.patch
Patch9:		%{name}-passive.patch
# http://lite.mit.edu/
Patch10:	%{name}-ktany.patch
Patch11:	%{name}-size.patch
Patch12:	%{name}-ftp-glob.patch
Patch13:	%{name}-check.patch
Patch14:	%{name}-double-free.patch
Patch15:	%{name}-varargs.patch
Patch16:	%{name}-norpath.patch
Patch17:	%{name}-paths.patch
Patch18:	%{name}-autoconf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	e2fsprogs-devel >= 1.34
BuildRequires:	flex
BuildRequires:	mawk
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.268
%{?with_tcl:BuildRequires:	tcl-devel}
Requires:	rc-scripts
Requires:	setup >= 2.4.6-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_localstatedir	/var/lib/kerberos

%description
Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description -l pl.UTF-8
Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (użytkownik lub serwis) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package clients
Summary:	Kerberos V5 programs for use on workstations
Summary(pl.UTF-8):	Oprogramowanie klienckie dla stacji roboczej kerberosa
Group:		Networking
Requires:	%{name}-libs = %{version}

%description clients
Kerberos V5 Clients.

Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description clients -l pl.UTF-8
Oprogramowanie klienckie do korzystania z usług systemu Kerberos V5.

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (użytkownik lub serwis) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package server
Summary:	Kerberos V5 Server
Summary(pl.UTF-8):	Serwer Kerberos V5
Group:		Networking
Requires:	%{name}-libs = %{version}
Requires:	words

%description server
Master KDC.

Kerberos V5 is based on the Kerberos authentication system developed
at MIT. Under Kerberos, a client (generally either a user or a
service) sends a request for a ticket to the Key Distribution Center
(KDC). The KDC creates a "ticket-granting ticket" (TGT) for the
client, encrypts it using the client's password as the key, and sends
the encrypted TGT back to the client. The client then attempts to
decrypt the TGT, using its password. If the client successfully
decrypts the TGT (i.e., if the client gave the correct password), it
keeps the decrypted TGT, which indicates proof of the client's
identity.

%description server -l pl.UTF-8
Główne centrum dystrybucji kluczy (KDC).

Kerberos V5 jest systemem autentykacji rozwijanym w MIT. W tym
systemie klient (użytkownik lub serwis) wysyła żądanie biletu do
Centrum Dystrybucji Kluczy (KDC). KDC tworzy zakodowany kredyt (TGT),
używając hasła klienta do jego zaszyfrowania i wysyła go z powrotem do
klienta. Klient następnie przystępuje do rozkodowywania kredytu przy
pomocy swojego hasła. Jeżeli zrobi to prawidłowo (tzn. poda poprawne
hasło), jego bilet uaktywnia się i będzie ważny na daną usługę.

%package ftpd
Summary:	The standard UNIX FTP (file transfer protocol) server
Summary(pl.UTF-8):	Serwer FTP
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	ftpd

%description ftpd
FTP is the file transfer protocol, which is a widely used Internet
protocol for transferring files and for archiving files.

%description ftpd -l pl.UTF-8
FTP jest protokołem transmisji plików szeroko rozpowszechnionym w
Internecie.

%package kshd
Summary:	Kerberized remote shell server
Summary(pl.UTF-8):	Skerberyzowany serwer zdalnego dostępu
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rshd

%description kshd
The kshd package contains kerberized remote shell server which
provides remote execution facilities with authentication based on the
Kerberos authentication system.

%description kshd -l pl.UTF-8
Ten pakiet zawiera skerberyzowaną wersję serwer zdalnego dostępu,
który umożliwia zdalne wykonywanie poleceń w oparciu o system
autentykacji Kerberos.

%package telnetd
Summary:	Server for the telnet remote login
Summary(pl.UTF-8):	Serwer protokołu telnet
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	telnetd

%description telnetd
Telnet is a popular protocol for remote logins across the Internet.
This package provides a telnet daemon which allows remote logins into
the machine it is running on.

%description telnetd -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera serwer pozwalający na zdalne logowanie się klientów na maszynę
na której działa.

%package klogind
Summary:	Remote login server
Summary(pl.UTF-8):	Serwer zdalnego logowania
Group:		Networking/Daemons
Requires:	%{name}-libs = %{version}
Requires:	rc-inetd >= 0.8.1
Obsoletes:	rlogind

%description klogind
Klogind is the server for the rlogin program. The server is based on
rlogind but uses Kerberos authentication.

%description klogind -l pl.UTF-8
Klogind jest serwerem dla programu rlogin. Oparty jest na rlogind ale
wykorzystuje system autentykacji Kerberos.


%package rlogin
Summary:	rlogin is used when signing onto a system
Summary(pl.UTF-8):	Narzędzie do logowania w systemie
Group:		Networking
Requires:	%{name}-libs = %{version}
Provides:	rlogin

%description rlogin
login is used when signing onto a system. It can also be used to
switch from one user to another at any time (most modern shells have
support for this feature built into them, however). This package
contain kerberized version login program.

%description rlogin -l pl.UTF-8
login jest używany przy logowaniu do systemu. Może być także użyty do
przełączenia z jednego użytkownika na innego w dowolnej chwili
(większość współczesnych shelli ma wbudowaną obsługę tego). Ten pakiet
zawiera skerberyzowaną wersję programu rlogin.

%package rsh
Summary:	Clients for remote access commands (rsh, rlogin, rcp)
Summary(pl.UTF-8):	Klient zdalnego dostępu (rsh, rlogin, rcp)
Group:		Applications/Networking
Requires:	%{name}-libs = %{version}
Obsoletes:	rcp
Obsoletes:	rsh

%description rsh
The rsh package contains a set of programs which allow users to run
commands on remote machines, login to other machines and copy files
between machines (rsh, rlogin and rcp). All three of these commands
use rhosts style authentication. This package contains the clients
needed for all of these services.

%description rsh -l pl.UTF-8
Ten pakiet zawiera zestaw narzędzi pozwalających na wykonywanie
poleceń na zdalnych maszynach, logowanie na inne maszyny oraz
kopiowanie plików pomiędzy maszynami (rsh, rlogin, rcp).

%package ftp
Summary:	The standard UNIX FTP (file transfer protocol) client
Summary(pl.UTF-8):	Klient protokołu FTP
Group:		Networking
Requires:	%{name}-libs = %{version}

%description ftp
The ftp package provides the standard UNIX command-line FTP client
with kerberos authentication support. FTP is the file transfer
protocol, which is a widely used Internet protocol for transferring
files and for archiving files.

%description ftp -l pl.UTF-8
Ten pakiet dostarcza standardowego klienta FTP z wbudowaną obsługą
kerberosa. FTP jest protokołem do przesyłania plików szeroko
rozpowszechnionym w Internecie.

%package telnet
Summary:	Client for the telnet remote login
Summary(pl.UTF-8):	Klient usługi telnet
Group:		Networking
Requires:	%{name}-libs = %{version}
Obsoletes:	telnet

%description telnet
Telnet is a popular protocol for remote logins across the Internet.
This package provides a command line telnet client.

%description telnet -l pl.UTF-8
Telnet jest popularnym protokołem zdalnego logowania. Ten pakiet
zawiera klienta tej usługi.

%package libs
Summary:	Kerberos V5 shared libraries
Summary(pl.UTF-8):	Biblioteki dzielone dla Kerberosa V5
Group:		Libraries
Requires(post):	/sbin/ldconfig
Requires(post,preun):	grep
Requires(preun):	coreutils
Obsoletes:	krb5-configs
Obsoletes:	krb5-lib

%description libs
Libraries for Kerberos V5 Server and Client

%description libs -l pl.UTF-8
Biblioteki dynamiczne dla systemu Kerberos V5.

%package devel
Summary:	Header files for Kerberos V5 libraries and documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do bibliotek Kerberosa V5
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}

%description devel
Header files for Kerberos V5 libraries and development documentation.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek Kerberosa V5.

%package static
Summary:	Static Kerberos V5 libraries
Summary(pl.UTF-8):	Biblioteki statyczne Kerberosa V5
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static Kerberos V5 libraries.

%description static -l pl.UTF-8
Biblioteki statyczne Kerberosa V5.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p0
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1

%build
cd src
%{__aclocal}
%{__autoconf}
cp -f /usr/share/automake/config.sub config/
CC="%{__cc}"
CFLAGS="%{rpmcflags} -fPIC -I%{_includedir}/et"
%configure \
	--libexecdir=%{_libdir} \
	--enable-shared \
	--enable-static \
	%{?with_krb4: --with-krb4}%{?!with_krb4: --without-krb4} \
	--with-vague-errors \
	--enable-dns \
	--enable-dns-for-kdc \
	--enable-dns-for-realm \
	--with-netlib=-lresolv \
	%{!?with_tcl: --with-tcl=%{_prefix}} \
	--with-system-et \
	--with-system-ss \
	%{_target_platform}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_localstatedir},/var/log/kerberos,%{_infodir},%{_mandir}}
install -d $RPM_BUILD_ROOT/etc/{rc.d/init.d,sysconfig/rc-inetd,shrc.d,logrotate.d}

%{__make} -C src install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE5} $RPM_BUILD_ROOT%{_sysconfdir}/
install %{SOURCE6} $RPM_BUILD_ROOT%{_localstatedir}/
install %{SOURCE3} $RPM_BUILD_ROOT%{_localstatedir}/
install %{SOURCE4} $RPM_BUILD_ROOT/etc/logrotate.d/kerberos
install %{SOURCE7} $RPM_BUILD_ROOT/etc/sysconfig/kerberos
install %{SOURCE14} $RPM_BUILD_ROOT%{_sbindir}/propagation
install %{SOURCE8} %{SOURCE9} $RPM_BUILD_ROOT/etc/shrc.d

install %{SOURCE10} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/klogind
install %{SOURCE11} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/ftpd
install %{SOURCE12} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/telnetd
install %{SOURCE13} $RPM_BUILD_ROOT/etc/sysconfig/rc-inetd/kshd

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/krb5kdc
install %{SOURCE15} $RPM_BUILD_ROOT/etc/rc.d/init.d/kpropd
install %{SOURCE16} $RPM_BUILD_ROOT/etc/rc.d/init.d/kadmind
%if %{with krb4}
install %{SOURCE2}			$RPM_BUILD_ROOT/etc/rc.d/init.d/krb524d
%endif

ln -sf %{_datadir}/dict/words $RPM_BUILD_ROOT%{_localstatedir}/kadm5.dict
touch $RPM_BUILD_ROOT%{_localstatedir}/krb5.keytab

echo .so kadmin.8 > $RPM_BUILD_ROOT%{_mandir}/man8/kadmin.local.8

rm -rf $RPM_BUILD_ROOT%{_includedir}/asn.1

find doc -size 0 -print | xargs rm -f

# rpath fix
sed "s/^CC_LINK=.*/CC_LINK='\$(CC) \$(PROG_LIBPATH)'/g" src/krb5-config > $RPM_BUILD_ROOT%{_bindir}/krb5-config

%clean
rm -rf $RPM_BUILD_ROOT

%post server
/sbin/chkconfig --add krb5kdc
%service krb5kdc restart "krb5kdc daemon"

/sbin/chkconfig --add kadmind
%service kadmind restart "kadmind daemon"

/sbin/chkconfig --add kpropd
%service kpropd restart "kpropd daemon"

%if %{with krb4}
/sbin/chkconfig --add krb524d
%service krb524d restart "krb524d daemon"
%endif

%postun server
if [ "$1" = 0 ]; then
	%service krb5kdc stop
	/sbin/chkconfig --del krb5kdc

	%service kadmind stop
	/sbin/chkconfig --del kadmind

	%service kpropd stop
	/sbin/chkconfig --del kpropd

	%if %{with krb4}
	%service krb524d stop
	/sbin/chkconfig --del krb524d
	%endif
fi

%post ftpd
%service -q rc-inetd reload

%postun ftpd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post kshd
%service -q rc-inetd reload

%postun kshd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post telnetd
%service -q rc-inetd reload

%postun telnetd
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post klogind
%service -q rc-inetd reload

%postun klogind
if [ "$1" = 0 ]; then
	%service -q rc-inetd reload
fi

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%files server
%defattr(644,root,root,755)
%doc doc/krb5-{admin,install}.html
%doc %{?with_krb4:doc/krb425.html}
%attr(754,root,root) /etc/rc.d/init.d/krb5kdc
%attr(754,root,root) /etc/rc.d/init.d/kadmind
%attr(754,root,root) /etc/rc.d/init.d/kpropd
%{?with_krb4:%attr(754,root,root) /etc/rc.d/init.d/krb524d}

%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/logrotate.d/*
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/kerberos

%attr(750,root,root) %dir /var/log/kerberos
%attr(700,root,root) %dir %{_localstatedir}
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_localstatedir}/*

%attr(755,root,root) %{_sbindir}/kadmin
%attr(755,root,root) %{_sbindir}/kadmin.local
%attr(755,root,root) %{_sbindir}/propagation
%attr(755,root,root) %{_sbindir}/kdb5_util
%attr(755,root,root) %{_sbindir}/kprop
%attr(755,root,root) %{_sbindir}/kpropd
%attr(755,root,root) %{_sbindir}/krb5-send-pr
%attr(755,root,root) %{_sbindir}/krb5kdc
%attr(755,root,root) %{_sbindir}/kadmind
%attr(755,root,root) %{_sbindir}/ktutil
%attr(755,root,root) %{_sbindir}/k5srvutil
%attr(755,root,root) %{_sbindir}/v5passwdd
%attr(755,root,root) %{_sbindir}/gss-server
%attr(755,root,root) %{_sbindir}/sserver
%{?with_krb4:%attr(755,root,root) %{_sbindir}/kadmind4}
%{?with_krb4:%attr(755,root,root) %{_sbindir}/krb524d}

%{_mandir}/man8/kadmin.8*
%{_mandir}/man8/kadmin.local.8*
%{_mandir}/man8/kdb5_util.8*
%{_mandir}/man8/kprop.8*
%{_mandir}/man8/kpropd.8*
%{_mandir}/man8/krb5kdc.8*
%{_mandir}/man8/kadmind.8*
%{_mandir}/man8/ktutil.8*
%{_mandir}/man8/k5srvutil.8*
%{_mandir}/man8/sserver.8*

%files clients
%defattr(644,root,root,755)
%doc doc/krb5-user.html
%attr(755,root,root) /etc/shrc.d/kerberos.*

%attr(755,root,root) %{_bindir}/kdestroy
%attr(755,root,root) %{_bindir}/kinit
%attr(755,root,root) %{_bindir}/v5passwd
%attr(755,root,root) %{_bindir}/klist
%attr(755,root,root) %{_bindir}/gss-client
%attr(4755,root,root) %{_bindir}/ksu
%{?with_krb4:%attr(755,root,root) %{_bindir}/krb524init}

%attr(755,root,root) %{_bindir}/kpasswd
%attr(755,root,root) %{_bindir}/sclient
%attr(755,root,root) %{_bindir}/kvno

%{_mandir}/man1/v5passwd.1*
%{_mandir}/man1/kerberos.1*
%{_mandir}/man1/kdestroy.1*
%{_mandir}/man1/kinit.1*
%{_mandir}/man1/klist.1*
%{_mandir}/man1/ksu.1*
%{_mandir}/man1/kpasswd.1*
%{_mandir}/man1/sclient.1*
%{_mandir}/man1/kvno.1*
%{_mandir}/man5/.k5login.5*

%files rlogin
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rlogin
%{_mandir}/man1/rlogin.1*

%files ftp
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ftp
%{_mandir}/man1/ftp.1*

%files rsh
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/rcp
%attr(755,root,root) %{_bindir}/rsh
%{?with_krb4:%attr(755,root,root) %{_bindir}/v4rcp}
%{_mandir}/man1/rsh.1*
%{_mandir}/man1/rcp.1*
%{?with_krb4:%{_mandir}/man1/v4rcp.1*}

%files telnet
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/telnet
%{_mandir}/man1/telnet.1*

%files telnetd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/telnetd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/telnetd
%{_mandir}/man8/telnetd.8*

%files ftpd
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/ftpd
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/ftpd
%{_mandir}/man8/ftpd.8*

%files kshd
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/kshd
%{_mandir}/man8/kshd.8*

%files klogind
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/klogind
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/rc-inetd/klogind
%{_mandir}/man8/klogind.8*

%files libs
%defattr(644,root,root,755)
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/krb5.conf
%attr(400,root,root) %ghost %{_localstatedir}/krb5.keytab

%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_sbindir}/login.krb5

%{_mandir}/man8/login.krb5.8*
%{_mandir}/man5/krb5.conf.5*
%{_mandir}/man5/kdc.conf.5*

%files devel
%defattr(644,root,root,755)
%doc doc/{kadmin,krb5-protocol}
%attr(755,root,root) %{_bindir}/krb5-config
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/gssapi
%{?with_krb4:%{_includedir}/kerberosIV}
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
