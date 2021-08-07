Name:           jose
Version:        11
Release:        1
Summary:        José is a command line utility for performing various tasks on JSON  objects
License:        ASL 2.0
URL:            https://github.com/latchset/%{name}
Source0:        https://github.com/latchset/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig, gcc, openssl-devel, zlib-devel, meson, ninja-build, asciidoc
BuildRequires:  jansson-devel >= 2.10

Provides:       lib%{name}
Provides:       lib%{name}-openssl
Provides:       lib%{name}-zlib

Obsoletes:      lib%{name}

%description
José is a C-language implementation of the Javascript Object
Signing and Encryption standards. José provides a command-line
utility which encompasses most of the JOSE features. This allows
for easy integration into your project and one-off scripts.

%package  devel
Summary:        Development libraries and files for lib%{name}
Requires:       pkgconfig, jansson-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}

Provides:       lib%{name}-devel
Provides:       lib%{name}-openssl-devel
Provides:       lib%{name}-zlib-devel

Obsoletes:      lib%{name}-devel

%description  devel
The package contains lib and header files for developing application
that use %{name}

%package help
Summary:        Documents files for %{name}
Requires:       man, info

%description help
Man pages and other related documents for %{name}

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf %{buildroot}
%meson_install
rm -rf %{buildroot}/%{_libdir}/lib%{name}.la

%check
%meson_test

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/%{name}
%{_libdir}/lib%{name}.so.*
%license COPYING

%files devel
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files help
%{_mandir}/man1/jose*.1*
%{_mandir}/man3/jose*.3*


%changelog
* Mon Aug 9 2021 zoulin<zoulin13@huawei.com> - 11-1
- Type:enhancement
- ID:NA
- SUG:NA
- DESC: update version to 11

* Sat Sep 21 2019 caomeng<caomeng5@huawei.com> - 10-5
- Type:other
- ID:NA
- SUG:NA
- DESC: move libjose into primary package

* Wed Sep 4 2019 caomeng<caomeng5@huawei.com> - 10-4
- Package init
