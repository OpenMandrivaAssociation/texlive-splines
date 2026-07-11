%global tl_name splines
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	MetaPost macros for drawing cubic spline interpolants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/splines
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/splines.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a small package of macros for creating cubic spline interpolants
in MetaPost or Metafont. Given a list of points the macros can produce a
closed or a relaxed spline joining them. Given a list of function values
y_j at x_j, the result would define the graph of a cubic spline
interpolating function y=f(x), which is either periodic or relaxed.

