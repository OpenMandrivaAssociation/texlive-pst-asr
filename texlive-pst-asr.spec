Name:		texlive-pst-asr
Version:	22138
Release:	2
Summary:	Typeset autosegmental representations for linguists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-asr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package allows the user to typeset autosegmental
representations. It uses the PStricks, and xkeyval packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-asr/pst-asr.tex
%{_texmfdistdir}/tex/latex/pst-asr/pst-asr.sty
%doc %{_texmfdistdir}/doc/generic/pst-asr/README
%doc %{_texmfdistdir}/doc/generic/pst-asr/pst-asr-doc-source.zip
%doc %{_texmfdistdir}/doc/generic/pst-asr/pst-asr-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-asr/pst-asr-examples.pdf
%doc %{_texmfdistdir}/doc/generic/pst-asr/pst-asr-examples.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
