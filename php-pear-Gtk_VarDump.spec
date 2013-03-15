%define		_class		Gtk
%define		_subclass	VarDump
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.0.1
Release:	3
Summary:	A simple GUI to example PHP data trees
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Gtk_VarDump/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Patch0:		php-pear-Gtk_VarDump-1.0.1-php_gtk2.patch
Requires:	php-gtk2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear

%description
Just a regedit type interface to examine PHP data trees.

%prep
%setup -q -c
%patch0 -p1
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-2mdv2011.0
+ Revision: 679338
- mass rebuild

* Sat Nov 27 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.1-1mdv2011.0
+ Revision: 602114
- new version

* Mon Dec 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-5mdv2010.1
+ Revision: 478681
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 1.0.0-4mdv2010.0
+ Revision: 441109
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-3mdv2009.0
+ Revision: 236848
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-2mdv2008.0
+ Revision: 94912
- attempt to make it use php-gtk2

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-1mdv2008.0
+ Revision: 15672
- 1.0.0


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-7mdv2007.0
+ Revision: 81602
- Import php-pear-Gtk_VarDump

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-7mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.0-1mdk
- initial Mandriva package (PLD import)

