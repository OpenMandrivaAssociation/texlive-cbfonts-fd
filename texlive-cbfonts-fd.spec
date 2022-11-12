Name:		texlive-cbfonts-fd
Version:	54080
Release:	1
Summary:	LaTeX font description files for the CB Greek fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/cbfonts-fd
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides font description files for all the many
shapes available from the cbfonts collection. The files provide
the means whereby the NFSS knows which fonts a LaTeX user is
requesting.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrcmr.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrcmro.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrcmss.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrcmtt.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlcmss.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlcmtt.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlmr.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlmro.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlmss.fd
%{_texmfdistdir}/tex/latex/cbfonts-fd/lgrlmtt.fd
%doc %{_texmfdistdir}/doc/fonts/cbfonts-fd/README
%doc %{_texmfdistdir}/doc/fonts/cbfonts-fd/cbfonts-fd.pdf
%doc %{_texmfdistdir}/doc/fonts/cbfonts-fd/manifest.txt
#- source
%doc %{_texmfdistdir}/source/fonts/cbfonts-fd/cbfonts-fd.fdd

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
