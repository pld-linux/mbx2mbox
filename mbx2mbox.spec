#
# Conditional build:
# _without_tests	- do not perform "make test"
#
%include        /usr/lib/rpm/macros.perl
Summary:	Converts Outlook .mbx and .dbx files into standard UUCP mailbox files
Summary(pl):	Konwersja plik�w .mbx i .dbx z Outlooka na standardowe skrzynki UUCP
Name:		mbx2mbox
Version:	0.34
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/mbx2mbox/%{name}-%{version}.tar.gz
URL:		http://mbx2mbox.sourceforge.net/
BuildRequires:	perl >= 5.6.0
BuildRequires:	perl-Date-Manip
BuildRequires:	rpm-perlprov
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mbx2mbox attempts to convert Microsoft's proprietary .mbx and .dbx
formats to the standard Unix-style UUCP mail format used by programs
like UCB Mail, Pine, and Netscape Messenger. The .mbx and .dbx files
provided as arguments to mbx2mbox are processed and output to files
having the same name, except without the .mbx extension.

%description -l pl
mbx2mbox pr�buje konwertowa� pliki .mbx i .dbx we w�asno�ciowych
formatach Microsoftu do standardowego, uniksowego formatu skrzynek
UUCP, u�ywanego przez programy takie jak UCB Mail, Pine czy Netscape
Messenger. Pliki .mbx i .dbx przekazane jako argumenty mbx2mbox s�
przetwarzane z zapisywane do plik�w o tej samej nazwie, ale bez
rozszerzenia .mbx.

%prep
%setup -q

%build
%{__perl} Makefile.PL
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mbx2mbox
%{_mandir}/man1/mbx2mbox*