#
# Conditional build:
%bcond_without tests		# do not perform "make test"
#
%include        /usr/lib/rpm/macros.perl
Summary:	Converts Outlook .mbx and .dbx files into standard UUCP mailbox files
Summary(pl.UTF-8):	Konwersja plików .mbx i .dbx z Outlooka na standardowe skrzynki UUCP
Name:		mbx2mbox
Version:	0.34
Release:	2
License:	GPL
Group:		Applications/Text
Source0:	http://dl.sourceforge.net/mbx2mbox/%{name}-%{version}.tar.gz
# Source0-md5:	a72210d985ef56ef1ad3b37bb428bf7b
URL:		http://mbx2mbox.sourceforge.net/
BuildRequires:	perl-devel >= 1:5.6.0
BuildRequires:	perl-Date-Manip
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
mbx2mbox attempts to convert Microsoft's proprietary .mbx and .dbx
formats to the standard Unix-style UUCP mail format used by programs
like UCB Mail, Pine, and Netscape Messenger. The .mbx and .dbx files
provided as arguments to mbx2mbox are processed and output to files
having the same name, except without the .mbx extension.

%description -l pl.UTF-8
mbx2mbox próbuje konwertować pliki .mbx i .dbx we własnościowych
formatach Microsoftu do standardowego, uniksowego formatu skrzynek
UUCP, używanego przez programy takie jak UCB Mail, Pine czy Netscape
Messenger. Pliki .mbx i .dbx przekazane jako argumenty mbx2mbox są
przetwarzane z zapisywane do plików o tej samej nazwie, ale bez
rozszerzenia .mbx.

%prep
%setup -q

%build
%{__perl} Makefile.PL
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mbx2mbox
%{_mandir}/man1/mbx2mbox*
