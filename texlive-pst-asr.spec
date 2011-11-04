# revision 22138
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-asr
# catalog-date 2011-04-20 18:25:54 +0200
# catalog-license lppl
# catalog-version 1.3
Name:		texlive-pst-asr
Version:	1.3
Release:	1
Summary:	Typeset autosegmental representations for linguists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-asr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-asr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the user to typeset autosegmental
representations. It uses the PStricks, and xkeyval packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
