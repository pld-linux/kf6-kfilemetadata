#
# Conditional build:
%bcond_with	tests		# build with tests

# TODO:
# - runtime Requires if any

%define         kdeappsver      21.12.3
%define		kdeframever	6.16
%define		qtver		6.7.2
%define		kfname		kfilemetadata
Summary:	File metadata and extraction library
Summary(pl.UTF-8):	Biblioteka do obsługi i wydobywania metadanych plików
Name:		kf6-%{kfname}
Version:	6.16.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	a0d92726a7d5f6b050852eea9e569f78
#Patch0: xattr.patch
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
%if %{with tests}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
%endif
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	attr-devel
BuildRequires:	catdoc
BuildRequires:	cmake >= 3.16
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel
BuildRequires:	ffmpeg-devel
#BuildRequires:	ka5-krita
BuildRequires:	ka6-kdegraphics-mobipocket-devel >= %{kdeappsver}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-karchive-devel >= %{version}
BuildRequires:	kf6-kcodecs-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	poppler-cpp-devel >= 24.08.0
BuildRequires:	poppler-glib-devel >= 24.08.0
BuildRequires:	poppler-qt6-devel >= 24.08.0
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	taglib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
File metadata and extraction library.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	--debug-output

%ninja_build -C build

%{?with_tests:%ninja_build -C build test}


%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

# not supported by glibc yet
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/ie

%find_lang %{kfname}6

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kfname}6.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfilemetadata_dump6
%{_datadir}/qlogging-categories6/kfilemetadata.categories
%attr(755,root,root) %{_libdir}/libKF6FileMetaData.so.*.*.*
%ghost %{_libdir}/libKF6FileMetaData.so.3
%dir %{_libdir}/qt6/plugins/kf6/kfilemetadata
%dir %{_libdir}/qt6/plugins/kf6/kfilemetadata/writers
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/writers/kfilemetadata_taglibwriter.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_epubextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_exiv2extractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_fb2extractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_ffmpegextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_odfextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_office2007extractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_officeextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_plaintextextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_poextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_popplerextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_postscriptdscextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_taglibextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_xmlextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_mobiextractor.so
%attr(755,root,root) %{_datadir}/qlogging-categories6/kfilemetadata.renamecategories
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_pngextractor.so
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kfilemetadata/kfilemetadata_krita.so

%files devel
%defattr(644,root,root,755)
%{_libdir}/libKF6FileMetaData.so
%{_includedir}/KF6/KFileMetaData
%{_libdir}/cmake/KF6FileMetaData
