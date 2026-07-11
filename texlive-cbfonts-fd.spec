%global tl_name cbfonts-fd
%global tl_revision 54080

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	LaTeX font description files for the CB Greek fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/cbfonts-fd
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cbfonts-fd.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides font description files for all the many shapes
available from the cbfonts collection. The files provide the means
whereby the NFSS knows which fonts a LaTeX user is requesting. The
package depends on cbgreek-complete.

