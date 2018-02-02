%global modulename mold-source-map
# npm(browserify) is missing dep for tests
%global enable_tests 0

Name:           nodejs-%{modulename}
Version:        0.4.0
Release:        1
Summary:        Mold a source map that is almost perfect for you into one that is
License:        MIT
URL:            https://github.com/thlorenz/mold-source-map
Source0:  			https://registry.npmjs.org/%{modulename}/-/%{modulename}-%{version}.tgz

BuildArch:      noarch
ExclusiveArch:	%{nodejs_arches} noarch
BuildRequires:  nodejs-packaging
BuildRequires:  npm(convert-source-map) npm(through)
%if 0%{?enable_tests}
BuildRequires:	npm(tap) npm(browserify)
%endif

%description
%{summary}.

%prep
%setup -n package
%nodejs_fixdep through '^2.3'

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{modulename}
cp -pr package.json index.js \
	%{buildroot}%{nodejs_sitelib}/%{modulename}
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} -e 'require("./")'
%if 0%{?enable_tests}
%{_bindir}/tap test/*.js
%else
%{_bindir}/echo -e "\e[101m -=#=- Tests disabled -=#=- \e[0m"
%endif

%files
%doc *.md
%license LICENSE
%{nodejs_sitelib}/%{modulename}

%changelog
* Thu Feb 1 2018 Christian Glombek <christian.glombek@rwth-aachen.de> - 0.4.0-1
- Initial RPM Spec
