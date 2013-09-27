%define	_class		Gtk
%define	_subclass	VarDump
%define	modname	%{_class}_%{_subclass}

Summary:	A simple GUI to example PHP data trees
Name:		php-pear-%{modname}
Version:	1.0.1
Release:	3
License:	PHP License
Group:		Development/PHP
Url:		http://pear.php.net/package/Gtk_VarDump/
Source0:	http://download.pear.php.net/package/%{modname}-%{version}.tar.bz2
Patch0:		php-pear-Gtk_VarDump-1.0.1-php_gtk2.patch
BuildArch:	noarch
BuildRequires:	php-pear
Requires:	php-gtk2
Requires(post,preun):	php-pear
Requires:	php-pear

%description
Just a regedit type interface to examine PHP data trees.

%prep
%setup -qc
%apply_patches
mv package.xml %{modname}-%{version}/%{modname}.xml

%install
cd %{modname}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{modname}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{modname}.xml %{buildroot}%{_datadir}/pear/packages

%files
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{modname}
%{_datadir}/pear/packages/%{modname}.xml

