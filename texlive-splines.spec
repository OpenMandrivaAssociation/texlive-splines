Name:		texlive-splines
Version:	15878
Release:	2
Summary:	MetaPost macros for drawing cubic spline interpolants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/splines
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a small package of macros for creating cubic spline
interpolants in MetaPost or MetaFont. Given a list of points
the macros can produce a closed or a relaxed spline joining
them. Given a list of function values y_j at x_j, the result
would define the graph of a cubic spline interpolating function
y=f(x), which is either periodic or relaxed.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/splines/splines.mp
%{_texmfdistdir}/metapost/splines/testsplines.mp
%doc %{_texmfdistdir}/doc/metapost/splines/README
%doc %{_texmfdistdir}/doc/metapost/splines/splines.pdf
#- source
%doc %{_texmfdistdir}/source/metapost/splines/splines.dtx
%doc %{_texmfdistdir}/source/metapost/splines/splines.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc source %{buildroot}%{_texmfdistdir}
