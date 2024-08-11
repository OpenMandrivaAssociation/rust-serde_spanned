# Rust packages always list license files and docs
# inside the crate as well as the containing directory
%undefine _duplicate_files_terminate_build
# FIXME as of 0.6.7, tests fail
%bcond_with check
%global debug_package %{nil}

%global crate serde_spanned

Name:           rust-serde_spanned
Version:        0.6.7
Release:        1
Summary:        Serde-compatible spanned Value
Group:          Development/Rust

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/serde_spanned
Source:         %{crates_source}

ExclusiveArch:  %{rust_arches}

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  rust >= 1.65
%if %{with check}
BuildRequires:  (crate(serde-untagged/default) >= 0.1.0 with crate(serde-untagged/default) < 0.2.0~)
BuildRequires:  (crate(serde/default) >= 1.0.0 with crate(serde/default) < 2.0.0~)
BuildRequires:  (crate(serde_derive/default) >= 1.0.0 with crate(serde_derive/default) < 2.0.0~)
%endif

%global _description %{expand:
Serde-compatible spanned Value.}

%description %{_description}

%package        devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(serde_spanned) = 0.6.7
Requires:       cargo
Requires:       rust >= 1.65

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(serde_spanned/default) = 0.6.7
Requires:       cargo
Requires:       crate(serde_spanned) = 0.6.7

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
Group:          Development/Rust
BuildArch:      noarch
Provides:       crate(serde_spanned/serde) = 0.6.7
Requires:       (crate(serde/default) >= 1.0.145 with crate(serde/default) < 2.0.0~)
Requires:       cargo
Requires:       crate(serde_spanned) = 0.6.7

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif
