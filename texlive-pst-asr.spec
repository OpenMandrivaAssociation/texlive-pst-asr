%global tl_name pst-asr
%global tl_revision 22138

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3
Release:	%{tl_revision}.1
Summary:	Typeset autosegmental representations for linguists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-asr
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package allows the user to typeset autosegmental representations. It
uses the PStricks, and xkeyval packages.

